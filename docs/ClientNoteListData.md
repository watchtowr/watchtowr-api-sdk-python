# ClientNoteListData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientNote]**](ClientNote.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.client_note_list_data import ClientNoteListData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientNoteListData from a JSON string
client_note_list_data_instance = ClientNoteListData.from_json(json)
# print the JSON string representation of the object
print(ClientNoteListData.to_json())

# convert the object into a dict
client_note_list_data_dict = client_note_list_data_instance.to_dict()
# create an instance of ClientNoteListData from a dict
client_note_list_data_from_dict = ClientNoteListData.from_dict(client_note_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


