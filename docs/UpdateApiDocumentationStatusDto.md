# UpdateApiDocumentationStatusDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The target status to update the asset to. | 
**status_reason** | **str** | The reason for updating the status. | [optional] 

## Example

```python
from watchtowr_api_sdk.models.update_api_documentation_status_dto import UpdateApiDocumentationStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateApiDocumentationStatusDto from a JSON string
update_api_documentation_status_dto_instance = UpdateApiDocumentationStatusDto.from_json(json)
# print the JSON string representation of the object
print(UpdateApiDocumentationStatusDto.to_json())

# convert the object into a dict
update_api_documentation_status_dto_dict = update_api_documentation_status_dto_instance.to_dict()
# create an instance of UpdateApiDocumentationStatusDto from a dict
update_api_documentation_status_dto_from_dict = UpdateApiDocumentationStatusDto.from_dict(update_api_documentation_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


