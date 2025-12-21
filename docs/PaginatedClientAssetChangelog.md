# PaginatedClientAssetChangelog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientActivityLog]**](ClientActivityLog.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.paginated_client_asset_changelog import PaginatedClientAssetChangelog

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClientAssetChangelog from a JSON string
paginated_client_asset_changelog_instance = PaginatedClientAssetChangelog.from_json(json)
# print the JSON string representation of the object
print(PaginatedClientAssetChangelog.to_json())

# convert the object into a dict
paginated_client_asset_changelog_dict = paginated_client_asset_changelog_instance.to_dict()
# create an instance of PaginatedClientAssetChangelog from a dict
paginated_client_asset_changelog_from_dict = PaginatedClientAssetChangelog.from_dict(paginated_client_asset_changelog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


