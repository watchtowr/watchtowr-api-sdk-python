# ClientIpDnsRecordPointingAtData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientIpRelatedDnsRecord]**](ClientIpRelatedDnsRecord.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.client_ip_dns_record_pointing_at_data import ClientIpDnsRecordPointingAtData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientIpDnsRecordPointingAtData from a JSON string
client_ip_dns_record_pointing_at_data_instance = ClientIpDnsRecordPointingAtData.from_json(json)
# print the JSON string representation of the object
print(ClientIpDnsRecordPointingAtData.to_json())

# convert the object into a dict
client_ip_dns_record_pointing_at_data_dict = client_ip_dns_record_pointing_at_data_instance.to_dict()
# create an instance of ClientIpDnsRecordPointingAtData from a dict
client_ip_dns_record_pointing_at_data_from_dict = ClientIpDnsRecordPointingAtData.from_dict(client_ip_dns_record_pointing_at_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


