# CreateClientNoteDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** | Content of the note. | 
**title** | **str** | Title of the note. | [optional] 

## Example

```python
from openapi_client.models.create_client_note_dto import CreateClientNoteDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClientNoteDto from a JSON string
create_client_note_dto_instance = CreateClientNoteDto.from_json(json)
# print the JSON string representation of the object
print(CreateClientNoteDto.to_json())

# convert the object into a dict
create_client_note_dto_dict = create_client_note_dto_instance.to_dict()
# create an instance of CreateClientNoteDto from a dict
create_client_note_dto_from_dict = CreateClientNoteDto.from_dict(create_client_note_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


