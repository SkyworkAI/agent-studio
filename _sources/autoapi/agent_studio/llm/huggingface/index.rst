:py:mod:`agent_studio.llm.huggingface`
======================================

.. py:module:: agent_studio.llm.huggingface


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.llm.huggingface.HuggingFaceProvider




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.llm.huggingface.config
   agent_studio.llm.huggingface.logger


.. py:data:: config

   

.. py:data:: logger

   

.. py:class:: HuggingFaceProvider(**kwargs)


   Bases: :py:obj:`agent_studio.llm.base_model.BaseModel`

   .. py:attribute:: name
      :value: 'huggingface'

      

   .. py:method:: compose_messages(intermedia_msg: list[agent_studio.llm.base_model.PromptSeg]) -> Any


   .. py:method:: generate_response(messages: list[agent_studio.llm.base_model.PromptSeg], **kwargs) -> tuple[str, dict[str, Any]]

      Creates a chat completion using the Gemini API.



