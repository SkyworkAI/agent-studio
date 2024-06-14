:py:mod:`agent_studio.agent.base_agent`
=======================================

.. py:module:: agent_studio.agent.base_agent


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.agent.base_agent.BaseAgent




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.agent.base_agent.config
   agent_studio.agent.base_agent.logger


.. py:data:: config

   

.. py:data:: logger

   

.. py:class:: BaseAgent(model: agent_studio.llm.base_model.BaseModel)


   Base class for agents.

   .. py:attribute:: name
      :type: str
      :value: 'base'

      

   .. py:method:: reset(task_config: dict[str, Any], registered_evaluators: dict[str, type[agent_studio.envs.desktop_env.evaluators.evaluator_helper.Evaluator]]) -> None


   .. py:method:: get_token_count() -> int


   .. py:method:: generate_action(obs: numpy.ndarray | None) -> tuple[str, str]


   .. py:method:: step_action(confirmed: bool, **kwargs) -> tuple[dict, bool]

      Executes the code and record the result.


   .. py:method:: eval(final_obs: numpy.ndarray | None = None) -> dict[str, Any]
      :abstractmethod:


   .. py:method:: close() -> None


   .. py:method:: trajectory2intermediate_msg() -> list[agent_studio.llm.base_model.PromptSeg]
      :abstractmethod:



