# ClientEngineSettingsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientEngineSettingsDetails**](ClientEngineSettingsDetails.md) | Engine settings data | 

## Example

```python
from watchtowr_api_sdk.models.client_engine_settings_data import ClientEngineSettingsData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientEngineSettingsData from a JSON string
client_engine_settings_data_instance = ClientEngineSettingsData.from_json(json)
# print the JSON string representation of the object
print(ClientEngineSettingsData.to_json())

# convert the object into a dict
client_engine_settings_data_dict = client_engine_settings_data_instance.to_dict()
# create an instance of ClientEngineSettingsData from a dict
client_engine_settings_data_from_dict = ClientEngineSettingsData.from_dict(client_engine_settings_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


