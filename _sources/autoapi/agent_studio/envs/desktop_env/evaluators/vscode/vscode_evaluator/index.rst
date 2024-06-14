:py:mod:`agent_studio.envs.desktop_env.evaluators.vscode.vscode_evaluator`
==========================================================================

.. py:module:: agent_studio.envs.desktop_env.evaluators.vscode.vscode_evaluator


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.vscode.vscode_evaluator.VSCodeEvaluator




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.vscode.vscode_evaluator.config
   agent_studio.envs.desktop_env.evaluators.vscode.vscode_evaluator.logger


.. py:data:: config

   

.. py:data:: logger

   

.. py:class:: VSCodeEvaluator(eval_procedure: list[dict], reset_procedure: list[dict])


   Bases: :py:obj:`agent_studio.envs.desktop_env.evaluators.evaluator.Evaluator`

   Base class for evaluation.

   .. py:attribute:: name
      :type: str
      :value: 'vscode'

      

   .. py:method:: install_extension(extension_id: str) -> None


   .. py:method:: uninstall_extension(extension_id: str) -> None


   .. py:method:: uninstall_all_extensions() -> None


   .. py:method:: extension_installed(extension_id: str, exists: bool, version: str | None = None, published_before: str | None = None, published_after: str | None = None) -> None


   .. py:method:: match_installed_extension(extension_id: str, exists: bool, version: str | None = None, published_before: str | None = None, published_after: str | None = None) -> float



