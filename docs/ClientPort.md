# ClientPort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**status** | **str** |  | 
**created_at** | [**DatetimeDate**](datetime.date.md) |  | 
**updated_at** | [**DatetimeDate**](datetime.date.md) |  | 
**last_seen_at** | [**DatetimeDate**](datetime.date.md) |  | 
**deleted_at** | [**DatetimeDate**](datetime.date.md) |  | 
**id** | **float** |  | 
**ip** | **str** |  | 
**ip_id** | **float** |  | 
**port** | **float** |  | 
**banner** | **str** |  | 
**service** | **str** |  | 
**business_units** | [**List[ClientBusinessUnit]**](ClientBusinessUnit.md) |  | 

## Example

```python
from openapi_client.models.client_port import ClientPort

# TODO update the JSON string below
json = "{}"
# create an instance of ClientPort from a JSON string
client_port_instance = ClientPort.from_json(json)
# print the JSON string representation of the object
print(ClientPort.to_json())

# convert the object into a dict
client_port_dict = client_port_instance.to_dict()
# create an instance of ClientPort from a dict
client_port_from_dict = ClientPort.from_dict(client_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


