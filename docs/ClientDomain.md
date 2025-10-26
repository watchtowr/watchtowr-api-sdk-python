# ClientDomain


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
**business_units** | [**List[ClientBusinessUnit]**](ClientBusinessUnit.md) |  | 
**live** | **bool** |  | 
**dns_records** | **List[str]** |  | 
**metadata** | **object** |  | 
**custom_properties** | [**List[ClientCustomProperty]**](ClientCustomProperty.md) |  | 
**criticality** | **str** |  | 
**infrastructure** | [**Infrastructure**](Infrastructure.md) |  | [optional] 
**engine_settings** | [**ClientEngineSettings**](ClientEngineSettings.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.client_domain import ClientDomain

# TODO update the JSON string below
json = "{}"
# create an instance of ClientDomain from a JSON string
client_domain_instance = ClientDomain.from_json(json)
# print the JSON string representation of the object
print(ClientDomain.to_json())

# convert the object into a dict
client_domain_dict = client_domain_instance.to_dict()
# create an instance of ClientDomain from a dict
client_domain_from_dict = ClientDomain.from_dict(client_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


