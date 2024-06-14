:py:mod:`agent_studio.utils.json_utils`
=======================================

.. py:module:: agent_studio.utils.json_utils


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   agent_studio.utils.json_utils.read_jsonl
   agent_studio.utils.json_utils.add_jsonl
   agent_studio.utils.json_utils.read_json
   agent_studio.utils.json_utils.add_json
   agent_studio.utils.json_utils.format_json
   agent_studio.utils.json_utils.export_trajectories
   agent_studio.utils.json_utils.save_image_or_array
   agent_studio.utils.json_utils.parse_and_save_objects



.. py:function:: read_jsonl(file_path: str, start_idx: int = 0, end_idx: int | None = None) -> list

   Reads lines from a .jsonl file between start_idx and end_idx.

   :param file_path: Path to the .jsonl file
   :type file_path: str
   :param start_idx: The starting index of lines to read
   :type start_idx: int, optional
   :param end_idx: The ending index of lines to read
   :type end_idx: int | None, optional

   :returns:

             A list of dictionaries, each dictionary is a line from
                 the .jsonl file
   :rtype: list[dict]


.. py:function:: add_jsonl(data: list, file_path: str, mode='a')

   Adds a list of dictionaries to a .jsonl file.

   :param data: A list of json objects to add to the file
   :type data: list[dict]
   :param file_path: Path to the .jsonl file
   :type file_path: str


.. py:function:: read_json(file_path: str, start_idx: int = 0, end_idx: int | None = None) -> dict

   Reads a dictionary from a .json file.

   :param file_path: Path to the .json file
   :type file_path: str


.. py:function:: add_json(data: dict, file_path: str, mode='a')

   Adds a dictionary to a .json file.

   :param data: The dictionary to add to the file
   :type data: dict
   :param file_path: Path to the .json file
   :type file_path: str


.. py:function:: format_json(data: dict, indent=4, sort_keys=False)

   Prints a dictionary in a formatted way.

   :param data: The dictionary to print
   :type data: dict


.. py:function:: export_trajectories(self_eval_results: dict | None, task_config: dict, trajectory: list, record_path: str, score: float | None, feedback: str | None, token_count: int | None, video_meta: dict | None = None, jsonl_name: str = 'results.jsonl') -> None

   Exports the trajectory data to a .jsonl file.


.. py:function:: save_image_or_array(obj: Any, folder_path: str) -> str


.. py:function:: parse_and_save_objects(obj: Any, folder_path: str) -> Any


