:py:mod:`agent_studio.llm.base_model`
=====================================

.. py:module:: agent_studio.llm.base_model


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.llm.base_model.TrajectorySeg
   agent_studio.llm.base_model.BaseModel




.. py:class:: TrajectorySeg


   .. py:attribute:: obs
      :type: numpy.ndarray | None

      

   .. py:attribute:: prompt
      :type: list[agent_studio.utils.prompt.PromptSeg]

      

   .. py:attribute:: response
      :type: str | None

      

   .. py:attribute:: info
      :type: dict[str, Any]

      

   .. py:attribute:: act
      :type: str

      

   .. py:attribute:: res
      :type: dict[str, Any]

      

   .. py:attribute:: timestamp
      :type: float

      

   .. py:attribute:: annotation
      :type: dict[str, Any] | None

      


.. py:class:: BaseModel


   Base class for models.

   .. py:attribute:: name
      :type: str
      :value: 'base'

      

   .. py:method:: compose_messages(intermediate_msg: list[agent_studio.utils.prompt.PromptSeg]) -> Any
      :abstractmethod:


   .. py:method:: generate_response(messages: list[agent_studio.utils.prompt.PromptSeg], **kwargs) -> tuple[str, dict[str, Any]]
      :abstractmethod:

      Generate a response given messages.



