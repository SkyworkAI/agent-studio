:py:mod:`agent_studio.envs.desktop_env.evaluators.evaluator`
============================================================

.. py:module:: agent_studio.envs.desktop_env.evaluators.evaluator


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.evaluator.Handler
   agent_studio.envs.desktop_env.evaluators.evaluator.Evaluator



Functions
~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.evaluator.evaluation_handler
   agent_studio.envs.desktop_env.evaluators.evaluator.reset_handler



Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.evaluator.logger


.. py:data:: logger

   

.. py:exception:: FeedbackException(message: str)


   Bases: :py:obj:`Exception`

   Exception to be raised when evaluation failed.


.. py:function:: evaluation_handler(name)


.. py:function:: reset_handler(name)


.. py:class:: Handler(name: str, fun: Callable)



.. py:class:: Evaluator(eval_procedure: list[dict[str, dict[str, Any]]], reset_procedure: list[dict[str, dict[str, Any]]])


   Base class for evaluation.

   .. py:attribute:: name
      :type: str
      :value: 'evaluator'

      

   .. py:attribute:: prompt
      :type: str
      :value: 'system_prompt'

      

   .. py:method:: auto_register_handlers() -> None

      Register a handler for a specific action.


   .. py:method:: reset() -> None

      Reset the environment before task execution.



