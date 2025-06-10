# ClientCloudAssetData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientCloudAsset**](ClientCloudAsset.md) |  | 

## Example

```python
from openapi_client.models.client_cloud_asset_data import ClientCloudAssetData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCloudAssetData from a JSON string
client_cloud_asset_data_instance = ClientCloudAssetData.from_json(json)
# print the JSON string representation of the object
print(ClientCloudAssetData.to_json())

# convert the object into a dict
client_cloud_asset_data_dict = client_cloud_asset_data_instance.to_dict()
# create an instance of ClientCloudAssetData from a dict
client_cloud_asset_data_from_dict = ClientCloudAssetData.from_dict(client_cloud_asset_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


