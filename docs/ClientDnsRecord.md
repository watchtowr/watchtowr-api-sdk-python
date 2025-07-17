# ClientDnsRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**name** | **str** |  | 
**type** | **str** |  | 
**ttl** | **float** | Time To Live | 
**value** | **str** |  | 
**discovered_on** | [**DatetimeDate**](datetime.date.md) |  | 

## Example

```python
from openapi_client.models.client_dns_record import ClientDnsRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ClientDnsRecord from a JSON string
client_dns_record_instance = ClientDnsRecord.from_json(json)
# print the JSON string representation of the object
print(ClientDnsRecord.to_json())

# convert the object into a dict
client_dns_record_dict = client_dns_record_instance.to_dict()
# create an instance of ClientDnsRecord from a dict
client_dns_record_from_dict = ClientDnsRecord.from_dict(client_dns_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


