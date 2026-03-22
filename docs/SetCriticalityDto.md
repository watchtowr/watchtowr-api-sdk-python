# SetCriticalityDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criticality** | **str** | The criticality level to assign to the asset. Accepted values are &#39;High&#39;, &#39;Medium&#39;, &#39;Low&#39;, &#39;Unknown&#39;. | 

## Example

```python
from watchtowr_api_sdk.models.set_criticality_dto import SetCriticalityDto

# TODO update the JSON string below
json = "{}"
# create an instance of SetCriticalityDto from a JSON string
set_criticality_dto_instance = SetCriticalityDto.from_json(json)
# print the JSON string representation of the object
print(SetCriticalityDto.to_json())

# convert the object into a dict
set_criticality_dto_dict = set_criticality_dto_instance.to_dict()
# create an instance of SetCriticalityDto from a dict
set_criticality_dto_from_dict = SetCriticalityDto.from_dict(set_criticality_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


