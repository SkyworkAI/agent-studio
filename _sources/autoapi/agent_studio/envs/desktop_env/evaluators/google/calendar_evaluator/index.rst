:py:mod:`agent_studio.envs.desktop_env.evaluators.google.calendar_evaluator`
============================================================================

.. py:module:: agent_studio.envs.desktop_env.evaluators.google.calendar_evaluator


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.google.calendar_evaluator.GoogleCalendarEvaluator



Functions
~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.google.calendar_evaluator.time_match
   agent_studio.envs.desktop_env.evaluators.google.calendar_evaluator.event_match
   agent_studio.envs.desktop_env.evaluators.google.calendar_evaluator.reminders_match



Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.google.calendar_evaluator.config
   agent_studio.envs.desktop_env.evaluators.google.calendar_evaluator.logger


.. py:data:: config

   

.. py:data:: logger

   

.. py:function:: time_match(timestamp1: str, timestamp2: str) -> bool

   Checks if the pred time matches the ref time.


.. py:function:: event_match(event1: dict, event2: dict) -> bool

   Checks if the event2 matches the event1.


.. py:function:: reminders_match(reminder1: dict, reminder2: dict) -> bool

   Compares two reminder structures for equality.


.. py:class:: GoogleCalendarEvaluator(eval_procedure: list[dict], reset_procedure: list[dict])


   Bases: :py:obj:`agent_studio.envs.desktop_env.evaluators.google.evaluator_base.GoogleEvaluatorBase`

   .. py:attribute:: name
      :type: str
      :value: 'google_calendar'

      

   .. py:attribute:: prompt
      :type: str
      :value: 'evaluators/google/calendar_prompt'

      

   .. py:method:: check_event_exists(event_info: dict[str, Any], exists: bool) -> None

      Check if the event exists on the calendar.

      :param event_info: Event information.
      :type event_info: dict[str, Any]
      :param exists: Whether the event should exist.
      :type exists: bool

      :raises FeedbackException: If the event exists does not match the expected value.

      :returns: None

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


   .. py:method:: clear_calendar() -> None

      Clears all events on the calendar.


   .. py:method:: create_event(event_info: dict[str, Any]) -> None

      Creates an event on the calendar.


   .. py:method:: delete_event(event_info: dict[str, Any]) -> None

      Deletes events that match the given event.


   .. py:method:: list_events() -> list[dict]

      Lists all events on the calendar.


   .. py:method:: search_events_by_time_range(start_time: str, end_time: str) -> list[dict[str, Any]]

      Searches for events that fall within the given time range.


   .. py:method:: search_events(event_info: dict[str, Any]) -> list[dict[str, str]]

      Searches for events that match the reference event.


   .. py:method:: delete_event_by_id(event_id: str) -> None

      Deletes an event on the calendar.



