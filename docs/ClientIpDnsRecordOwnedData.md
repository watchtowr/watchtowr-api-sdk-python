# ClientIpDnsRecordOwnedData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientDnsRecord]**](ClientDnsRecord.md) |  | 

## Example

```python
from openapi_client.models.client_ip_dns_record_owned_data import ClientIpDnsRecordOwnedData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientIpDnsRecordOwnedData from a JSON string
client_ip_dns_record_owned_data_instance = ClientIpDnsRecordOwnedData.from_json(json)
# print the JSON string representation of the object
print(ClientIpDnsRecordOwnedData.to_json())

# convert the object into a dict
client_ip_dns_record_owned_data_dict = client_ip_dns_record_owned_data_instance.to_dict()
# create an instance of ClientIpDnsRecordOwnedData from a dict
client_ip_dns_record_owned_data_from_dict = ClientIpDnsRecordOwnedData.from_dict(client_ip_dns_record_owned_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


