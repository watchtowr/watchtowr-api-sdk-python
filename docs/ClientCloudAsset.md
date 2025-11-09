# ClientCloudAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | 
**source** | **str** |  | 
**provider** | **str** |  | 
**super_type** | **str** |  | 
**sub_type** | **str** |  | 
**hostname** | **str** |  | 
**cloud_resource_id** | **str** |  | 
**created_at** | [**datetime.date**](datetime.date.md) |  | 
**updated_at** | [**datetime.date**](datetime.date.md) |  | 
**deleted_at** | [**datetime.date**](datetime.date.md) |  | 
**metadata** | **object** |  | 
**custom_properties** | [**List[ClientCustomProperty]**](ClientCustomProperty.md) |  | 
**criticality** | **str** |  | 

## Example

```python
from watchtowr_api_sdk.models.client_cloud_asset import ClientCloudAsset

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCloudAsset from a JSON string
client_cloud_asset_instance = ClientCloudAsset.from_json(json)
# print the JSON string representation of the object
print(ClientCloudAsset.to_json())

# convert the object into a dict
client_cloud_asset_dict = client_cloud_asset_instance.to_dict()
# create an instance of ClientCloudAsset from a dict
client_cloud_asset_from_dict = ClientCloudAsset.from_dict(client_cloud_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


