:py:mod:`agent_studio.llm.claude`
=================================

.. py:module:: agent_studio.llm.claude


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.llm.claude.AnthropicProvider




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.llm.claude.config
   agent_studio.llm.claude.logger


.. py:data:: config

   

.. py:data:: logger

   

.. py:class:: AnthropicProvider(**kwargs: Any)


   Bases: :py:obj:`agent_studio.llm.base_model.BaseModel`

   Base class for models.

   .. py:attribute:: name
      :value: 'claude'

      

   .. py:method:: compose_messages(intermedia_msg: list[agent_studio.llm.base_model.PromptSeg]) -> list[dict[str, Any]]

      Composes the messages to be sent to the model.


   .. py:method:: generate_response(messages: list[agent_studio.llm.base_model.PromptSeg], **kwargs) -> tuple[str, dict[str, Any]]

      Creates a chat completion using the Anthropic API.



