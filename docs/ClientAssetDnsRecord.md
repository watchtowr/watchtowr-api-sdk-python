# ClientAssetDnsRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**name** | **str** |  | 
**type** | **str** |  | 
**ttl** | **float** | Time To Live | 
**value** | **str** |  | 
**discovered_on** | [**datetime.date**](datetime.date.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.client_asset_dns_record import ClientAssetDnsRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ClientAssetDnsRecord from a JSON string
client_asset_dns_record_instance = ClientAssetDnsRecord.from_json(json)
# print the JSON string representation of the object
print(ClientAssetDnsRecord.to_json())

# convert the object into a dict
client_asset_dns_record_dict = client_asset_dns_record_instance.to_dict()
# create an instance of ClientAssetDnsRecord from a dict
client_asset_dns_record_from_dict = ClientAssetDnsRecord.from_dict(client_asset_dns_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


