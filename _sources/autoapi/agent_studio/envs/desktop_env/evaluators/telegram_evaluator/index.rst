:py:mod:`agent_studio.envs.desktop_env.evaluators.telegram_evaluator`
=====================================================================

.. py:module:: agent_studio.envs.desktop_env.evaluators.telegram_evaluator


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.telegram_evaluator.TelegramService
   agent_studio.envs.desktop_env.evaluators.telegram_evaluator.TelegramEvaluator




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.telegram_evaluator.logger
   agent_studio.envs.desktop_env.evaluators.telegram_evaluator.config


.. py:data:: logger

   

.. py:data:: config

   

.. py:class:: TelegramService


   .. py:method:: message_match(chat_id: int | str, ref_messages: list[dict]) -> None


   .. py:method:: delete_recent_messages(chat_id: str | int, n: int) -> None


   .. py:method:: send_messages(chat_id: str | int, messages: list[str], replyto_offset: int | None = None)


   .. py:method:: send_document(chat_id: str | int, file_path: str, caption: str, replyto_offset: int | None = None)



.. py:class:: TelegramEvaluator(eval_procedure: list[dict], reset_procedure: list[dict])


   Bases: :py:obj:`agent_studio.envs.desktop_env.evaluators.evaluator.Evaluator`

   Base class for evaluation.

   .. py:attribute:: name
      :type: str
      :value: 'telegram'

      

   .. py:method:: message_match(chat_id: str | int, ref_messages: list[dict]) -> None

      Check if the messages in the chat match the reference messages.

      :param chat_id: Chat id.
      :type chat_id: str | int
      :param ref_messages: List of reference messages.
                           Each reference message is a dictionary with the following keys:

                           - type (str): Type of the message.                     valid values are 'text', 'document'.
                           - compare_method (str): Method to compare the message.                     Supported methods is 'exact'.
                           - value (str): Value to compare with the message.                     Only used when compare_method is 'exact'.
                           - file_path (str, optional): Path to the file.                     Only used when type is 'document'.
                           - caption (str, optional): Caption of the file.                     Only used when type is 'document'.
                           - replyto (dict, optional): Reference message to reply to.                     Required keys are the same as the ref_messages                     (for recursive matching).
      :type ref_messages: list[dict]

      :raises FeedbackException: If the messages do not match.

      :returns: None

      Example::

          ref_messages = [
              {
                  "type": "text",
                  "compare_method": "exact",
                  "value": "Welcome to the agent_studio!",
              },
              {
                  "type": "document",
                  "file_path": "data/test/telegram/GitHub-logo.png",
                  "caption": "GitHub logo.",
                  "replyto": {
                      "type": "text",
                      "compare_method": "exact",
                      "value": "hi",
                  }
              }
          ]


   .. py:method:: send_messages(chat_id: str | int, messages: list[str])

      Send a message to specific chat.

      :param chat_id: Chat id.
      :type chat_id: str | int
      :param messages: List of messages to be sent.
                       messages are in the order of sending.
      :type messages: list[str]

      :returns: None


   .. py:method:: delete_recent_messages(chat_id: str | int, n: int)

      Delete recent messages from specific chat.

      :param chat_id: Chat id.
      :type chat_id: str | int
      :param n: Number of messages to be deleted.
      :type n: int

      :returns: None


   .. py:method:: send_document(chat_id: str | int, file_path: str, caption: str = '', replyto_offset: int | None = None)

      Send a document to specific chat.

      :param chat_id: Chat id.
      :type chat_id: str | int
      :param file_path: Path to the document.
      :type file_path: str
      :param caption: Caption of the document. Defaults to "".
      :type caption: str, optional
      :param replyto_offset: Offset of the message to reply to.                 Defaults to None. The offset is counted from the last message.                 E.g. 0 means reply to the last message,                 1 means reply to the second last message, etc.
      :type replyto_offset: int, optional

      :returns: None



