:py:mod:`agent_studio.utils.task_status`
========================================

.. py:module:: agent_studio.utils.task_status


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.utils.task_status.StateEnum
   agent_studio.utils.task_status.StateInfo
   agent_studio.utils.task_status.TaskStatus




.. py:class:: StateEnum


   Bases: :py:obj:`enum.Enum`

   Generic enumeration.

   Derive from this class to define new enumerations.

   .. py:attribute:: IN_PROGRESS
      :value: 'in_progress'

      

   .. py:attribute:: WAIT_FOR_INPUT
      :value: 'wait_for_input'

      

   .. py:attribute:: FINISHED
      :value: 'finished'

      

   .. py:attribute:: TERMINATE
      :value: 'terminate'

      


.. py:class:: StateInfo(state: StateEnum, message: str | dict = '', result: str = '')



.. py:class:: TaskStatus


   .. py:method:: set_task_state(state_info: StateInfo) -> None


   .. py:method:: get_task_state() -> StateInfo


   .. py:method:: reset_state() -> None


   .. py:method:: wait_for_state_change(cur_state: StateEnum) -> StateInfo

      Return when the state is different from the current state



