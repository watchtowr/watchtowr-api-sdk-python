# CapabilitySearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CapabilitySearchData**](CapabilitySearchData.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.capability_search_response import CapabilitySearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilitySearchResponse from a JSON string
capability_search_response_instance = CapabilitySearchResponse.from_json(json)
# print the JSON string representation of the object
print(CapabilitySearchResponse.to_json())

# convert the object into a dict
capability_search_response_dict = capability_search_response_instance.to_dict()
# create an instance of CapabilitySearchResponse from a dict
capability_search_response_from_dict = CapabilitySearchResponse.from_dict(capability_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


