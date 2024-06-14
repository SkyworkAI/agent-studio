:py:mod:`agent_studio.llm.utils`
================================

.. py:module:: agent_studio.llm.utils


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   agent_studio.llm.utils.extract_from_response
   agent_studio.llm.utils.openai_encode_image
   agent_studio.llm.utils.anthropic_encode_image
   agent_studio.llm.utils.decode_image



.. py:function:: extract_from_response(response: str, backtick='```') -> str


.. py:function:: openai_encode_image(image: pathlib.Path | PIL.Image.Image | numpy.ndarray) -> str


.. py:function:: anthropic_encode_image(image: pathlib.Path | PIL.Image.Image | numpy.ndarray) -> str


.. py:function:: decode_image(encoded_image: str) -> PIL.Image.Image


