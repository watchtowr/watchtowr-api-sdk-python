# TtpLibraryCategoryItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Category ID | 
**name** | **str** | Category name | 

## Example

```python
from watchtowr_api_sdk.models.ttp_library_category_item import TtpLibraryCategoryItem

# TODO update the JSON string below
json = "{}"
# create an instance of TtpLibraryCategoryItem from a JSON string
ttp_library_category_item_instance = TtpLibraryCategoryItem.from_json(json)
# print the JSON string representation of the object
print(TtpLibraryCategoryItem.to_json())

# convert the object into a dict
ttp_library_category_item_dict = ttp_library_category_item_instance.to_dict()
# create an instance of TtpLibraryCategoryItem from a dict
ttp_library_category_item_from_dict = TtpLibraryCategoryItem.from_dict(ttp_library_category_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


