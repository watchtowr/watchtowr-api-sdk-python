# ClientCloudStorage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discovery_reason** | **str** |  | [optional] 
**type** | **str** |  | 
**source** | **str** |  | 
**status** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**platform** | **str** |  | 
**url** | **str** |  | [optional] 
**business_units** | [**List[ClientBusinessUnit]**](ClientBusinessUnit.md) |  | 
**metadata** | **object** | Additional asset metadata; shape varies by asset type. Defaults to an empty object. | 
**custom_properties** | [**List[ClientCustomProperty]**](ClientCustomProperty.md) |  | 
**criticality** | **str** |  | [optional] 

## Example

```python
from watchtowr_api_sdk.models.client_cloud_storage import ClientCloudStorage

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCloudStorage from a JSON string
client_cloud_storage_instance = ClientCloudStorage.from_json(json)
# print the JSON string representation of the object
print(ClientCloudStorage.to_json())

# convert the object into a dict
client_cloud_storage_dict = client_cloud_storage_instance.to_dict()
# create an instance of ClientCloudStorage from a dict
client_cloud_storage_from_dict = ClientCloudStorage.from_dict(client_cloud_storage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


