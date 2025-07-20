# ClientNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**note** | **str** |  | 
**note_type** | **str** |  | 
**note_id** | **float** |  | 
**title** | **str** |  | 
**author** | **object** |  | 
**last_modified** | [**DatetimeDate**](datetime.date.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.client_note import ClientNote

# TODO update the JSON string below
json = "{}"
# create an instance of ClientNote from a JSON string
client_note_instance = ClientNote.from_json(json)
# print the JSON string representation of the object
print(ClientNote.to_json())

# convert the object into a dict
client_note_dict = client_note_instance.to_dict()
# create an instance of ClientNote from a dict
client_note_from_dict = ClientNote.from_dict(client_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


