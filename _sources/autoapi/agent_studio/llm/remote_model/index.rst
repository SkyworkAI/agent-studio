:py:mod:`agent_studio.llm.remote_model`
=======================================

.. py:module:: agent_studio.llm.remote_model


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.llm.remote_model.RemoteProvider




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.llm.remote_model.config
   agent_studio.llm.remote_model.logger


.. py:data:: config

   

.. py:data:: logger

   

.. py:class:: RemoteProvider(**kwargs)


   Bases: :py:obj:`agent_studio.llm.base_model.BaseModel`

   Base class for models.

   .. py:attribute:: name
      :value: 'remote'

      

   .. py:method:: generate_response(messages: list[dict[str, Any]], **kwargs) -> tuple[str, dict[str, Any]]

      Creates a chat completion using the Gemini API.



