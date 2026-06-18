# ClientIpRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discovery_reason** | **str** |  | [optional] 
**type** | **str** |  | 
**source** | **str** |  | 
**status** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**iprange** | **str** |  | 
**asn** | **str** |  | 
**desc** | **str** |  | 
**country** | **str** |  | 
**business_units** | [**List[ClientBusinessUnit]**](ClientBusinessUnit.md) |  | 
**metadata** | **object** | Additional asset metadata; shape varies by asset type. Defaults to an empty object. | 
**custom_properties** | [**List[ClientCustomProperty]**](ClientCustomProperty.md) |  | 
**criticality** | **str** |  | [optional] 

## Example

```python
from watchtowr_api_sdk.models.client_ip_range import ClientIpRange

# TODO update the JSON string below
json = "{}"
# create an instance of ClientIpRange from a JSON string
client_ip_range_instance = ClientIpRange.from_json(json)
# print the JSON string representation of the object
print(ClientIpRange.to_json())

# convert the object into a dict
client_ip_range_dict = client_ip_range_instance.to_dict()
# create an instance of ClientIpRange from a dict
client_ip_range_from_dict = ClientIpRange.from_dict(client_ip_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


