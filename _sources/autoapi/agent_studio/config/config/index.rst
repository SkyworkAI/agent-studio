:py:mod:`agent_studio.config.config`
====================================

.. py:module:: agent_studio.config.config


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.config.config.Config




.. py:class:: Config


   Singleton for config.

   .. py:attribute:: seed
      :type: int
      :value: 42

      

   .. py:attribute:: headless
      :type: bool
      :value: False

      

   .. py:attribute:: python_timeout
      :type: int
      :value: 20

      

   .. py:attribute:: need_human_confirmation
      :type: bool
      :value: False

      

   .. py:attribute:: minimal_action_interval
      :type: float
      :value: 3.0

      

   .. py:attribute:: task_config_paths
      :type: dict

      

   .. py:attribute:: api_key_path
      :type: str
      :value: 'agent_studio/config/api_key.json'

      

   .. py:attribute:: stop_code
      :type: str
      :value: 'exit()'

      

   .. py:attribute:: remote
      :type: bool
      :value: True

      

   .. py:attribute:: env_type
      :type: str
      :value: 'desktop'

      

   .. py:attribute:: env_server_addr
      :type: str
      :value: '127.0.0.1'

      

   .. py:attribute:: env_server_host
      :type: str
      :value: '0.0.0.0'

      

   .. py:attribute:: vnc_port
      :type: int
      :value: 5900

      

   .. py:attribute:: env_server_port
      :type: int
      :value: 8000

      

   .. py:attribute:: vnc_password
      :type: str
      :value: '123456'

      

   .. py:attribute:: monitor_idx
      :type: int
      :value: 1

      

   .. py:attribute:: vnc_frame_size
      :type: tuple[int, int]
      :value: (1000, 1000)

      

   .. py:attribute:: record_path
      :value: 'data/trajectories'

      

   .. py:attribute:: video_fps
      :type: int
      :value: 5

      

   .. py:attribute:: mouse_fps
      :type: int
      :value: 5

      

   .. py:attribute:: stop_hotkeys
      :type: str
      :value: '<ctrl>+<shift>+h'

      

   .. py:attribute:: prompt_folder
      :type: str
      :value: 'agent_studio/agent/prompts'

      

   .. py:attribute:: init_code_path
      :type: str
      :value: 'agent_studio/agent/prompts/init_code.txt'

      

   .. py:attribute:: provider
      :type: str
      :value: 'remote'

      

   .. py:attribute:: agent
      :type: str
      :value: 'direct'

      

   .. py:attribute:: max_retries
      :type: int
      :value: 3

      

   .. py:attribute:: exec_model
      :type: str
      :value: 'gemini-pro-vision'

      

   .. py:attribute:: eval_model
      :type: str

      

   .. py:attribute:: model_server
      :type: str
      :value: 'http://127.0.0.1:65123'

      

   .. py:attribute:: temperature
      :type: float
      :value: 0.0

      

   .. py:attribute:: max_tokens
      :type: int
      :value: 4096

      

   .. py:attribute:: gemini_api_key
      :type: str
      :value: 'LOAD_FROM_API_KEY_PATH_AUTOMATICALLY'

      

   .. py:attribute:: openai_api_key
      :type: str
      :value: 'LOAD_FROM_API_KEY_PATH_AUTOMATICALLY'

      

   .. py:attribute:: anthropic_api_key
      :type: str
      :value: 'LOAD_FROM_API_KEY_PATH_AUTOMATICALLY'

      

   .. py:attribute:: google_credential_path
      :type: str
      :value: 'agent_studio/config/credentials.json'

      

   .. py:attribute:: google_calendar_id
      :type: str
      :value: 'LOAD_FROM_API_KEY_PATH_AUTOMATICALLY'

      

   .. py:attribute:: gmail_recipient
      :type: str
      :value: 'test@outlook.com'

      

   .. py:attribute:: vscode_workspace_path
      :type: str
      :value: 'vscode_workspace'

      

   .. py:attribute:: vscode_executable_path
      :type: str
      :value: 'code'

      

   .. py:attribute:: telegram_workdir
      :type: str
      :value: 'agent_studio/config'

      

   .. py:attribute:: telegram_api_id
      :type: int | str
      :value: 'LOAD_FROM_API_KEY_PATH_AUTOMATICALLY'

      

   .. py:attribute:: telegram_api_hash
      :type: str
      :value: 'LOAD_FROM_API_KEY_PATH_AUTOMATICALLY'

      

   .. py:attribute:: qa_answer_pattern
      :type: str
      :value: '\\[\\[\\[(.*?)\\]\\]\\]'

      

   .. py:attribute:: project_root
      :type: pathlib.Path

      

   .. py:attribute:: log_dir
      :type: pathlib.Path

      


