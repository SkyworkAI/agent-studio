:py:mod:`agent_studio.utils.communication`
==========================================

.. py:module:: agent_studio.utils.communication


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.utils.communication.AgentStudioStatusResponse
   agent_studio.utils.communication.AgentStudioTextRequest
   agent_studio.utils.communication.AgentStudioResetRequest
   agent_studio.utils.communication.AgentStudioEvalRequest




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.utils.communication.bytes2str
   agent_studio.utils.communication.str2bytes


.. py:data:: bytes2str
   :type: Callable[Ellipsis, str]

   

.. py:data:: str2bytes
   :type: Callable[Ellipsis, Any]

   

.. py:class:: AgentStudioStatusResponse


   Bases: :py:obj:`pydantic.BaseModel`

   .. py:attribute:: status
      :type: str

      

   .. py:attribute:: content
      :type: str
      :value: ''

      

   .. py:attribute:: message
      :type: dict | str
      :value: ''

      


.. py:class:: AgentStudioTextRequest


   Bases: :py:obj:`pydantic.BaseModel`

   .. py:attribute:: message
      :type: str

      


.. py:class:: AgentStudioResetRequest


   Bases: :py:obj:`pydantic.BaseModel`

   .. py:attribute:: task_config
      :type: dict

      


.. py:class:: AgentStudioEvalRequest


   Bases: :py:obj:`pydantic.BaseModel`

   .. py:attribute:: task_config
      :type: dict

      

   .. py:attribute:: trajectory
      :type: str

      


