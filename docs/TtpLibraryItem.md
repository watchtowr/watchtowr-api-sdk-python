# TtpLibraryItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Tactic ID | 
**name** | **str** | Tactic name | 
**identifier** | **str** | Tactic identifier | 
**type** | **str** | Tactic type | 
**category** | [**TtpLibraryCategoryItem**](TtpLibraryCategoryItem.md) | Parent category | 
**module** | **str** | Module name | [optional] 
**enabled_on** | **datetime** | Date the tactic was enabled | [optional] 

## Example

```python
from watchtowr_api_sdk.models.ttp_library_item import TtpLibraryItem

# TODO update the JSON string below
json = "{}"
# create an instance of TtpLibraryItem from a JSON string
ttp_library_item_instance = TtpLibraryItem.from_json(json)
# print the JSON string representation of the object
print(TtpLibraryItem.to_json())

# convert the object into a dict
ttp_library_item_dict = ttp_library_item_instance.to_dict()
# create an instance of TtpLibraryItem from a dict
ttp_library_item_from_dict = TtpLibraryItem.from_dict(ttp_library_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


