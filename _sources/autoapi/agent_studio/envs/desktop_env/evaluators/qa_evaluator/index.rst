:py:mod:`agent_studio.envs.desktop_env.evaluators.qa_evaluator`
===============================================================

.. py:module:: agent_studio.envs.desktop_env.evaluators.qa_evaluator


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.qa_evaluator.QAEvaluator




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.qa_evaluator.logger
   agent_studio.envs.desktop_env.evaluators.qa_evaluator.config


.. py:data:: logger

   

.. py:data:: config

   

.. py:class:: QAEvaluator(eval_procedure: list[dict[str, dict[str, Any]]], reset_procedure: list[dict[str, dict[str, Any]]])


   Bases: :py:obj:`agent_studio.envs.desktop_env.evaluators.evaluator.Evaluator`

   .. py:attribute:: name
      :type: str
      :value: 'qa'

      

   .. py:method:: string_match(trajectory: list[agent_studio.agent.base_agent.TrajectorySeg], answer: str) -> None



