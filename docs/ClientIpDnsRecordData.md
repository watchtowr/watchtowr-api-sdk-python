# ClientIpDnsRecordData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_records_total_count** | **float** |  | 
**dns_records_owned** | [**ClientIpDnsRecordOwnedData**](ClientIpDnsRecordOwnedData.md) |  | 
**dns_records_pointing_at** | [**ClientIpDnsRecordPointingAtData**](ClientIpDnsRecordPointingAtData.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.client_ip_dns_record_data import ClientIpDnsRecordData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientIpDnsRecordData from a JSON string
client_ip_dns_record_data_instance = ClientIpDnsRecordData.from_json(json)
# print the JSON string representation of the object
print(ClientIpDnsRecordData.to_json())

# convert the object into a dict
client_ip_dns_record_data_dict = client_ip_dns_record_data_instance.to_dict()
# create an instance of ClientIpDnsRecordData from a dict
client_ip_dns_record_data_from_dict = ClientIpDnsRecordData.from_dict(client_ip_dns_record_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


