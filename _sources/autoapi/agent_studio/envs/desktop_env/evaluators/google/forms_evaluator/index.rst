:py:mod:`agent_studio.envs.desktop_env.evaluators.google.forms_evaluator`
=========================================================================

.. py:module:: agent_studio.envs.desktop_env.evaluators.google.forms_evaluator


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.google.forms_evaluator.GoogleFormsService
   agent_studio.envs.desktop_env.evaluators.google.forms_evaluator.GoogleFormsEvaluator



Functions
~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.google.forms_evaluator.form_match



Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.google.forms_evaluator.config
   agent_studio.envs.desktop_env.evaluators.google.forms_evaluator.logger


.. py:data:: config

   

.. py:data:: logger

   

.. py:function:: form_match(form_to_match: dict[str, Any], ref_form: dict[str, Any]) -> bool

   Checks if the form_to_match matches the ref_form.


.. py:class:: GoogleFormsService


   Bases: :py:obj:`agent_studio.envs.desktop_env.evaluators.google.gservice.GoogleService`

   .. py:method:: create_form(title: str, description: str | None = None) -> dict

      Creates a form with the given title and description.


   .. py:method:: get_form(form_id: str) -> dict

      Gets a form by its ID.


   .. py:method:: add_question(form_id: str, question: dict[str, Any], index: int) -> None


   .. py:method:: search_form_by_title(title: str) -> list[str]

      Searches for forms with the given title.


   .. py:method:: delete_form_by_id(form_id: str) -> None

      Deletes a form by its ID.


   .. py:method:: delete_form(form_info: dict[str, Any]) -> None

      Deletes a form with the given title and description.


   .. py:method:: check_form_exists(form_info: dict[str, Any], exists: bool) -> None

      Checks if the form matches the given parameters.



.. py:class:: GoogleFormsEvaluator(eval_procedure: list[dict], reset_procedure: list[dict])


   Bases: :py:obj:`agent_studio.envs.desktop_env.evaluators.google.evaluator_base.GoogleEvaluatorBase`

   Base class for evaluation.

   .. py:attribute:: name
      :type: str
      :value: 'google_forms'

      

   .. py:method:: check_form_exists(form_info: dict[str, Any], exists: bool) -> None


   .. py:method:: create_form(title: str, description: str | None = None) -> None


   .. py:method:: delete_form(form_info: dict[str, Any]) -> None



