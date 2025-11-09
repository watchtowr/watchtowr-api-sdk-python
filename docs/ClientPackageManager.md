# ClientPackageManager


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | 
**source** | **str** |  | 
**status** | **str** |  | 
**created_at** | [**datetime.date**](datetime.date.md) |  | 
**updated_at** | [**datetime.date**](datetime.date.md) |  | 
**deleted_at** | [**datetime.date**](datetime.date.md) |  | 
**id** | **float** |  | 
**url** | **str** |  | 
**platform** | **str** |  | 
**business_units** | [**List[ClientBusinessUnit]**](ClientBusinessUnit.md) |  | 
**custom_properties** | [**List[ClientCustomProperty]**](ClientCustomProperty.md) |  | 
**criticality** | **str** |  | 

## Example

```python
from watchtowr_api_sdk.models.client_package_manager import ClientPackageManager

# TODO update the JSON string below
json = "{}"
# create an instance of ClientPackageManager from a JSON string
client_package_manager_instance = ClientPackageManager.from_json(json)
# print the JSON string representation of the object
print(ClientPackageManager.to_json())

# convert the object into a dict
client_package_manager_dict = client_package_manager_instance.to_dict()
# create an instance of ClientPackageManager from a dict
client_package_manager_from_dict = ClientPackageManager.from_dict(client_package_manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


