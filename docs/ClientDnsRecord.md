# ClientDnsRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | DNS Record ID | 
**asset** | [**ClientDnsRecordAsset**](ClientDnsRecordAsset.md) | Asset information | 
**record_name** | **str** | Identifies the resource this record resolves to. | 
**type** | **str** | The DNS record type defines the purpose or function of the record, such as domain name resolution, email routing, and more. | 
**ttl** | **float** | Time to live (TTL) controls how long each record is cached by resolvers. | 
**value** | **str** | The value of a DNS record, depending on the record type. For example, the IP address of the origin server that hosts the web content served by an A or AAAA record. | 
**created_at** | **datetime** | Creation date | 

## Example

```python
from watchtowr_api_sdk.models.client_dns_record import ClientDnsRecord

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


