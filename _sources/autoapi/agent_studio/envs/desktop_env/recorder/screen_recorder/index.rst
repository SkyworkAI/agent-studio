:py:mod:`agent_studio.envs.desktop_env.recorder.screen_recorder`
================================================================

.. py:module:: agent_studio.envs.desktop_env.recorder.screen_recorder


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.recorder.screen_recorder.FrameBuffer
   agent_studio.envs.desktop_env.recorder.screen_recorder.WindowManagerDummy
   agent_studio.envs.desktop_env.recorder.screen_recorder.LinuxWindowManager
   agent_studio.envs.desktop_env.recorder.screen_recorder.DarwinWindowManager
   agent_studio.envs.desktop_env.recorder.screen_recorder.WindowsWindowManager
   agent_studio.envs.desktop_env.recorder.screen_recorder.ScreenRecorder
   agent_studio.envs.desktop_env.recorder.screen_recorder.VNCRecorder




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.recorder.screen_recorder.PROCESS_PER_MONITOR_DPI_AWARE
   agent_studio.envs.desktop_env.recorder.screen_recorder.logger
   agent_studio.envs.desktop_env.recorder.screen_recorder.config


.. py:data:: PROCESS_PER_MONITOR_DPI_AWARE
   :value: 2

   

.. py:data:: logger

   

.. py:data:: config

   

.. py:class:: FrameBuffer


   .. py:method:: add_frame(frame_id, frame)


   .. py:method:: clear()


   .. py:method:: get_frames(start_frame_id, end_frame_id=None)



.. py:class:: WindowManagerDummy


   .. py:method:: send_to_background() -> None


   .. py:method:: bring_to_front() -> None



.. py:class:: LinuxWindowManager


   Bases: :py:obj:`WindowManagerDummy`

   .. py:method:: send_to_background() -> None


   .. py:method:: bring_to_front() -> None



.. py:class:: DarwinWindowManager


   Bases: :py:obj:`WindowManagerDummy`

   .. py:method:: send_to_background() -> None


   .. py:method:: bring_to_front() -> None



.. py:class:: WindowsWindowManager


   Bases: :py:obj:`WindowManagerDummy`

   .. py:method:: send_to_background() -> None


   .. py:method:: bring_to_front() -> None



.. py:class:: ScreenRecorder(fps: int)


   Bases: :py:obj:`agent_studio.envs.desktop_env.recorder.base_recorder.Recorder`

   .. py:method:: reset(**kwargs) -> None


   .. py:method:: start() -> None


   .. py:method:: stop() -> None


   .. py:method:: pause() -> None


   .. py:method:: resume() -> None


   .. py:method:: wait_exit() -> None


   .. py:method:: save(video_path: str, start_frame_id: int, end_frame_id: int | None = None) -> dict


   .. py:method:: get_current_frame() -> numpy.ndarray



.. py:class:: VNCRecorder(vnc_streamer: agent_studio.envs.desktop_env.vnc_client.VNCStreamer, **args)


   Bases: :py:obj:`ScreenRecorder`


