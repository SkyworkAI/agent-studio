import bisect
import copy
import json
import logging
import pathlib
import sys
import uuid
from enum import Enum
from typing import get_origin

import cv2
from PIL import Image
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QAction
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QFileDialog,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QMenu,
    QMenuBar,
    QMessageBox,
    QPushButton,
    QScrollArea,
    QSlider,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from agent_studio.recorder.utils import (
    Event,
    KeyboardAction,
    KeyboardActionAdvanced,
    KeyboardEvent,
    KeyboardEventAdvanced,
    MouseAction,
    MouseActionAdvanced,
    MouseEvent,
    MouseEventAdvanced,
    Record,
)
from agent_studio.utils.types import Action, Episode

# from qfluentwidgets import FluentTranslator

logger = logging.getLogger(__name__)


class ImageExtractor:
    def __init__(self, video_path: str):
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)

        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.duration = self.total_frames / self.fps

    # Extract the frame no later than the target time
    def extract_left(self, target_time: float) -> Image.Image | None:
        frame_no = int(target_time * self.fps)
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
        ret, frame = self.cap.read()
        if not ret:
            logging.info("Cannot find frame for the target time")
            return None
        return Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Extract the frame no earlier than the target time
    def extract_right(self, target_time: float) -> Image.Image | None:
        frame_no = int(target_time * self.fps) + 1
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
        ret, frame = self.cap.read()
        if not ret:
            logging.info("Cannot find frame for the target time")
            return None
        return Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))


def convert_to_episode(record: Record, base_path: pathlib.Path) -> Episode:
    extractor = ImageExtractor((base_path / record.video.path).as_posix())
    # use the name of the action as the action space
    action_space = list(KeyboardActionAdvanced.__members__.keys()) + list(
        MouseActionAdvanced.__members__.keys()
    )

    episode: Episode = Episode(
        instruction=record.instruction,
        annotation_id=record.annotation_id,
        actions=[],
        source="agent-studio",
        platform="desktop",
        metadata={},
        action_space=action_space,
        is_success=True,
    )

    img_folder = base_path / "image"
    img_folder.mkdir(exist_ok=True)

    obs_after_image_path: str | None = None
    last_event: Event | None = None
    for idx, event in enumerate(record.events):
        action_id = uuid.uuid4().hex
        if last_event is None:
            obs_before_image = extractor.extract_left(event.time / 2)
        else:
            obs_before_image = extractor.extract_left(
                (last_event.time + last_event.duration + event.time) / 2
            )
        # obs_after_image = extractor.extract_right(event.time)
        if obs_before_image is not None:
            image_save_path = img_folder / f"{action_id}.png"
            obs_before_image_path = image_save_path.relative_to(base_path).as_posix()
            obs_before_image.save(image_save_path)
        else:
            logging.error("No first frame")
            obs_before_image_path = None

        if len(episode.actions) > 0:
            episode.actions[-1].obs_after = obs_before_image_path

        if isinstance(event, KeyboardEventAdvanced):
            action = Action(
                action_id=action_id,
                obs_before=obs_before_image_path,
                obs_after=obs_after_image_path,
                operation=event.action.name,
                bbox=None,
                metadata={"note": event.note, "repr": str(event)},
            )
            episode.actions.append(action)
        # elif isinstance(event, KeyboardEvent):
        #     action = Action(
        #         action_id=action_id,
        #         obs_before=obs_before_image_path,
        #         obs_after=obs_after_image_path,
        #         operation=event.action.name,
        #         bbox=None,
        #         metadata={
        #             "ascii": event.ascii,
        #             "note": event.note,
        #             "repr": str(event)
        #         }
        #     )
        #     episode.actions.append(action)
        # elif isinstance(event, MouseEvent):
        #     action = Action(
        #         action_id=action_id,
        #         obs_before=obs_before_image_path,
        #         obs_after=obs_after_image_path,
        #         operation=event.action.name,
        #         bbox={
        #             "x": event.x, "y": event.y,
        #             "width": 1.0, "height": 1.0
        #         },
        #         metadata={
        #             "repr": str(event)
        #         }
        #     )
        #     episode.actions.append(action)
        elif isinstance(event, MouseEventAdvanced):
            action = Action(
                action_id=action_id,
                obs_before=obs_before_image_path,
                obs_after=obs_after_image_path,
                operation=event.action.name,
                bbox=(
                    {"x": event.x1, "y": event.y1, "width": 1.0, "height": 1.0}
                    if event.action != MouseActionAdvanced.MOUSE_DRAG
                    else None
                ),
                metadata={
                    "button": event.button,
                    "from": {"x": event.x1, "y": event.y1},
                    "to": {"x": event.x2, "y": event.y2},
                    "repr": str(event),
                },
            )
            episode.actions.append(action)
        else:
            logging.error(f"Unsupported event type: {type(event)}")

        obs_after_image_path = obs_before_image_path
        last_event = copy.deepcopy(event)

    if len(episode.actions) > 0 and last_event is not None:
        obs_after_image = extractor.extract_left(
            (last_event.time + extractor.duration) / 2
        )
        action_id = uuid.uuid4().hex
        if obs_after_image is not None:
            image_save_path = img_folder / f"{action_id}.png"
            obs_after_image_path = image_save_path.relative_to(base_path).as_posix()
            obs_after_image.save(image_save_path)
        else:
            logging.error("No first frame")
            obs_after_image_path = None
        episode.actions[-1].obs_after = obs_after_image_path

    return episode


def aggregate_mouse_events(events: list[Event]) -> list[Event]:
    aggregated_events: list[Event] = []
    mouse_events = {}

    for event in events:
        if isinstance(event, MouseEvent):
            if event.action == MouseAction.MOUSE_PRESSED:
                if event.button not in mouse_events:
                    mouse_events[event.button] = event
                else:
                    logging.error(f"Mouse button {event.button} is already pressed")
            elif event.action == MouseAction.MOUSE_RELEASED:
                if event.button in mouse_events:
                    if (
                        mouse_events[event.button].x == event.x
                        and mouse_events[event.button].y == event.y
                    ):
                        aggregated_events.append(
                            MouseEventAdvanced(
                                time=mouse_events[event.button].time,
                                event_type="mouse",
                                action=MouseActionAdvanced.MOUSE_CLICK,
                                x1=mouse_events[event.button].x,
                                y1=mouse_events[event.button].y,
                                button=event.button,
                            )
                        )
                    else:
                        aggregated_events.append(
                            MouseEventAdvanced(
                                time=mouse_events[event.button].time,
                                duration=event.time - mouse_events[event.button].time,
                                event_type="mouse",
                                action=MouseActionAdvanced.MOUSE_DRAG,
                                x1=mouse_events[event.button].x,
                                y1=mouse_events[event.button].y,
                                x2=event.x,
                                y2=event.y,
                                button=event.button,
                            )
                        )
                    mouse_events.pop(event.button)
                else:
                    logging.error(f"Mouse button {event.button} is not pressed")
            elif event.action == MouseAction.MOUSE_SCROLL_UP:
                aggregated_events.append(
                    MouseEventAdvanced(
                        time=event.time,
                        event_type="mouse",
                        action=MouseActionAdvanced.MOUSE_SCROLL_UP,
                        x1=event.x,
                        y1=event.y,
                        button=event.button,
                        x2=event.dx,
                        y2=event.dy,
                    )
                )
            elif event.action == MouseAction.MOUSE_SCROLL_DOWN:
                aggregated_events.append(
                    MouseEventAdvanced(
                        time=event.time,
                        event_type="mouse",
                        action=MouseActionAdvanced.MOUSE_SCROLL_DOWN,
                        x1=event.x,
                        y1=event.y,
                        button=event.button,
                        x2=event.dx,
                        y2=event.dy,
                    )
                )
        else:
            aggregated_events.append(event)

    return sorted(aggregated_events)


def is_visiable_ascii(ascii_code) -> bool:
    if 0 <= ascii_code <= 31 or ascii_code == 127:
        return False
    else:
        return True


def aggregate_keyboard_events(events: list[Event]) -> list[Event]:
    aggregated_event: Event | None = None
    key_events: dict[int, KeyboardEvent] = {}
    modif_key_events: dict[int, KeyboardEvent] = {}

    for event in events:
        if isinstance(event, KeyboardEvent):
            if event.action == KeyboardAction.KEY_DOWN:
                assert (
                    event.key_code not in key_events
                    and event.key_code not in modif_key_events
                ), f"Key {event.key_code} is already pressed"
                if event.ascii is not None:
                    # normal key press
                    key_events[event.key_code] = event
                    # if invisiable key, it's probably a shortcut
                    if not is_visiable_ascii(event.ascii):
                        assert event.note is not None
                        if aggregated_event is None:
                            aggregated_event = KeyboardEventAdvanced(
                                time=event.time,
                                event_type="keyboard",
                                action=KeyboardActionAdvanced.KEY_SHORTCUT,
                                note=event.note,
                            )
                        break
                    else:
                        if len(modif_key_events) == 0:
                            # typing
                            assert event.note is not None
                            if aggregated_event is None:
                                aggregated_event = KeyboardEventAdvanced(
                                    time=event.time,
                                    event_type="keyboard",
                                    action=KeyboardActionAdvanced.KEY_TYPE,
                                    note=event.note,
                                )
                            else:
                                aggregated_event.note += event.note
                                aggregated_event.duration = (
                                    event.time - aggregated_event.time
                                )
                        else:
                            # shortcut
                            key_str = " + ".join(
                                sorted([str(e.note) for e in modif_key_events.values()])
                                + sorted([str(e.note) for e in key_events.values()])
                            )
                            aggregated_event = KeyboardEventAdvanced(
                                time=event.time,
                                event_type="keyboard",
                                action=KeyboardActionAdvanced.KEY_SHORTCUT,
                                note=key_str,
                            )
                else:
                    # modifier keys
                    modif_key_events[event.key_code] = event
            elif event.action == KeyboardAction.KEY_UP:
                if len(modif_key_events) == 1 and len(key_events) == 0:
                    # single modifier key
                    assert modif_key_events[event.key_code].note is not None
                    aggregated_event = KeyboardEventAdvanced(
                        time=event.time,
                        event_type="keyboard",
                        action=KeyboardActionAdvanced.KEY_PRESS,
                        note=modif_key_events[event.key_code].note,
                    )
                    break
                else:
                    if event.ascii is not None:
                        key_events.pop(event.key_code, None)
                    else:
                        modif_key_events.pop(event.key_code, None)
        elif isinstance(event, KeyboardEventAdvanced):
            if event.action == KeyboardActionAdvanced.KEY_TYPE:
                if aggregated_event is None:
                    aggregated_event = copy.deepcopy(event)
                else:
                    assert event.note is not None
                    aggregated_event.note += event.note
                    aggregated_event.duration = event.time - aggregated_event.time
            else:
                aggregated_event = copy.deepcopy(event)
        elif aggregated_event is not None:
            break

    return [aggregated_event] if aggregated_event is not None else []


def aggregate_events(events: list[Event]) -> list[Event]:
    # Aggregate events, e.g. for keyboard events, aggregate
    # consecutive key presses into a single event, KEY_TYPE
    aggregated_events: list[Event] = []
    cur_keyboard_event: KeyboardEventAdvanced | None = None
    modif_keys: set[str] = set()

    for event in events:
        if isinstance(event, KeyboardEvent):
            if event.action == KeyboardAction.KEY_DOWN:
                if event.ascii is not None:
                    # notmal key press
                    if len(modif_keys) == 0:
                        # typing
                        if cur_keyboard_event is None:
                            cur_keyboard_event = KeyboardEventAdvanced(
                                time=event.time,
                                event_type="keyboard",
                                action=KeyboardActionAdvanced.KEY_TYPE,
                                key_code=[event.key_code],
                                note=chr(event.ascii),
                            )
                        else:
                            assert cur_keyboard_event.note is not None
                            cur_keyboard_event.key_code.append(event.key_code)
                            cur_keyboard_event.note += chr(event.ascii)
                            cur_keyboard_event.duration = (
                                event.time - cur_keyboard_event.time
                            )
                    else:
                        # shortcut
                        aggregated_events.append(event)
                else:
                    # modifier keys
                    if cur_keyboard_event is not None:
                        aggregated_events.append(cur_keyboard_event)
                        cur_keyboard_event = None
                    assert event.note is not None
                    modif_keys.add(event.note)
                    aggregated_events.append(event)
            if event.action == KeyboardAction.KEY_UP:
                if event.ascii is None:
                    # modifier keys
                    assert event.note is not None
                    modif_keys.discard(event.note)
                if len(modif_keys) != 0:
                    # ignore key up event if there are no modifier keys pressed
                    aggregated_events.append(event)
        elif isinstance(event, MouseEvent):
            cur_keyboard_event = None
            aggregated_events.append(event)
        elif isinstance(event, KeyboardEventAdvanced):
            if event.action == KeyboardActionAdvanced.KEY_TYPE:
                if cur_keyboard_event is None:
                    cur_keyboard_event = copy.deepcopy(event)
                else:
                    assert cur_keyboard_event.note is not None
                    assert event.note is not None
                    cur_keyboard_event.key_code.extend(event.key_code)
                    cur_keyboard_event.note += event.note
                    cur_keyboard_event.duration = event.time - cur_keyboard_event.time
            else:
                aggregated_events.append(event)
        else:
            aggregated_events.append(event)
    if cur_keyboard_event is not None:
        aggregated_events.append(cur_keyboard_event)

    return sorted(aggregated_events)


class TrajectoryEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trajectory Editor")
        self.setGeometry(100, 100, 1000, 600)

        self.record: Record | None = None
        self.current_event: Event | None = None
        self.current_file = None

        self.create_menu_bar()

        # Main layout
        main_layout = QHBoxLayout()

        # Video widget (left side)
        video_layout = QVBoxLayout()

        # Show opened file path
        self.file_path_label = QLabel("No file opened")
        self.file_path_label.setFixedHeight(30)
        video_layout.addWidget(self.file_path_label)

        # Show instruction
        self.instruction_label = QLabel("Instruction: ")
        self.instruction_label.setFixedHeight(30)
        video_layout.addWidget(self.instruction_label)

        self.video_widget = QVideoWidget()
        self.media_player = QMediaPlayer()
        self.media_player.setVideoOutput(self.video_widget)
        video_layout.addWidget(self.video_widget)

        # Create a horizontal layout for the controls
        controls_layout = QHBoxLayout()

        # Add play button to the controls layout
        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.play_pause)
        self.play_button.setFixedHeight(30)
        controls_layout.addWidget(self.play_button)

        # Add seek slider to the controls layout
        self.seek_slider = QSlider(Qt.Orientation.Horizontal)
        self.seek_slider.sliderMoved.connect(self.set_position)
        self.seek_slider.setFixedHeight(10)
        controls_layout.addWidget(self.seek_slider)

        # Add time label to the controls layout, format: mm:ss::ms
        self.time_label = QLabel("00:00:000 / 00:00:000")
        self.time_label.setFixedHeight(30)
        controls_layout.addWidget(self.time_label)

        # Add the controls layout to the video layout
        video_layout.addLayout(controls_layout)

        video_container = QWidget()
        video_container.setLayout(video_layout)
        main_layout.addWidget(video_container, 2)

        # Right side layout
        right_layout = QVBoxLayout()

        # List widget (middle-right)
        self.list_widget = QListWidget()
        self.list_widget.setSelectionMode(QListWidget.SelectionMode.ExtendedSelection)
        # single click to show event details
        self.list_widget.itemSelectionChanged.connect(self.update_event_details)
        # double click to seek the video to the event time
        self.list_widget.itemDoubleClicked.connect(self.seek_to_event)
        right_layout.addWidget(self.list_widget)

        # Event details widget (bottom-right)
        self.event_details_widget = QWidget()
        self.event_details_layout = QFormLayout()
        self.event_details_widget.setLayout(self.event_details_layout)

        # Create a scroll area and set the event details widget as its widget
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.event_details_widget)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFixedHeight(200)  # Adjust the size as needed
        right_layout.addWidget(self.scroll_area)

        right_container = QWidget()
        right_container.setLayout(right_layout)
        main_layout.addWidget(right_container, 1)

        # Set the main layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Connect media player signals
        self.media_player.positionChanged.connect(self.position_changed)
        self.media_player.durationChanged.connect(self.duration_changed)

        # shortcut ctrl+n to open a new record
        new_shortcut = QAction(self)
        new_shortcut.setShortcut("Ctrl+N")
        new_shortcut.triggered.connect(self.open_file)
        self.addAction(new_shortcut)

        # shortcut ctrl+e to export the record
        export_shortcut = QAction(self)
        export_shortcut.setShortcut("Ctrl+E")
        export_shortcut.triggered.connect(self.export_file)
        self.addAction(export_shortcut)

        # Shortcut d to delete the selected event
        delete_shortcut = QAction(self)
        delete_shortcut.setShortcut("D")
        delete_shortcut.triggered.connect(self.delete_event)
        self.addAction(delete_shortcut)

        # Shortcut A to aggregate the selected event
        aggregate_shortcut = QAction(self)
        aggregate_shortcut.setShortcut("A")
        aggregate_shortcut.triggered.connect(self.aggregate_events)
        self.addAction(aggregate_shortcut)

        # Shortcut ctrl+s to save the record
        save_shortcut = QAction(self)
        save_shortcut.setShortcut("Ctrl+S")
        save_shortcut.triggered.connect(self.save_file)
        self.addAction(save_shortcut)

    def create_menu_bar(self):
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        # File menu
        file_menu = QMenu("File", self)
        menu_bar.addMenu(file_menu)

        # Open action
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        # Save action
        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        # Save As action
        save_as_action = QAction("Save As", self)
        save_as_action.triggered.connect(self.save_file_as)
        file_menu.addAction(save_as_action)

        # Export action as idm format
        export_action = QAction("Export", self)
        export_action.triggered.connect(self.export_file)
        file_menu.addAction(export_action)

    # -- List Widget Slots --#

    def seek_to_event(self, item):
        selected_index = self.list_widget.row(item)
        if self.record is not None:
            self.media_player.setPosition(
                int(self.record.events[selected_index].time * 1000)
            )

    def delete_event(self):
        selected_items = self.list_widget.selectedItems()
        if self.record is not None:
            for item in selected_items:
                selected_index = self.list_widget.row(item)
                self.record.events.pop(selected_index)
                self.list_widget.takeItem(selected_index)

    def update_event_details(self):
        # Clear previous details
        for i in reversed(range(self.event_details_layout.rowCount())):
            self.event_details_layout.removeRow(i)

        selected_items = self.list_widget.selectedItems()
        if not selected_items or self.record is None:
            self.current_event = None
            return

        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(self.delete_event)
        self.event_details_layout.addRow(delete_button)

        # Dynamically create UI elements based on event type
        if len(selected_items) == 1:
            selected_index = self.list_widget.row(selected_items[0])
            self.current_event = self.record.events[selected_index]
            # Add static fields
            self.event_details_layout.addRow(
                "Event Type:", QLabel(self.current_event.event_type)
            )
            self.create_dynamic_ui(self.current_event)
        else:
            # Multiple items selected, show advanced options
            # all selected events should have the same type
            event_types = set()
            for item in selected_items:
                selected_index = self.list_widget.row(item)
                event_types.add(self.record.events[selected_index].event_type)
            # add a aggregate button to aggregate the selected events
            aggregate_button = QPushButton("Aggregate")
            aggregate_button.clicked.connect(self.aggregate_events)
            self.event_details_layout.addRow(aggregate_button)
            if len(event_types) == 1:
                aggregated_events = aggregate_keyboard_events(
                    [
                        self.record.events[self.list_widget.row(item)]
                        for item in selected_items
                    ]
                )
                # only display the first aggregated event
                if len(aggregated_events) > 0:
                    self.current_event = aggregated_events[0]
                    self.create_dynamic_ui(aggregated_events[0])

    def aggregate_events(self):
        if self.record is None or self.current_event is None:
            return
        # Delete the selected events
        # and insert self.current_event to the record
        selected_items = self.list_widget.selectedItems()
        selected_indices = [self.list_widget.row(item) for item in selected_items]
        for i in reversed(selected_indices):
            self.record.events.pop(i)
        self.record.events.append(self.current_event)
        self.list_widget.clear()
        self.record.events = sorted(self.record.events)
        self._reload_events()

    def create_dynamic_ui(self, event: Event):
        for field_name, field in event.model_fields.items():
            if field_name in ["event_type"]:
                continue  # Skip static fields

            field_type = field.annotation
            field_value = getattr(event, field_name)

            label = QLabel(field_name.capitalize() + ":")
            widget = self.create_widget_for_field(field_name, field_type, field_value)

            if widget:
                self.event_details_layout.addRow(label, widget)

    def create_widget_for_field(self, field_name, field_type, field_value):
        if isinstance(field_type, type) and issubclass(field_type, Enum):
            widget = QComboBox()
            widget.addItems([e.name for e in field_type])
            if field_value:
                widget.setCurrentText(field_value.name)
            widget.currentTextChanged.connect(
                lambda text: self.update_field(field_name, field_type[text])
            )
        elif field_type == bool or get_origin(field_type) == bool:
            widget = QCheckBox()
            if field_value is not None:
                widget.setChecked(field_value)
            widget.stateChanged.connect(
                lambda state: self.update_field(field_name, bool(state))
            )
        elif field_type == int or get_origin(field_type) == int:
            widget = QSpinBox()
            widget.setMaximum(999999)
            widget.setMinimum(0)
            if field_value is not None:
                widget.setValue(field_value)
            widget.valueChanged.connect(
                lambda value: self.update_field(field_name, value)
            )
        elif field_type == float or get_origin(field_type) == float:
            widget = QDoubleSpinBox()
            widget.setDecimals(9)
            if field_value is not None:
                widget.setValue(field_value)
            widget.valueChanged.connect(
                lambda value: self.update_field(field_name, value)
            )
        elif field_type == str or get_origin(field_type) == str:
            widget = QLineEdit(str(field_value) if field_value is not None else "")
            widget.textChanged.connect(lambda text: self.update_field(field_name, text))
        else:
            # For complex types, use a QLabel for now
            widget = QLabel(str(field_value) if field_value is not None else "")

        return widget

    def update_field(self, field_name, value):
        if self.current_event is not None:
            setattr(self.current_event, field_name, value)
            self.update_list_item()

    def update_list_item(self):
        selected_items = self.list_widget.selectedItems()
        if len(selected_items) == 1 and self.current_event is not None:
            selected_items[0].setText(self.current_event.format())

    # Menu Bar Slots #

    def _reload_events(self):
        if self.record is None or self.current_file is None:
            return
        self.list_widget.clear()
        base_path = pathlib.Path(self.current_file).parent
        self.media_player.setSource(
            QUrl.fromLocalFile((base_path / self.record.video.path).as_posix())
        )
        self.list_widget.clear()
        for i, event in enumerate(self.record.events):
            self.list_widget.addItem(event.format())

    def _load_file(self, file_name):
        if file_name:
            self.current_file = file_name
            try:
                with open(file_name, "r") as f:
                    self.record = Record.model_validate(json.load(f))
                    assert self.record is not None
                    self.record.events = aggregate_mouse_events(self.record.events)
                    self._reload_events()
                    self.file_path_label.setText(file_name)
                    self.instruction_label.setText(
                        f"Instruction: {self.record.instruction}"
                    )
            except Exception as e:
                QMessageBox.critical(
                    self, "Load Failed", f"An error occurred while loading: {str(e)}"
                )

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Record Trajectory")
        self._load_file(file_name)

    def save_file(self):
        if self.current_file:
            self.save_to_file(self.current_file)
        else:
            self.save_file_as()

    def save_file_as(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Record Trajectory")
        if file_name:
            self.current_file = file_name
            self.save_to_file(file_name)

    def save_to_file(self, file_name):
        if self.record is None:
            QMessageBox.critical(self, "Save Failed", "No record to save.")
            return
        try:
            json_str = self.record.model_dump_json(indent=4)
            with open(file_name, "w") as f:
                f.write(json_str)
            QMessageBox.information(self, "Save Successful", "File saved successfully.")
        except Exception as e:
            QMessageBox.critical(
                self, "Save Failed", f"An error occurred while saving: {str(e)}"
            )

    def export_file(self):
        if self.record is None or self.current_file is None:
            QMessageBox.critical(self, "Export Failed", "No record to export.")
            return
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Export Record Trajectory",
            (pathlib.Path(self.current_file) / "trajectory.jsonl").as_posix(),
        )
        if file_name:
            try:
                for event in self.record.events:
                    if not isinstance(event, KeyboardEventAdvanced) and not isinstance(
                        event, MouseEventAdvanced
                    ):
                        raise ValueError(
                            "Please aggregate the events before exporting."
                        )
                episode = convert_to_episode(
                    self.record, pathlib.Path(file_name).parent
                )
                json_str = episode.model_dump_json()
                with open(file_name, "w") as f:
                    f.write(json_str + "\n")
                QMessageBox.information(
                    self, "Export Successful", "File exported successfully."
                )
            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Export Failed",
                    f"An error occurred while exporting: {str(e)}",
                )

    # Media Player Slots #

    def play_pause(self):
        if self.media_player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.media_player.pause()
            self.play_button.setText("Play")
        else:
            self.media_player.play()
            self.play_button.setText("Pause")

    def handle_item_color(self):
        # find out the current event
        if self.record is not None:
            # position is in milliseconds
            idx = (
                bisect.bisect_right(
                    self.record.events,
                    Event(time=self.media_player.position() / 1000.0, event_type=""),
                )
                - 1
            )
            # change the corresponding item to green
            for i in range(self.list_widget.count()):
                item = self.list_widget.item(i)
                if item is None:
                    logging.error("Item is None")
                    continue
                if i == idx:
                    item.setBackground(Qt.GlobalColor.green)
                elif i == idx + 1:
                    item.setBackground(Qt.GlobalColor.yellow)
                else:
                    item.setBackground(Qt.GlobalColor.white)

    def set_position(self, position):
        self.media_player.setPosition(position)

    def position_changed(self, position):
        self.seek_slider.setValue(position)
        self.handle_item_color()
        # Update the time label, format the time as mm:ss::ms
        self.time_label.setText(
            f"{position // 60000:02}:{(position // 1000) % 60:02}"
            f":{position % 1000:03} / "
            f"{self.media_player.duration() // 60000:02}"
            f":{(self.media_player.duration() // 1000) % 60:02}"
            f":{self.media_player.duration() % 1000:03}"
        )

    def duration_changed(self, duration):
        self.seek_slider.setRange(0, duration)


def main():
    app = QApplication(sys.argv)
    player = TrajectoryEditor()
    player.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
