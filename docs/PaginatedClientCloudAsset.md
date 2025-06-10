# PaginatedClientCloudAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientCloudAsset]**](ClientCloudAsset.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openapi_client.models.paginated_client_cloud_asset import PaginatedClientCloudAsset

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClientCloudAsset from a JSON string
paginated_client_cloud_asset_instance = PaginatedClientCloudAsset.from_json(json)
# print the JSON string representation of the object
print(PaginatedClientCloudAsset.to_json())

# convert the object into a dict
paginated_client_cloud_asset_dict = paginated_client_cloud_asset_instance.to_dict()
# create an instance of PaginatedClientCloudAsset from a dict
paginated_client_cloud_asset_from_dict = PaginatedClientCloudAsset.from_dict(paginated_client_cloud_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


