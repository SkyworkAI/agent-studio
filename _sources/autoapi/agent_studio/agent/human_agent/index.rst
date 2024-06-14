:py:mod:`agent_studio.agent.human_agent`
========================================

.. py:module:: agent_studio.agent.human_agent


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.agent.human_agent.HumanAgent




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.agent.human_agent.config
   agent_studio.agent.human_agent.logger


.. py:data:: config

   

.. py:data:: logger

   

.. py:class:: HumanAgent


   Bases: :py:obj:`agent_studio.agent.base_agent.BaseAgent`

   Human agents for Human-recorder

   .. py:attribute:: name
      :value: 'human'

      

   .. py:method:: reset(task_config: dict[str, Any], registered_evaluators: dict[str, Any]) -> None


   .. py:method:: step_action(confirmed: bool, **kwargs) -> tuple[dict, bool]

      Executes the code and record the result.

      :param confirmed: Whether the action is confirmed by the human.
      :type confirmed: bool
      :param obs: The observation of the environment.                 For example, the screenshot.
      :type obs: np.ndarray | None
      :param code: The code to execute.
      :type code: str
      :param annotation: The annotation of the action. For bounding box, etc.
      :type annotation: dict

      :returns: The result of the execution and whether the task is done.
      :rtype: tuple[dict, bool]


   .. py:method:: generate_action(obs: numpy.ndarray | None) -> tuple[str, str]
      :abstractmethod:

      This function shouldn't be called by human agents.


   .. py:method:: trajectory2intermediate_msg() -> list[dict[str, Any]]
      :abstractmethod:

      This function shouldn't be called by human agents.


   .. py:method:: eval(final_obs: numpy.ndarray | None = None) -> dict[str, Any]
      :abstractmethod:

      This function shouldn't be called by human agents.



