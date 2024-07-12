:py:mod:`agent_studio.envs.desktop_env.evaluators.google.docs_evaluator`
========================================================================

.. py:module:: agent_studio.envs.desktop_env.evaluators.google.docs_evaluator


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.google.docs_evaluator.GoogleDocsEvaluator




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.google.docs_evaluator.logger


.. py:data:: logger

   

.. py:class:: GoogleDocsEvaluator(eval_procedure: list[dict], reset_procedure: list[dict])


   Bases: :py:obj:`agent_studio.envs.desktop_env.evaluators.google.evaluator_base.GoogleEvaluatorBase`

   .. py:attribute:: name
      :type: str
      :value: 'google_docs'

      

   .. py:method:: get_document(document_id: str) -> dict

      Gets a document by its ID.


   .. py:method:: get_text_at_index(document, index)

      Gets the text at the given index in the document.


   .. py:method:: replace_text(document_id: str, old_text: str, new_text: str) -> None

      Replaces text in the document.


   .. py:method:: get_document_title(document_id: str) -> str

      Gets the title of the document.


   .. py:method:: delete_text(document_id: str, start_index: int, end_index: int) -> None

      Deletes text in the document.


   .. py:method:: insert_table(document_id: str, rows: int, columns: int, index: int = 1) -> None

      Inserts a table at the given index in the document.


   .. py:method:: search_doc_by_title(title: str) -> list[str]

      Searches for documents with the given title.


   .. py:method:: delete_doc_by_id(doc_id: str) -> None

      Deletes a document by its ID.


   .. py:method:: find_text_format(document, text) -> dict | None

      Finds the formatting of the given text in the document.


   .. py:method:: find_hyperlink(document: dict, search_text: str, expected_url: str) -> bool

      Searches for a hyperlink in the document with the specified text and URL.

      :param document: The document object.
      :type document: dict
      :param search_text: The text of the hyperlink to search for.
      :type search_text: str
      :param expected_url: The expected URL of the hyperlink.
      :type expected_url: str

      :returns: Whether the hyperlink is found and matches the criteria.
      :rtype: bool


   .. py:method:: text_format_match(title: str, text: str, font: str | None = None, size: int | None = None) -> None

      Evaluates if the text matches the specified formatting.


   .. py:method:: hyperlink_match(title: str, text: str, url: str, exists: bool) -> None

      Evaluates if a hyperlink with the specified text and URL exists in the document.

      :param title: The title of the document to search for.
      :type title: str
      :param text: The text of the hyperlink to match.
      :type text: str
      :param url: The URL the hyperlink should point to.
      :type url: str

      :raises FeedbackException: If the hyperlink does not match the expected criteria.


   .. py:method:: check_doc_exists(title: str, exists: bool, content: str | None = None) -> None

      Checks if the document matches the given parameters.

      :param title: Document title.
      :type title: str
      :param exists: Whether the document should exist.
      :type exists: bool
      :param content: Document content.
      :type content: str | None

      :raises FeedbackException: If the document exists does not match the expected value.

      :returns: None


   .. py:method:: create_document(title: str, content: str = '', hyperlink: dict[str, str] | None = None) -> dict

      Creates a document with the given title and content.

      :param title: Document title.
      :type title: str
      :param content: Document content.
      :type content: str

      :returns: Document information.
      :rtype: dict


   .. py:method:: delete_document(title: str, content: str | None = None) -> None

      Deletes a document with the given title and content.

      :param title: Document title.
      :type title: str
      :param content: Document content.
      :type content: str

      :returns: None



