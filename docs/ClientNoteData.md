# ClientNoteData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientNote**](ClientNote.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.client_note_data import ClientNoteData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientNoteData from a JSON string
client_note_data_instance = ClientNoteData.from_json(json)
# print the JSON string representation of the object
print(ClientNoteData.to_json())

# convert the object into a dict
client_note_data_dict = client_note_data_instance.to_dict()
# create an instance of ClientNoteData from a dict
client_note_data_from_dict = ClientNoteData.from_dict(client_note_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


