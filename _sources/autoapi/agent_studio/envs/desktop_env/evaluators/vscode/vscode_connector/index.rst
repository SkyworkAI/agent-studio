:py:mod:`agent_studio.envs.desktop_env.evaluators.vscode.vscode_connector`
==========================================================================

.. py:module:: agent_studio.envs.desktop_env.evaluators.vscode.vscode_connector


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   agent_studio.envs.desktop_env.evaluators.vscode.vscode_connector.FilterType
   agent_studio.envs.desktop_env.evaluators.vscode.vscode_connector.SortBy
   agent_studio.envs.desktop_env.evaluators.vscode.vscode_connector.SortOrder
   agent_studio.envs.desktop_env.evaluators.vscode.vscode_connector.VSCodeConnector




.. py:class:: FilterType


   Bases: :py:obj:`enum.Enum`

   Filter type for marketplace search

   .. py:attribute:: Tag
      :value: 1

      

   .. py:attribute:: ExtensionId
      :value: 4

      

   .. py:attribute:: Category
      :value: 5

      

   .. py:attribute:: ExtensionName
      :value: 7

      

   .. py:attribute:: Target
      :value: 8

      

   .. py:attribute:: Featured
      :value: 9

      

   .. py:attribute:: SearchText
      :value: 10

      

   .. py:attribute:: ExcludeWithFlags
      :value: 12

      


.. py:class:: SortBy


   Bases: :py:obj:`enum.Enum`

   Result sorting options for marketplace search

   .. py:attribute:: NoneOrRelevance
      :value: 0

      

   .. py:attribute:: LastUpdatedDate
      :value: 1

      

   .. py:attribute:: Title
      :value: 2

      

   .. py:attribute:: PublisherName
      :value: 3

      

   .. py:attribute:: InstallCount
      :value: 4

      

   .. py:attribute:: PublishedDate
      :value: 10

      

   .. py:attribute:: AverageRating
      :value: 6

      

   .. py:attribute:: WeightedRating
      :value: 12

      


.. py:class:: SortOrder


   Bases: :py:obj:`enum.Enum`

   Sort order for marketplace search

   .. py:attribute:: Default
      :value: 0

      

   .. py:attribute:: Ascending
      :value: 1

      

   .. py:attribute:: Descending
      :value: 2

      


.. py:class:: VSCodeConnector(workspace_path: str, executable_path: str = 'code')


   .. py:method:: marketplace_search(query: list[dict], sort_by: SortBy, sort_order: SortOrder)

      Search for extensions in the marketplace

      :param query: List of query filters
      :type query: list[dict]
      :param sort_by: Sort by option
      :type sort_by: SortBy
      :param sort_order: Sort order option
      :type sort_order: SortOrder

      :returns: List of extensions
      :rtype: list

      Example::

          query = [
                      {
                          "filterType": FilterType.ExtensionName.value,
                          "value": "DavidAnson.vscode-markdownlint"
                      },
                  ]


   .. py:method:: marketplace_search_by_extension_id(extension_name: str)

      Search by extension name
      Default sort by install count descending


   .. py:method:: marketplace_search_by_keyword(keyword: str)

      Search by keyword
      Default sort by install count descending


   .. py:method:: update_settings(settings: str) -> None


   .. py:method:: compare_settings(settings: str) -> bool


   .. py:method:: reset_settings() -> None


   .. py:method:: list_extensions() -> dict


   .. py:method:: uninstall_all_extensions() -> bool


   .. py:method:: install_extension(extension_name: str) -> bool


   .. py:method:: uninstall_extension(extension_name: str) -> bool


   .. py:method:: extension_installed(extension_name: str) -> bool


   .. py:method:: get_vscode_extensions(session: requests.Session, query: list, max_page: int = 2, page_size: int = 10, sort_by: SortBy = SortBy.InstallCount, sort_order: SortOrder = SortOrder.Descending, include_versions: bool = True, include_files: bool = True, include_category_and_tags: bool = True, include_shared_accounts: bool = True, include_version_properties: bool = True, exclude_non_validated: bool = True, include_installation_targets: bool = True, include_asset_uri: bool = True, include_statistics: bool = True, include_latest_version_only=False, unpublished: bool = True, include_name_conflict_info: bool = True, api_version: str = '7.2-preview.1')
      :staticmethod:

      https://gist.github.com/jossef/8d7681ac0c7fd28e93147aa5044bc129



