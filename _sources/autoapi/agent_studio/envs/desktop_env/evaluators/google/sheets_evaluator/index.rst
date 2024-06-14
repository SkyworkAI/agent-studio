:py:mod:`agent_studio.envs.desktop_env.evaluators.google.sheets_evaluator`
==========================================================================

.. py:module:: agent_studio.envs.desktop_env.evaluators.google.sheets_evaluator


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.google.sheets_evaluator.GoogleSheetsService
   agent_studio.envs.desktop_env.evaluators.google.sheets_evaluator.GoogleSheetsEvaluator




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.google.sheets_evaluator.logger


.. py:data:: logger

   

.. py:class:: GoogleSheetsService


   Bases: :py:obj:`agent_studio.envs.desktop_env.evaluators.google.gservice.GoogleService`

   .. py:method:: create_spreadsheet(title: str) -> dict

      Creates a Google Sheets spreadsheet with the given title.


   .. py:method:: get_spreadsheet(spreadsheet_id: str) -> dict

      Gets the Google Sheets spreadsheet by its ID.


   .. py:method:: get_spreadsheet_title(spreadsheet_id: str) -> str

      Gets the title of the Google Sheets spreadsheet.


   .. py:method:: read_range(spreadsheet_id: str, range_name: str) -> list

      Reads values from the Google Sheets spreadsheet.


   .. py:method:: write_range(spreadsheet_id: str, range_name: str, values: list) -> None

      Writes values to the Google Sheets spreadsheet.


   .. py:method:: append_values(spreadsheet_id: str, range_name: str, values: list) -> None

      Appends values to the Google Sheets spreadsheet.


   .. py:method:: clear_range(spreadsheet_id: str, range_name: str) -> None

      Clears the range in the Google Sheets spreadsheet.


   .. py:method:: search_spreadsheet_by_title(title: str) -> list[str]

      Searches for Google Sheets spreadsheets with the given title.


   .. py:method:: delete_spreadsheet(title: str, content: str | None = None) -> None

      Removes duplicate Google Sheets spreadsheets based on their content.


   .. py:method:: delete_spreadsheet_by_id(spreadsheet_id: str) -> None

      Deletes the Google Sheets spreadsheet with the given ID.


   .. py:method:: check_spreadsheet_exists(title: str, exists: bool, content: str | None = None) -> None

      Checks if the spreadsheet matches the given parameters.



.. py:class:: GoogleSheetsEvaluator(eval_procedure: list[dict], reset_procedure: list[dict])


   Bases: :py:obj:`agent_studio.envs.desktop_env.evaluators.google.evaluator_base.GoogleEvaluatorBase`

   Base class for evaluation.

   .. py:attribute:: name
      :type: str
      :value: 'google_sheets'

      

   .. py:method:: check_spreadsheet_exists(title: str, exists: bool, content: str | None = None) -> None


   .. py:method:: create_spreadsheet(title: str) -> None


   .. py:method:: delete_spreadsheet(title: str, content: str | None = None) -> None



