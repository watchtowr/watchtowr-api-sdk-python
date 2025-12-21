# UpdateClientEngineSettingsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adversary_sight_enabled** | **bool** | This setting manages the Adversary Sight engine coverage for the asset. | 
**dns_bruteforcing_enabled** | **bool** | This setting manages the DNS Bruteforcing engine coverage for the asset. | 
**automated_red_teaming_enabled** | **bool** | This setting manages the Automated Red Teaming engine coverage for the asset. | 
**intrusive_http_checks_enabled** | **bool** | This setting manages Intrusive HTTP Checks engine coverage for the asset. | 
**credential_stuffing_enabled** | **bool** | This setting manages the Credential Stuffing engine coverage for the asset. | 
**rapid_reaction_enabled** | **bool** |  This setting manages the Rapid Reaction engine coverage for the asset | 

## Example

```python
from watchtowr_api_sdk.models.update_client_engine_settings_dto import UpdateClientEngineSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClientEngineSettingsDto from a JSON string
update_client_engine_settings_dto_instance = UpdateClientEngineSettingsDto.from_json(json)
# print the JSON string representation of the object
print(UpdateClientEngineSettingsDto.to_json())

# convert the object into a dict
update_client_engine_settings_dto_dict = update_client_engine_settings_dto_instance.to_dict()
# create an instance of UpdateClientEngineSettingsDto from a dict
update_client_engine_settings_dto_from_dict = UpdateClientEngineSettingsDto.from_dict(update_client_engine_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


