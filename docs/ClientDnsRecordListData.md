# ClientDnsRecordListData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientDnsRecord]**](ClientDnsRecord.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.client_dns_record_list_data import ClientDnsRecordListData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientDnsRecordListData from a JSON string
client_dns_record_list_data_instance = ClientDnsRecordListData.from_json(json)
# print the JSON string representation of the object
print(ClientDnsRecordListData.to_json())

# convert the object into a dict
client_dns_record_list_data_dict = client_dns_record_list_data_instance.to_dict()
# create an instance of ClientDnsRecordListData from a dict
client_dns_record_list_data_from_dict = ClientDnsRecordListData.from_dict(client_dns_record_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


