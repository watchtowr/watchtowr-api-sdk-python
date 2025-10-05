# PaginatedUsers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientUser]**](ClientUser.md) | List of users | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.paginated_users import PaginatedUsers

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUsers from a JSON string
paginated_users_instance = PaginatedUsers.from_json(json)
# print the JSON string representation of the object
print(PaginatedUsers.to_json())

# convert the object into a dict
paginated_users_dict = paginated_users_instance.to_dict()
# create an instance of PaginatedUsers from a dict
paginated_users_from_dict = PaginatedUsers.from_dict(paginated_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


