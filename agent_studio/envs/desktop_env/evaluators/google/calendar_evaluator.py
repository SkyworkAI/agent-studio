import logging
from datetime import datetime, timezone
from typing import Any

from agent_studio.config import Config
from agent_studio.envs.desktop_env.evaluators.evaluator import (
    Evaluator,
    FeedbackException,
    evaluation_handler,
    reset_handler,
)
from agent_studio.envs.desktop_env.evaluators.google.gservice import GoogleService
from agent_studio.utils.human_utils import confirm_action

config = Config()
logger = logging.getLogger(__name__)


def time_match(timestamp1: str, timestamp2: str) -> bool:
    """Checks if the pred time matches the ref time."""
    timestamp1 = timestamp1.replace("Z", "+00:00")
    timestamp2 = timestamp2.replace("Z", "+00:00")
    dt1 = datetime.fromisoformat(timestamp1).astimezone(timezone.utc)
    dt2 = datetime.fromisoformat(timestamp2).astimezone(timezone.utc)

    return dt1 == dt2


def event_match(
    event1: dict,
    event2: dict,
) -> bool:
    """Checks if the event2 matches the event1."""
    for key, value in event1.items():
        pred_value = event2.get(key, None)
        if key in ["summary", "description", "location"]:
            if value != pred_value:
                return False
        elif key in ["start", "end"]:
            if not (
                "dateTime" in value
                and "dateTime" in pred_value
                and time_match(value["dateTime"], pred_value["dateTime"])
            ):
                return False
        elif key == "recurrence" or key == "colorId":
            if value != pred_value:
                return False
        elif key == "attendees":
            emails1 = {attendee["email"] for attendee in value}
            emails2 = (
                {attendee["email"] for attendee in pred_value} if pred_value else set()
            )
            if emails1 != emails2:
                return False
        elif key == "reminders":
            if not reminders_match(value, pred_value):
                return False
    return True


def reminders_match(reminder1: dict, reminder2: dict) -> bool:
    """Compares two reminder structures for equality."""
    if reminder1.get("useDefault") != reminder2.get("useDefault"):
        return False
    overrides1 = {
        f"{r['method']}-{r['minutes']}": r for r in reminder1.get("overrides", [])
    }
    overrides2 = {
        f"{r['method']}-{r['minutes']}": r for r in reminder2.get("overrides", [])
    }
    return overrides1 == overrides2


class GoogleCalendarEvaluator(Evaluator):
    name: str = "google_calendar"

    def __init__(
        self,
    ) -> None:
        super().__init__()
        self.service = GoogleService(
            scopes=[
                "https://www.googleapis.com/auth/calendar",
            ],
            service_name="calendar",
            service_version="v3",
        ).service

    @evaluation_handler("check_event_exists")
    def check_event_exists(
        self,
        event_info: dict[str, Any],
        exists: bool,
    ) -> None:
        """
        Check if the event exists on the calendar.

        Args:
            event_info (dict[str, Any]): Event information.
            exists (bool): Whether the event should exist.

        Raises:
            FeedbackException: If the event exists does not match the expected value.

        Returns:
            None

        Example::

            event_info = {
                "summary": "Meeting with John",
                "description": "Discuss the project",
                "location": "Office",
                "start": {
                    "dateTime": "2022-01-01T10:00:00Z",
                },
                "end": {
                    "dateTime": "2022-01-01T11:00:00Z",
                },
            }
        """
        events = self.search_events(event_info)
        event_exists = len(events) > 0

        if event_exists != exists:
            raise FeedbackException(
                f"The error occured when checking the existence of {event_info}. "
                f"It should be {exists}."
            )

    @reset_handler("clear_calendar")
    def clear_calendar(self) -> None:
        """Clears all events on the calendar."""

        @confirm_action("Clearing all events on the calendar")
        def _clear_calendar() -> None:
            events = self.list_events()
            for event in events:
                self.service.events().delete(
                    calendarId=config.google_calendar_id, eventId=event["id"]
                ).execute()
            logger.debug("All events have been deleted.")

        logger.debug("Clearing all events on the calendar")
        _clear_calendar()

    @reset_handler("create_event")
    def create_event(
        self,
        event_info: dict[str, Any],
    ) -> None:
        """Creates an event on the calendar."""
        self.service.events().insert(
            calendarId=config.google_calendar_id, body=event_info
        ).execute()

    @reset_handler("delete_event")
    def delete_event(
        self,
        event_info: dict[str, Any],
    ) -> None:
        """Deletes events that match the given event."""
        events = self.search_events_by_time_range(
            start_time=event_info["start"]["dateTime"],
            end_time=event_info["end"]["dateTime"],
        )
        for event in events:
            if event_match(event_info, event):
                logger.debug(f"Deleting event: {event['summary']}")
                confirm_action(f"Deleting event: {event['summary']}")(
                    self.delete_event_by_id
                )(event["id"])

    def list_events(self) -> list[dict]:
        """Lists all events on the calendar."""
        events = []
        page_token = None
        while True:
            events_result = (
                self.service.events()
                .list(calendarId=config.google_calendar_id, pageToken=page_token)
                .execute()
            )
            events.extend(events_result["items"])
            page_token = events_result.get("nextPageToken")
            if not page_token:
                break
        return events

    def search_events_by_time_range(
        self,
        start_time: str,
        end_time: str,
    ) -> list[dict[str, Any]]:
        """Searches for events that fall within the given time range."""
        events = []
        page_token = None
        while True:
            events_result = (
                self.service.events()
                .list(
                    calendarId=config.google_calendar_id,
                    timeMin=start_time,
                    timeMax=end_time,
                    singleEvents=True,
                )
                .execute()
            )
            events.extend(events_result["items"])
            page_token = events_result.get("nextPageToken")
            if not page_token:
                break
        return events

    def search_events(self, event_info: dict[str, Any]) -> list[dict[str, str]]:
        """Searches for events that match the reference event."""
        events = self.search_events_by_time_range(
            start_time=event_info["start"]["dateTime"],
            end_time=event_info["end"]["dateTime"],
        )
        results = []
        for event in events:
            if event_match(event_info, event):
                results.append(event)
        return results

    def delete_event_by_id(self, event_id: str) -> None:
        """Deletes an event on the calendar."""
        self.service.events().delete(
            calendarId=config.google_calendar_id, eventId=event_id
        ).execute()
        logger.info(f"Event with ID {event_id} has been deleted.")
