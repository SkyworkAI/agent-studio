:py:mod:`agent_studio.envs.desktop_env.evaluators.os.process_evaluator`
=======================================================================

.. py:module:: agent_studio.envs.desktop_env.evaluators.os.process_evaluator


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.os.process_evaluator.ProcessEvaluator



Functions
~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.os.process_evaluator.find_procs_by_name



Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.os.process_evaluator.logger


.. py:data:: logger

   

.. py:function:: find_procs_by_name(name: str) -> list[psutil.Process]


.. py:class:: ProcessEvaluator(eval_procedure: list[dict[str, dict[str, Any]]], reset_procedure: list[dict[str, dict[str, Any]]])


   Bases: :py:obj:`agent_studio.envs.desktop_env.evaluators.evaluator.Evaluator`

   Base class for evaluation.

   .. py:attribute:: name
      :type: str
      :value: 'process'

      

   .. py:method:: match_process(name: str) -> None

      Check if a process with the given name is running.                 Can be a regex pattern.

      :param name: Name of the process to check.
      :type name: str

      :raises FeedbackException: If the process is not found.


   .. py:method:: create_process(cmd: list[str], wait_for: str | None) -> None

      Create a process with the given command.

      :param cmd: Command to create the process.
      :type cmd: list[str]
      :param wait_for: Name of the process to wait for.                 Can be a regex pattern.                 If None, the function will not wait for any process.
      :type wait_for: str | None

      :raises FeedbackException: If the process creation fails.


   .. py:method:: pkill_by_name(name: str) -> None

      Kill all processes with the given name.

      :param name: Name pattern of the process to kill.                 Can be a regex pattern.
      :type name: str



