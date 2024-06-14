:py:mod:`agent_studio.envs.desktop_env.evaluators.evaluator_helper`
===================================================================

.. py:module:: agent_studio.envs.desktop_env.evaluators.evaluator_helper


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.evaluator_helper.EvaluatorComb



Functions
~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.evaluator_helper.register_evaluators
   agent_studio.envs.desktop_env.evaluators.evaluator_helper.evaluator_router



Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.evaluator_helper.config
   agent_studio.envs.desktop_env.evaluators.evaluator_helper.logger


.. py:data:: config

   

.. py:data:: logger

   

.. py:class:: EvaluatorComb(evaluators: list[agent_studio.envs.desktop_env.evaluators.evaluator.Evaluator])


   .. py:method:: reset() -> None



.. py:function:: register_evaluators(base_path: str | pathlib.Path = 'agent_studio/envs/desktop_env/evaluators') -> dict[str, type[agent_studio.envs.desktop_env.evaluators.evaluator.Evaluator]]


.. py:function:: evaluator_router(task_configs: dict) -> EvaluatorComb

   Router to get the evaluator class


