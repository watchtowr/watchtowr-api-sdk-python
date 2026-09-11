# ClientPort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Port protocol, always uppercased (e.g. &#x60;TCP&#x60;, &#x60;UDP&#x60;). | 
**status** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**last_seen_at** | **datetime** |  | 
**id** | **str** |  | 
**ip** | **str** |  | [optional] 
**ip_id** | **float** |  | [optional] 
**port** | **float** |  | 
**banner** | **str** |  | [optional] 
**service** | **str** |  | 
**state** | **str** | Port state (e.g. &#x60;open&#x60;, &#x60;closed&#x60;, &#x60;filtered&#x60;). | [optional] 
**business_units** | [**List[ClientBusinessUnit]**](ClientBusinessUnit.md) |  | 
**metadata** | **Dict[str, object]** | Asset-type-specific metadata. Always empty for ports. | 

## Example

```python
from watchtowr_api_sdk.models.client_port import ClientPort

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


