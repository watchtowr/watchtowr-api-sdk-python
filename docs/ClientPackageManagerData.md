# ClientPackageManagerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientPackageManager**](ClientPackageManager.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.client_package_manager_data import ClientPackageManagerData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientPackageManagerData from a JSON string
client_package_manager_data_instance = ClientPackageManagerData.from_json(json)
# print the JSON string representation of the object
print(ClientPackageManagerData.to_json())

# convert the object into a dict
client_package_manager_data_dict = client_package_manager_data_instance.to_dict()
# create an instance of ClientPackageManagerData from a dict
client_package_manager_data_from_dict = ClientPackageManagerData.from_dict(client_package_manager_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


