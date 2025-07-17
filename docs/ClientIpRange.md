# ClientIpRange


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
**iprange** | **str** |  | 
**asn** | **str** |  | 
**desc** | **str** |  | 
**country** | **str** |  | 
**business_units** | [**List[ClientBusinessUnit]**](ClientBusinessUnit.md) |  | 
**custom_properties** | [**List[ClientCustomProperty]**](ClientCustomProperty.md) |  | 
**criticality** | **str** |  | 

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


