:py:mod:`agent_studio.envs.desktop_env.recorder.base_recorder`
==============================================================

.. py:module:: agent_studio.envs.desktop_env.recorder.base_recorder


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.recorder.base_recorder.MouseOptions
   agent_studio.envs.desktop_env.recorder.base_recorder.MODE
   agent_studio.envs.desktop_env.recorder.base_recorder.Event
   agent_studio.envs.desktop_env.recorder.base_recorder.Recorder




.. py:class:: MouseOptions


   Bases: :py:obj:`enum.Flag`

   Mouse options for the recorder. Log move, click and scroll, respectively.

   .. py:attribute:: LOG_MOVE

      

   .. py:attribute:: LOG_CLICK

      

   .. py:attribute:: LOG_SCROLL

      

   .. py:attribute:: LOG_ALL

      


.. py:class:: MODE


   Bases: :py:obj:`enum.Enum`

   The mode of the recorder. Switched by hotkeys.

   .. py:attribute:: INIT

      

   .. py:attribute:: CODING

      

   .. py:attribute:: TYPING

      


.. py:class:: Event(time: float, event_type: str, data: dict | str | None)



.. py:class:: Recorder


   .. py:method:: reset(**kwargs) -> None
      :abstractmethod:


   .. py:method:: start() -> None
      :abstractmethod:


   .. py:method:: stop() -> None
      :abstractmethod:


   .. py:method:: wait_exit() -> None
      :abstractmethod:


   .. py:method:: remove_incomplete_events(in_func: Callable, out_func: Callable, events: list[Event])
      :staticmethod:



