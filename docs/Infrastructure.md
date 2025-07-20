# Infrastructure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdn** | **str** |  | [optional] 
**cloud** | **str** |  | [optional] 
**waf** | **str** |  | [optional] 

## Example

```python
from watchtowr_api_sdk.models.infrastructure import Infrastructure

# TODO update the JSON string below
json = "{}"
# create an instance of Infrastructure from a JSON string
infrastructure_instance = Infrastructure.from_json(json)
# print the JSON string representation of the object
print(Infrastructure.to_json())

# convert the object into a dict
infrastructure_dict = infrastructure_instance.to_dict()
# create an instance of Infrastructure from a dict
infrastructure_from_dict = Infrastructure.from_dict(infrastructure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


