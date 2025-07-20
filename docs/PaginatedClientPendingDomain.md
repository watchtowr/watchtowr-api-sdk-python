# PaginatedClientPendingDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientPendingDomain]**](ClientPendingDomain.md) | List of pending domain items | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.paginated_client_pending_domain import PaginatedClientPendingDomain

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClientPendingDomain from a JSON string
paginated_client_pending_domain_instance = PaginatedClientPendingDomain.from_json(json)
# print the JSON string representation of the object
print(PaginatedClientPendingDomain.to_json())

# convert the object into a dict
paginated_client_pending_domain_dict = paginated_client_pending_domain_instance.to_dict()
# create an instance of PaginatedClientPendingDomain from a dict
paginated_client_pending_domain_from_dict = PaginatedClientPendingDomain.from_dict(paginated_client_pending_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


