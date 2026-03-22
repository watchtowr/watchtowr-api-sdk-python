# SetCriticalityDataResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SetCriticalityResponseDto**](SetCriticalityResponseDto.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.set_criticality_data_response_dto import SetCriticalityDataResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SetCriticalityDataResponseDto from a JSON string
set_criticality_data_response_dto_instance = SetCriticalityDataResponseDto.from_json(json)
# print the JSON string representation of the object
print(SetCriticalityDataResponseDto.to_json())

# convert the object into a dict
set_criticality_data_response_dto_dict = set_criticality_data_response_dto_instance.to_dict()
# create an instance of SetCriticalityDataResponseDto from a dict
set_criticality_data_response_dto_from_dict = SetCriticalityDataResponseDto.from_dict(set_criticality_data_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


