# ClientEngineSettingsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adversary_sight_enabled** | **bool** | Indicates whether the Adversary Sight engine coverage is enabled for the asset. | 
**automated_red_teaming_enabled** | **bool** | Indicates whether the Automated Red Teaming engine coverage is enabled for the asset. | 
**credential_stuffing_enabled** | **bool** | Indicates whether the Credential Stuffing engine coverage is enabled for the asset. | 
**dns_bruteforcing_enabled** | **bool** | Indicates whether the DNS Bruteforcing engine coverage is enabled for the asset. | 
**rapid_reaction_enabled** | **bool** | Indicates whether the Rapid Reaction engine coverage is enabled for the asset | 
**intrusive_http_checks_enabled** | **bool** | Indicates whether the Intrusive HTTP Checks engine coverage is enabled for the asset. | 
**id** | **float** | The asset ID | 
**type** | **str** | The asset type | 

## Example

```python
from watchtowr_api_sdk.models.client_engine_settings_details import ClientEngineSettingsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ClientEngineSettingsDetails from a JSON string
client_engine_settings_details_instance = ClientEngineSettingsDetails.from_json(json)
# print the JSON string representation of the object
print(ClientEngineSettingsDetails.to_json())

# convert the object into a dict
client_engine_settings_details_dict = client_engine_settings_details_instance.to_dict()
# create an instance of ClientEngineSettingsDetails from a dict
client_engine_settings_details_from_dict = ClientEngineSettingsDetails.from_dict(client_engine_settings_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


