:py:mod:`agent_studio.envs.desktop_env.evaluators.google.slides_evaluator`
==========================================================================

.. py:module:: agent_studio.envs.desktop_env.evaluators.google.slides_evaluator


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.google.slides_evaluator.GoogleSlidesEvaluator




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.google.slides_evaluator.logger


.. py:data:: logger

   

.. py:class:: GoogleSlidesEvaluator(eval_procedure: list[dict], reset_procedure: list[dict])


   Bases: :py:obj:`agent_studio.envs.desktop_env.evaluators.google.evaluator_base.GoogleEvaluatorBase`

   Base class for evaluation.

   .. py:attribute:: name
      :type: str
      :value: 'google_slides'

      

   .. py:method:: get_presentation(presentation_id: str) -> dict

      Gets the Google Slides presentation by its ID.


   .. py:method:: get_presentation_title(presentation_id: str) -> str

      Gets the title of the Google Slides presentation.


   .. py:method:: add_slide(presentation_id: str, page_id: str | None = None) -> None

      Adds a new slide to the Google Slides presentation.


   .. py:method:: create_textbox(presentation_id: str, slide_id: str, x: int, y: int, width: int, height: int) -> str | None

      Creates a textbox on the Google Slides presentation.


   .. py:method:: add_text_to_slide(presentation_id: str, page_id: str, text: str) -> None

      Adds text to the Google Slides presentation.


   .. py:method:: replace_text_in_slide(presentation_id: str, old_text: str, new_text: str, match_case: bool = True) -> None

      Replaces text in the Google Slides presentation.


   .. py:method:: get_slide_ids(presentation_id: str) -> list

      Gets the IDs of the slides in the Google Slides presentation.


   .. py:method:: get_slide_titles(presentation_id: str) -> list

      Gets the titles of the slides in the Google Slides presentation.


   .. py:method:: delete_slide(presentation_id: str, page_id: str) -> None

      Deletes a slide from the Google Slides presentation.


   .. py:method:: search_presentation_by_title(title: str) -> list[str]

      Searches for Google Slides presentations with the given title.


   .. py:method:: delete_presentation_by_id(presentation_id: str) -> None

      Deletes the Google Slides presentation with the given ID.


   .. py:method:: check_presentation_exists(title: str, exists: bool, content: str | None = None) -> None

      Checks if the presentation matches the given parameters.


   .. py:method:: create_presentation(title: str) -> None

      Creates a Google Slides presentation with the given title.


   .. py:method:: delete_presentation(title: str, content: str | None = None) -> None

      Removes duplicate Google Slides presentations based on their content.



