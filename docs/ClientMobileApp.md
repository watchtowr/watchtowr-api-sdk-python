# ClientMobileApp


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
**publisher** | **str** |  | 
**platform** | **str** |  | 
**app_id** | **str** |  | 
**url** | **str** |  | [optional] 
**s3path** | **str** |  | [optional] 
**business_units** | [**List[ClientBusinessUnit]**](ClientBusinessUnit.md) |  | 
**metadata** | **object** | Additional asset metadata; shape varies by asset type. Defaults to an empty object. | 
**custom_properties** | [**List[ClientCustomProperty]**](ClientCustomProperty.md) |  | 
**criticality** | **str** |  | [optional] 

## Example

```python
from watchtowr_api_sdk.models.client_mobile_app import ClientMobileApp

# TODO update the JSON string below
json = "{}"
# create an instance of ClientMobileApp from a JSON string
client_mobile_app_instance = ClientMobileApp.from_json(json)
# print the JSON string representation of the object
print(ClientMobileApp.to_json())

# convert the object into a dict
client_mobile_app_dict = client_mobile_app_instance.to_dict()
# create an instance of ClientMobileApp from a dict
client_mobile_app_from_dict = ClientMobileApp.from_dict(client_mobile_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


