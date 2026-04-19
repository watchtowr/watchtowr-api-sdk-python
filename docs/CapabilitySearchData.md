# CapabilitySearchData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hunts** | [**List[CapabilitySearchHuntItem]**](CapabilitySearchHuntItem.md) |  | 
**ttp_library** | [**List[TtpLibraryItem]**](TtpLibraryItem.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.capability_search_data import CapabilitySearchData

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilitySearchData from a JSON string
capability_search_data_instance = CapabilitySearchData.from_json(json)
# print the JSON string representation of the object
print(CapabilitySearchData.to_json())

# convert the object into a dict
capability_search_data_dict = capability_search_data_instance.to_dict()
# create an instance of CapabilitySearchData from a dict
capability_search_data_from_dict = CapabilitySearchData.from_dict(capability_search_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


