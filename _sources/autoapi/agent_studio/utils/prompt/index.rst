:py:mod:`agent_studio.utils.prompt`
===================================

.. py:module:: agent_studio.utils.prompt


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.utils.prompt.PromptSeg
   agent_studio.utils.prompt.PromptTag
   agent_studio.utils.prompt.Prompt
   agent_studio.utils.prompt.SysPromptComposer




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.utils.prompt.logger


.. py:data:: logger

   

.. py:class:: PromptSeg


   .. py:attribute:: role
      :type: str

      

   .. py:attribute:: content
      :type: Union[str, numpy.ndarray, pathlib.Path]

      


.. py:class:: PromptTag


   Bases: :py:obj:`enum.Enum`

   Prompt tags. Defines the type of prompt.

   .. py:attribute:: NONE
      :value: 'none'

      

   .. py:attribute:: SYSTEM
      :value: 'system'

      

   .. py:attribute:: EVALUATOR
      :value: 'evaluator'

      


.. py:class:: Prompt(name: str, prompt: str, tag: PromptTag, params: dict[str, str], parent: str | None = None)


   :param name: The name of the prompt. Here is the file relative path.
   :type name: str
   :param prompt: The prompt string.
   :type prompt: str
   :param tag: Not used.
   :type tag: PromptTag
   :param params: The parameters of the prompt. Defaults to {}.
   :type params: dict[str, str], optional
   :param parent: The parent prompt name. Defaults to None.
   :type parent: str | None, optional

   .. py:method:: list(indent: int = 0) -> str


   .. py:method:: compose(use_tag: bool = False) -> str



.. py:class:: SysPromptComposer(prompt_path_base: str = 'agent_studio/agent/prompts')


   .. py:method:: add(prompt_name: str) -> Prompt

      Add a prompt and all its parents to the composer.


   .. py:method:: list() -> str


   .. py:method:: compose(use_tag: bool = False, dry_run: bool = False) -> str



