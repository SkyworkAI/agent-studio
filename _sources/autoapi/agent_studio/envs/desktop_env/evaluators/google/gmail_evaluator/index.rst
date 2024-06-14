:py:mod:`agent_studio.envs.desktop_env.evaluators.google.gmail_evaluator`
=========================================================================

.. py:module:: agent_studio.envs.desktop_env.evaluators.google.gmail_evaluator


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.google.gmail_evaluator.GmailEvaluator



Functions
~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.google.gmail_evaluator.extract_email
   agent_studio.envs.desktop_env.evaluators.google.gmail_evaluator.message_match
   agent_studio.envs.desktop_env.evaluators.google.gmail_evaluator.get_attachment_name
   agent_studio.envs.desktop_env.evaluators.google.gmail_evaluator.get_body
   agent_studio.envs.desktop_env.evaluators.google.gmail_evaluator.get_message_from_raw



Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.google.gmail_evaluator.config
   agent_studio.envs.desktop_env.evaluators.google.gmail_evaluator.logger


.. py:data:: config

   

.. py:data:: logger

   

.. py:function:: extract_email(s)

   Extracts the first email address from the given string.


.. py:function:: message_match(msg_to_match: dict[str, Any], ref_msg: dict[str, Any]) -> bool

   Checks if the msg_to_match matches the ref_msg.


.. py:function:: get_attachment_name(raw_message: dict[str, Any]) -> str | None

   Retrieves the name of the attachment, if any.


.. py:function:: get_body(raw_message: dict[str, Any]) -> str

   Decodes the body of the message.


.. py:function:: get_message_from_raw(raw_message: dict[str, Any]) -> dict[str, Any]


.. py:class:: GmailEvaluator(eval_procedure: list[dict], reset_procedure: list[dict])


   Bases: :py:obj:`agent_studio.envs.desktop_env.evaluators.google.evaluator_base.GoogleEvaluatorBase`

   Base class for evaluation.

   .. py:attribute:: name
      :type: str
      :value: 'gmail'

      

   .. py:method:: check_draft_exists(draft_info: dict[str, Any], exists: bool) -> None

      Checks if the given draft exists.


   .. py:method:: check_sent_message_exists(message_info: dict[str, Any], exists: bool) -> None

      Checks if the given sent message exists.


   .. py:method:: is_email_marked_important(message_info: dict[str, Any], gt: bool)

      Checks if the email with the given ID is marked as important.


   .. py:method:: check_label_exists(label_name: str, exists: bool)

      Checks if a label exists by name.


   .. py:method:: email_has_label(message_info: dict[str, Any], label_name: str, gt: bool)


   .. py:method:: delete_label(label_name: str) -> None


   .. py:method:: create_label(label_name: str, label_list_visibility: str = 'labelShow', message_list_visibility: str = 'show') -> None


   .. py:method:: is_email_in_trash(message_info: dict[str, Any], in_trash: bool)

      Checks if the email with the given ID exists in trash.


   .. py:method:: create_draft(draft_info: dict[str, Any]) -> None

      Creates a draft email message in the user's mailbox.


   .. py:method:: delete_draft(draft_info: dict[str, Any]) -> None

      Deletes the draft that matches the given criteria.


   .. py:method:: add_email_to_trash(message_info: dict[str, Any]) -> None

      Moves an email to the trash.


   .. py:method:: delete_sent_message(message_info: dict[str, Any]) -> None

      Deletes the sent message with the given criteria.


   .. py:method:: send_message(message_info: dict[str, Any]) -> None

      Creates and sends an email message.


   .. py:method:: mark_message_important(is_important: bool, subject_contains: str) -> None

      Marks the email with the given subject as important.


   .. py:method:: get_message(message_id: str) -> dict[str, Any]

      Retrieves the full message using the message ID.


   .. py:method:: search_messages(message_info: dict[str, Any], message_type: str) -> list[dict[str, Any]]

      Searches the messages that match the given criteria.


   .. py:method:: delete_draft_by_id(draft_id: str) -> None

      Deletes the draft with the given ID.


   .. py:method:: delete_sent_message_by_id(message_id: str) -> None

      Deletes the sent message with the given ID.



