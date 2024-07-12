:py:mod:`agent_studio.envs.desktop_env.evaluators.os.filesystem_evaluator`
==========================================================================

.. py:module:: agent_studio.envs.desktop_env.evaluators.os.filesystem_evaluator


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.os.filesystem_evaluator.FilesystemEvaluator




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.os.filesystem_evaluator.logger


.. py:data:: logger

   

.. py:class:: FilesystemEvaluator(eval_procedure: list[dict], reset_procedure: list[dict])


   Bases: :py:obj:`agent_studio.envs.desktop_env.evaluators.evaluator.Evaluator`

   Base class for evaluation.

   .. py:attribute:: name
      :type: str
      :value: 'filesystem'

      

   .. py:method:: exists(file_to_check: dict[str, bool]) -> None
      :staticmethod:


   .. py:method:: type_check(file_to_check: dict[str, str]) -> None
      :staticmethod:


   .. py:method:: permissions_check(file_to_check: dict[str, str]) -> None
      :staticmethod:


   .. py:method:: content_check(file_to_check: dict[str, str], method: str = 'exact') -> None
      :staticmethod:


   .. py:method:: metadata_check(file_to_check: dict[str, dict]) -> None
      :staticmethod:

      Check file metadata.

      :param file_to_check: dict[str, dict]:
                            Dictionary with file path as key and metadata as value.
                            Metadata is a dictionary with keys:
                            last_modified, creation_time, size, owner, group.
                            last_modified and creation_time are in ISO format.
                            size is in bytes.
                            owner and group are strings.

      :raises FeedbackException: If metadata doesn't match expected values.

      Example::

          file_to_check = {
              "tmp/test.txt": {
                  "last_modified": "2021-09-01T12:00:00",
                  "creation_time": "2021-09-01T12:00:00",
                  "size": 1000,
                  "owner": "user",
                  "group": "group"
              }


   .. py:method:: verify_ini(target_path: str, ref_path: str) -> None
      :staticmethod:

      Compare two ini files.

      :param target_path: str: Path to the target ini file.
      :param ref_path: str: Path to the reference ini file.

      :raises FeedbackException: If the files don't match.


   .. py:method:: match_file(file_to_check: dict[str, str]) -> None
      :staticmethod:


   .. py:method:: create_file(path: str, content: str | None = None) -> None
      :staticmethod:


   .. py:method:: create_directory(path: str)


   .. py:method:: mkdir(path: str) -> None
      :staticmethod:


   .. py:method:: rm(path: str) -> None
      :staticmethod:


   .. py:method:: rmdir(path: str) -> None
      :staticmethod:


   .. py:method:: rename(old_name: str, new_name: str) -> None
      :staticmethod:


   .. py:method:: copy(src: str, dest: str) -> None
      :staticmethod:


   .. py:method:: move(src: str, dest: str) -> None
      :staticmethod:


   .. py:method:: chmod(path: str, mode: str) -> None
      :staticmethod:



