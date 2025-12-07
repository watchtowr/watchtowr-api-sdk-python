# PaginatedClientSeedData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientSeedDataListItem]**](ClientSeedDataListItem.md) | List of submitted seed data items | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.paginated_client_seed_data import PaginatedClientSeedData

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClientSeedData from a JSON string
paginated_client_seed_data_instance = PaginatedClientSeedData.from_json(json)
# print the JSON string representation of the object
print(PaginatedClientSeedData.to_json())

# convert the object into a dict
paginated_client_seed_data_dict = paginated_client_seed_data_instance.to_dict()
# create an instance of PaginatedClientSeedData from a dict
paginated_client_seed_data_from_dict = PaginatedClientSeedData.from_dict(paginated_client_seed_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


