# ClientIpRelatedDnsRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**name** | **str** |  | 
**type** | **str** |  | 
**ttl** | **float** | Time To Live | 
**value** | **str** |  | 
**discovered_on** | [**datetime.date**](datetime.date.md) |  | 
**asset** | [**ClientIpRelatedDnsRecordAsset**](ClientIpRelatedDnsRecordAsset.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.client_ip_related_dns_record import ClientIpRelatedDnsRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ClientIpRelatedDnsRecord from a JSON string
client_ip_related_dns_record_instance = ClientIpRelatedDnsRecord.from_json(json)
# print the JSON string representation of the object
print(ClientIpRelatedDnsRecord.to_json())

# convert the object into a dict
client_ip_related_dns_record_dict = client_ip_related_dns_record_instance.to_dict()
# create an instance of ClientIpRelatedDnsRecord from a dict
client_ip_related_dns_record_from_dict = ClientIpRelatedDnsRecord.from_dict(client_ip_related_dns_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


