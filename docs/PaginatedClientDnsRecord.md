# PaginatedClientDnsRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientDnsRecord]**](ClientDnsRecord.md) | List of DNS record items | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.paginated_client_dns_record import PaginatedClientDnsRecord

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClientDnsRecord from a JSON string
paginated_client_dns_record_instance = PaginatedClientDnsRecord.from_json(json)
# print the JSON string representation of the object
print(PaginatedClientDnsRecord.to_json())

# convert the object into a dict
paginated_client_dns_record_dict = paginated_client_dns_record_instance.to_dict()
# create an instance of PaginatedClientDnsRecord from a dict
paginated_client_dns_record_from_dict = PaginatedClientDnsRecord.from_dict(paginated_client_dns_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


