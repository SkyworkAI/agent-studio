:py:mod:`agent_studio.envs.desktop_env.human_interface`
=======================================================

.. py:module:: agent_studio.envs.desktop_env.human_interface


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.human_interface.WorkerSignals
   agent_studio.envs.desktop_env.human_interface.InputDialog
   agent_studio.envs.desktop_env.human_interface.ResetThread
   agent_studio.envs.desktop_env.human_interface.EvalTaskThread
   agent_studio.envs.desktop_env.human_interface.Task
   agent_studio.envs.desktop_env.human_interface.HumanInterface



Functions
~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.human_interface.extract_evaluator_meta



Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.human_interface.config
   agent_studio.envs.desktop_env.human_interface.logger
   agent_studio.envs.desktop_env.human_interface.REMOTE_SERVER_ADDR


.. py:data:: config

   

.. py:data:: logger

   

.. py:data:: REMOTE_SERVER_ADDR

   

.. py:class:: WorkerSignals


   Bases: :py:obj:`PyQt6.QtCore.QObject`

   .. py:attribute:: status_bar_signal

      

   .. py:attribute:: next_action_editor_signal

      

   .. py:attribute:: save_button_signal

      

   .. py:attribute:: step_action_button_signal

      

   .. py:attribute:: show_dialog_signal

      

   .. py:attribute:: evaluation_display_signal

      

   .. py:attribute:: eval_button_signal

      

   .. py:attribute:: annotator_panel_signal

      

   .. py:attribute:: popup_window_signal

      


.. py:class:: InputDialog(parent=None, message='')


   Bases: :py:obj:`PyQt6.QtWidgets.QDialog`

   .. py:method:: accept()



.. py:class:: ResetThread(agent: agent_studio.agent.human_agent.HumanAgent, signals: WorkerSignals, task_config: dict)


   Bases: :py:obj:`PyQt6.QtCore.QThread`

   .. py:method:: run()


   .. py:method:: receive_user_input(text: str)



.. py:class:: EvalTaskThread(signals: WorkerSignals, trajectory_display: PyQt6.QtWidgets.QTextEdit, selected_task: dict, result_queue: queue.Queue)


   Bases: :py:obj:`PyQt6.QtCore.QThread`

   .. py:method:: run()


   .. py:method:: receive_user_input(text: str)



.. py:function:: extract_evaluator_meta(file_path) -> tuple[str, list[dict]]

   Extracts the reset_handler and evaluate_handler         and their metadata from the evaluator.


.. py:class:: Task(instruction: str, trajectory: list[str], evals: list[dict], visual: bool, task_id: str | None = None)


   .. py:method:: step_action(action: str) -> None


   .. py:method:: to_record() -> dict


   .. py:method:: to_task_config() -> dict



.. py:class:: HumanInterface(record_path: str, task_config_path: str)


   Bases: :py:obj:`PyQt6.QtWidgets.QMainWindow`

   .. py:method:: setup_ui() -> None

      Sets up the UI, including the VNC frame (left) and the right layout.


   .. py:method:: reset() -> None

      Clears all the text fields.


   .. py:method:: show_popup_dialog(title: str, message: str) -> None

      Shows a popup message.


   .. py:method:: start_record() -> None

      Starts the record.


   .. py:method:: generate_annotation() -> None


   .. py:method:: show_input_dialog(message: str) -> None


   .. py:method:: show_choice_dialog(message: str) -> None


   .. py:method:: set_task_status_bar_text(color: str, text: str) -> None


   .. py:method:: load_evaluator_args(base_path: str = 'agent_studio/envs/desktop_env/evaluators') -> None

      Loads the evaluator arguments.


   .. py:method:: evaluator_changed(index)


   .. py:method:: load_functions(evaluator_name)


   .. py:method:: list_item_changed(current, previous)


   .. py:method:: load_existing_task_configs() -> None


   .. py:method:: populate_instruction_selection_widget() -> None


   .. py:method:: task_list_double_clicked(item: PyQt6.QtWidgets.QListWidgetItem) -> None


   .. py:method:: method_list_double_clicked(item: PyQt6.QtWidgets.QListWidgetItem) -> None


   .. py:method:: step_action() -> None

      Steps the next action and adds it to the trajectory.


   .. py:method:: save_trajectory() -> None

      Saves the trajectory to the record path.


   .. py:method:: eval_task()


   .. py:method:: reconnect()


   .. py:method:: update_screen()


   .. py:method:: render()


   .. py:method:: closeEvent(event)



