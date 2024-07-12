:py:mod:`agent_studio.envs.desktop_env.evaluators.google.gservice`
==================================================================

.. py:module:: agent_studio.envs.desktop_env.evaluators.google.gservice


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.google.gservice.GoogleService




Attributes
~~~~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.google.gservice.config
   agent_studio.envs.desktop_env.evaluators.google.gservice.logger


.. py:data:: config

   

.. py:data:: logger

   

.. py:class:: GoogleService(scopes: list[str], service_name: str, service_version: str, debug: bool = False)


   Bases: :py:obj:`object`

   .. py:method:: authenticate(credential_path: str) -> google.oauth2.credentials.Credentials | None


   .. py:method:: update_token_crediential(credential: dict, token: dict | None) -> google.oauth2.credentials.Credentials | None



