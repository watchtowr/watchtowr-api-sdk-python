# SetCriticalityResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | The ID of the custom property record. | 
**key** | **str** | The property key. | 
**value** | **str** | The criticality value. | 
**is_preset** | **bool** | Whether this is a preset property. | 

## Example

```python
from watchtowr_api_sdk.models.set_criticality_response_dto import SetCriticalityResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SetCriticalityResponseDto from a JSON string
set_criticality_response_dto_instance = SetCriticalityResponseDto.from_json(json)
# print the JSON string representation of the object
print(SetCriticalityResponseDto.to_json())

# convert the object into a dict
set_criticality_response_dto_dict = set_criticality_response_dto_instance.to_dict()
# create an instance of SetCriticalityResponseDto from a dict
set_criticality_response_dto_from_dict = SetCriticalityResponseDto.from_dict(set_criticality_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


