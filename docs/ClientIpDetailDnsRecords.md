# ClientIpDetailDnsRecords


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_records_owned** | **List[str]** |  | 
**dns_records_pointing_at** | **List[str]** |  | 

## Example

```python
from watchtowr_api_sdk.models.client_ip_detail_dns_records import ClientIpDetailDnsRecords

# TODO update the JSON string below
json = "{}"
# create an instance of ClientIpDetailDnsRecords from a JSON string
client_ip_detail_dns_records_instance = ClientIpDetailDnsRecords.from_json(json)
# print the JSON string representation of the object
print(ClientIpDetailDnsRecords.to_json())

# convert the object into a dict
client_ip_detail_dns_records_dict = client_ip_detail_dns_records_instance.to_dict()
# create an instance of ClientIpDetailDnsRecords from a dict
client_ip_detail_dns_records_from_dict = ClientIpDetailDnsRecords.from_dict(client_ip_detail_dns_records_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


