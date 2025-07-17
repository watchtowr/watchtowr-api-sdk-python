# RemoveClientCustomPropertyResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**status** | **float** |  | 

## Example

```python
from watchtowr_api_sdk.models.remove_client_custom_property_response_dto import RemoveClientCustomPropertyResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveClientCustomPropertyResponseDto from a JSON string
remove_client_custom_property_response_dto_instance = RemoveClientCustomPropertyResponseDto.from_json(json)
# print the JSON string representation of the object
print(RemoveClientCustomPropertyResponseDto.to_json())

# convert the object into a dict
remove_client_custom_property_response_dto_dict = remove_client_custom_property_response_dto_instance.to_dict()
# create an instance of RemoveClientCustomPropertyResponseDto from a dict
remove_client_custom_property_response_dto_from_dict = RemoveClientCustomPropertyResponseDto.from_dict(remove_client_custom_property_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


