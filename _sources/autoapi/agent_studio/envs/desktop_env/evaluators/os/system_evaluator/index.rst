:py:mod:`agent_studio.envs.desktop_env.evaluators.os.system_evaluator`
======================================================================

.. py:module:: agent_studio.envs.desktop_env.evaluators.os.system_evaluator


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.os.system_evaluator.SystemEvaluator




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.os.system_evaluator.logger


.. py:data:: logger

   

.. py:class:: SystemEvaluator(eval_procedure: list[dict[str, dict[str, Any]]], reset_procedure: list[dict[str, dict[str, Any]]])


   Bases: :py:obj:`agent_studio.envs.desktop_env.evaluators.evaluator.Evaluator`

   Base class for evaluation.

   .. py:attribute:: name
      :type: str
      :value: 'system'

      

   .. py:method:: sleep(seconds: float) -> None


   .. py:method:: sleep_eval(seconds: float) -> None


   .. py:method:: exec(command: str) -> None



