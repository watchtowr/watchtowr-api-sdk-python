# CapecPattern


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capec_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from watchtowr_api_sdk.models.capec_pattern import CapecPattern

# TODO update the JSON string below
json = "{}"
# create an instance of CapecPattern from a JSON string
capec_pattern_instance = CapecPattern.from_json(json)
# print the JSON string representation of the object
print(CapecPattern.to_json())

# convert the object into a dict
capec_pattern_dict = capec_pattern_instance.to_dict()
# create an instance of CapecPattern from a dict
capec_pattern_from_dict = CapecPattern.from_dict(capec_pattern_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


