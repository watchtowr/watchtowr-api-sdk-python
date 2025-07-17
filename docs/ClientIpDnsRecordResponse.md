# ClientIpDnsRecordResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientIpDnsRecordData**](ClientIpDnsRecordData.md) |  | 

## Example

```python
from openapi_client.models.client_ip_dns_record_response import ClientIpDnsRecordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClientIpDnsRecordResponse from a JSON string
client_ip_dns_record_response_instance = ClientIpDnsRecordResponse.from_json(json)
# print the JSON string representation of the object
print(ClientIpDnsRecordResponse.to_json())

# convert the object into a dict
client_ip_dns_record_response_dict = client_ip_dns_record_response_instance.to_dict()
# create an instance of ClientIpDnsRecordResponse from a dict
client_ip_dns_record_response_from_dict = ClientIpDnsRecordResponse.from_dict(client_ip_dns_record_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


