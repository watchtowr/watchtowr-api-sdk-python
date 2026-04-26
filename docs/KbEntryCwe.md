# KbEntryCwe


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cwe_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from watchtowr_api_sdk.models.kb_entry_cwe import KbEntryCwe

# TODO update the JSON string below
json = "{}"
# create an instance of KbEntryCwe from a JSON string
kb_entry_cwe_instance = KbEntryCwe.from_json(json)
# print the JSON string representation of the object
print(KbEntryCwe.to_json())

# convert the object into a dict
kb_entry_cwe_dict = kb_entry_cwe_instance.to_dict()
# create an instance of KbEntryCwe from a dict
kb_entry_cwe_from_dict = KbEntryCwe.from_dict(kb_entry_cwe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


