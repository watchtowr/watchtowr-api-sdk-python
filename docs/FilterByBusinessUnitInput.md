# FilterByBusinessUnitInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Business unit ID | [optional] 
**type** | **str** | Business unit type | 
**name** | **str** | Business unit name | [optional] 

## Example

```python
from watchtowr_api_sdk.models.filter_by_business_unit_input import FilterByBusinessUnitInput

# TODO update the JSON string below
json = "{}"
# create an instance of FilterByBusinessUnitInput from a JSON string
filter_by_business_unit_input_instance = FilterByBusinessUnitInput.from_json(json)
# print the JSON string representation of the object
print(FilterByBusinessUnitInput.to_json())

# convert the object into a dict
filter_by_business_unit_input_dict = filter_by_business_unit_input_instance.to_dict()
# create an instance of FilterByBusinessUnitInput from a dict
filter_by_business_unit_input_from_dict = FilterByBusinessUnitInput.from_dict(filter_by_business_unit_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


