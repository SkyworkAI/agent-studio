:py:mod:`agent_studio.envs.desktop_env.evaluators.human_evaluator`
==================================================================

.. py:module:: agent_studio.envs.desktop_env.evaluators.human_evaluator


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.human_evaluator.HumanEvaluator




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.human_evaluator.logger
   agent_studio.envs.desktop_env.evaluators.human_evaluator.task_status
   agent_studio.envs.desktop_env.evaluators.human_evaluator.config


.. py:data:: logger

   

.. py:data:: task_status

   

.. py:data:: config

   

.. py:class:: HumanEvaluator(eval_procedure: list[dict[str, dict[str, Any]]], reset_procedure: list[dict[str, dict[str, Any]]])


   Bases: :py:obj:`agent_studio.envs.desktop_env.evaluators.evaluator.Evaluator`

   Base class for evaluation.

   .. py:attribute:: name
      :type: str
      :value: 'human'

      

   .. py:method:: handle_human_evaluation(prompt: str = 'Is the task successful?') -> None

      Human evaluation handler.



