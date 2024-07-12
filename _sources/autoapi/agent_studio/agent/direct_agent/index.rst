:py:mod:`agent_studio.agent.direct_agent`
=========================================

.. py:module:: agent_studio.agent.direct_agent


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.agent.direct_agent.DirectAgent




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.agent.direct_agent.config
   agent_studio.agent.direct_agent.logger


.. py:data:: config

   

.. py:data:: logger

   

.. py:class:: DirectAgent


   Bases: :py:obj:`agent_studio.agent.base_agent.BaseAgent`

   Zero-shot LLM agents.

   .. py:attribute:: name
      :type: str
      :value: 'direct'

      

   .. py:method:: reset(task_config: dict[str, Any], registered_evaluators: dict[str, type[agent_studio.envs.desktop_env.evaluators.evaluator_helper.Evaluator]]) -> None


   .. py:method:: trajectory2intermediate_msg() -> list[agent_studio.utils.prompt.PromptSeg]

      Converts the trajectory to intermediate messages.

      :returns:

                The intermediate messages.
                    + role:
                        - system
                        - user
                        - assistant
                    + content: The content of the message.                    content can either be a string or a np.array.                    If it is a np.array, it should be in RGB format.
      :rtype: list[PromptSeg]


   .. py:method:: eval(final_obs: numpy.ndarray | None = None) -> dict[str, Any]



