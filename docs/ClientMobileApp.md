# ClientMobileApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**source** | **str** |  | 
**status** | **str** |  | 
**created_at** | [**DatetimeDate**](datetime.date.md) |  | 
**updated_at** | [**DatetimeDate**](datetime.date.md) |  | 
**deleted_at** | [**DatetimeDate**](datetime.date.md) |  | 
**id** | **float** |  | 
**name** | **str** |  | 
**publisher** | **str** |  | 
**platform** | **str** |  | 
**app_id** | **str** |  | 
**url** | **str** |  | 
**s3path** | **str** |  | 
**business_units** | [**List[ClientBusinessUnit]**](ClientBusinessUnit.md) |  | 
**custom_properties** | [**List[ClientCustomProperty]**](ClientCustomProperty.md) |  | 
**criticality** | **str** |  | 

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


