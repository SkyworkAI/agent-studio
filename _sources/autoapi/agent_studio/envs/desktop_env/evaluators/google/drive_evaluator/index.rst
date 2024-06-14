:py:mod:`agent_studio.envs.desktop_env.evaluators.google.drive_evaluator`
=========================================================================

.. py:module:: agent_studio.envs.desktop_env.evaluators.google.drive_evaluator


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.google.drive_evaluator.GoogleDriveService
   agent_studio.envs.desktop_env.evaluators.google.drive_evaluator.GoogleDriveEvaluator




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.google.drive_evaluator.logger


.. py:data:: logger

   

.. py:class:: GoogleDriveService


   Bases: :py:obj:`agent_studio.envs.desktop_env.evaluators.google.gservice.GoogleService`

   .. py:method:: upload_file(name: str, path: str, mime_type: str, folder_id: str | None = None) -> dict

      Uploads a file to Google Drive.


   .. py:method:: download_file(file_id: str, output_file: str) -> None

      Downloads a file from Google Drive.


   .. py:method:: create_folder(folder_name: str, file_list: list[dict] | None = None) -> dict

      Creates a folder in Google Drive.


   .. py:method:: list_files(folder_id: str | None = None)

      Lists all files in Google Drive.


   .. py:method:: get_filename(file_id: str) -> str

      Gets the file name by ID.


   .. py:method:: rename_file(file_id: str, new_name: str) -> None

      Renames a file in Google Drive.


   .. py:method:: search_file_by_condition(condition: str) -> list[str]

      Searches for a file in Google Drive.


   .. py:method:: search_file(file_name: str) -> list[str]

      Searches for a file by name in Google Drive.


   .. py:method:: search_folder(folder_name)

      Searches for a folder in Google Drive.


   .. py:method:: delete_file_by_id(file_id: str) -> None

      Deletes a file from Google Drive.


   .. py:method:: delete_folder_by_id(folder_id: str) -> None

      Deletes a folder from Google Drive.


   .. py:method:: compare_file_content(file_id: str, content: str) -> bool

      Compares the content of a file in Google Drive with the given content.


   .. py:method:: share_file(file_id: str, user_email: str, role: str = 'reader') -> None

      Shares a file with a user.



.. py:class:: GoogleDriveEvaluator(eval_procedure: list[dict], reset_procedure: list[dict])


   Bases: :py:obj:`agent_studio.envs.desktop_env.evaluators.google.evaluator_base.GoogleEvaluatorBase`

   Base class for evaluation.

   .. py:attribute:: name
      :type: str
      :value: 'google_drive'

      

   .. py:method:: check_file_exists(file_name: str, exists: bool, content: str | None = None) -> None

      Checks if a file exists in Google Drive.


   .. py:method:: check_folder_exists(folder_name: str, exists: bool, file_list: list[dict] | None = None) -> None

      Checks if a folder exists in Google Drive.


   .. py:method:: create_folder(folder_name: str, file_list: list[dict] | None = None) -> None


   .. py:method:: upload_file(name: str, path: str, mime_type: str, folder_id: str | None = None) -> None


   .. py:method:: delete_file(file_name: str) -> None

      Deletes a file from Google Drive with name.


   .. py:method:: delete_folder(folder_name: str) -> None

      Deletes a folder from Google Drive with name.



