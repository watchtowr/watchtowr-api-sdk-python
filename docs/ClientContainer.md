# ClientContainer


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
**owner** | **str** |  | 
**platform** | **str** |  | 
**url** | **str** |  | [optional] 
**business_units** | [**List[ClientBusinessUnit]**](ClientBusinessUnit.md) |  | 
**metadata** | **object** | Additional asset metadata; shape varies by asset type. Defaults to an empty object. | 
**custom_properties** | [**List[ClientCustomProperty]**](ClientCustomProperty.md) |  | 
**criticality** | **str** |  | [optional] 

## Example

```python
from watchtowr_api_sdk.models.client_container import ClientContainer

# TODO update the JSON string below
json = "{}"
# create an instance of ClientContainer from a JSON string
client_container_instance = ClientContainer.from_json(json)
# print the JSON string representation of the object
print(ClientContainer.to_json())

# convert the object into a dict
client_container_dict = client_container_instance.to_dict()
# create an instance of ClientContainer from a dict
client_container_from_dict = ClientContainer.from_dict(client_container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


