# PaginatedClientPackageManager


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientPackageManager]**](ClientPackageManager.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.paginated_client_package_manager import PaginatedClientPackageManager

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClientPackageManager from a JSON string
paginated_client_package_manager_instance = PaginatedClientPackageManager.from_json(json)
# print the JSON string representation of the object
print(PaginatedClientPackageManager.to_json())

# convert the object into a dict
paginated_client_package_manager_dict = paginated_client_package_manager_instance.to_dict()
# create an instance of PaginatedClientPackageManager from a dict
paginated_client_package_manager_from_dict = PaginatedClientPackageManager.from_dict(paginated_client_package_manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


