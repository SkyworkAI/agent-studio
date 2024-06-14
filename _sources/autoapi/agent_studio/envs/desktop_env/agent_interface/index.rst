:py:mod:`agent_studio.envs.desktop_env.agent_interface`
=======================================================

.. py:module:: agent_studio.envs.desktop_env.agent_interface


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.agent_interface.FrameBuffer
   agent_studio.envs.desktop_env.agent_interface.WorkerSignals
   agent_studio.envs.desktop_env.agent_interface.InputDialog
   agent_studio.envs.desktop_env.agent_interface.ResetRuntimeThread
   agent_studio.envs.desktop_env.agent_interface.ResetTaskThread
   agent_studio.envs.desktop_env.agent_interface.GenerateActionThread
   agent_studio.envs.desktop_env.agent_interface.EvalTaskThread
   agent_studio.envs.desktop_env.agent_interface.StepActionThread
   agent_studio.envs.desktop_env.agent_interface.AgentInterface




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.agent_interface.config
   agent_studio.envs.desktop_env.agent_interface.logger
   agent_studio.envs.desktop_env.agent_interface.REMOTE_SERVER_ADDR


.. py:data:: config

   

.. py:data:: logger

   

.. py:data:: REMOTE_SERVER_ADDR

   

.. py:class:: FrameBuffer


   .. py:method:: add_frame(frame_id, frame)


   .. py:method:: clear()


   .. py:method:: get_frames(start_frame_id, end_frame_id=None)



.. py:class:: WorkerSignals


   Bases: :py:obj:`PyQt6.QtCore.QObject`

   .. py:attribute:: confirm_signal

      

   .. py:attribute:: decline_signal

      

   .. py:attribute:: start_signal

      

   .. py:attribute:: eval_signal

      

   .. py:attribute:: status_bar_signal

      

   .. py:attribute:: parsed_action_display_signal

      

   .. py:attribute:: response_display_signal

      

   .. py:attribute:: evaluation_display_signal

      

   .. py:attribute:: show_dialog_signal

      

   .. py:attribute:: output_display_signal

      

   .. py:attribute:: save_trajectory_signal

      

   .. py:attribute:: finish_run_task_signal

      

   .. py:attribute:: trajectory_display_signal

      

   .. py:attribute:: generate_action_signal

      

   .. py:attribute:: popup_window_signal

      


.. py:class:: InputDialog(parent=None, message='')


   Bases: :py:obj:`PyQt6.QtWidgets.QDialog`

   .. py:method:: accept()



.. py:class:: ResetRuntimeThread(signals: WorkerSignals)


   Bases: :py:obj:`PyQt6.QtCore.QThread`

   .. py:method:: run()


   .. py:method:: receive_user_input(text: str)
      :abstractmethod:



.. py:class:: ResetTaskThread(agent: agent_studio.agent.base_agent.BaseAgent, signals: WorkerSignals, selected_task: dict)


   Bases: :py:obj:`PyQt6.QtCore.QThread`

   .. py:method:: run()


   .. py:method:: receive_user_input(text: str)



.. py:class:: GenerateActionThread(signals: WorkerSignals, selected_task: dict, obs: numpy.ndarray | None, agent: agent_studio.agent.base_agent.BaseAgent)


   Bases: :py:obj:`PyQt6.QtCore.QThread`

   .. py:method:: run()



.. py:class:: EvalTaskThread(signals: WorkerSignals, trajectory_display: PyQt6.QtWidgets.QTextEdit, selected_task: dict, agent: agent_studio.agent.base_agent.BaseAgent, result_queue: queue.Queue, final_obs: numpy.ndarray | None = None)


   Bases: :py:obj:`PyQt6.QtCore.QThread`

   .. py:method:: run()


   .. py:method:: receive_user_input(text: str)



.. py:class:: StepActionThread(signals: WorkerSignals, trajectory_display: PyQt6.QtWidgets.QTextEdit, parsed_action_display: PyQt6.QtWidgets.QTextEdit, screen_recorder: agent_studio.envs.desktop_env.recorder.screen_recorder.ScreenRecorder | None, current_step_num: int, max_steps: int, agent: agent_studio.agent.base_agent.BaseAgent)


   Bases: :py:obj:`PyQt6.QtCore.QThread`

   .. py:method:: run()

      Steps the next action and adds it to the trajectory.


   .. py:method:: receive_user_input(text: str)
      :abstractmethod:



.. py:class:: AgentInterface(agent: agent_studio.agent.base_agent.BaseAgent, task_configs: list, record_path: str = config.record_path)


   Bases: :py:obj:`PyQt6.QtWidgets.QMainWindow`

   .. py:attribute:: layout_width
      :value: 300

      

   .. py:method:: setup_ui()

      Sets up the UI, including the VNC frame (left) and the right layout.


   .. py:method:: load_task_results()


   .. py:method:: populate_instruction_selection_widget()


   .. py:method:: select_task_instruction(item)


   .. py:method:: set_task_status_bar_text(color: str, text: str) -> None


   .. py:method:: show_input_dialog(message: str)


   .. py:method:: show_choice_dialog(message: str) -> None


   .. py:method:: show_error_popup_dialog(title: str, message: str) -> None

      Shows a popup message.


   .. py:method:: reset()

      Resets the task and waits for the environment to be ready.


   .. py:method:: reconnect()


   .. py:method:: save_trajectory()


   .. py:method:: run_task()


   .. py:method:: generate_action() -> None


   .. py:method:: eval_task()


   .. py:method:: finish_run_task() -> None


   .. py:method:: reject_action() -> None


   .. py:method:: step_action() -> None

      Steps the next action and adds it to the trajectory.


   .. py:method:: interrupt_action()


   .. py:method:: update_screen()


   .. py:method:: render()


   .. py:method:: closeEvent(event)



