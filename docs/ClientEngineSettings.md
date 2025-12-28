# ClientEngineSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adversary_sight_enabled** | **bool** | Indicates whether the Adversary Sight engine coverage is enabled for the asset. | 
**automated_red_teaming_enabled** | **bool** | Indicates whether the Automated Red Teaming engine coverage is enabled for the asset. | 
**credential_stuffing_enabled** | **bool** | Indicates whether the Credential Stuffing engine coverage is enabled for the asset. | 
**dns_bruteforcing_enabled** | **bool** | Indicates whether the DNS Bruteforcing engine coverage is enabled for the asset. | 
**rapid_reaction_enabled** | **bool** | Indicates whether the Rapid Reaction engine coverage is enabled for the asset | 
**intrusive_http_checks_enabled** | **bool** | Indicates whether the Intrusive HTTP Check engine coverage is enabled for the asset. | 

## Example

```python
from watchtowr_api_sdk.models.client_engine_settings import ClientEngineSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ClientEngineSettings from a JSON string
client_engine_settings_instance = ClientEngineSettings.from_json(json)
# print the JSON string representation of the object
print(ClientEngineSettings.to_json())

# convert the object into a dict
client_engine_settings_dict = client_engine_settings_instance.to_dict()
# create an instance of ClientEngineSettings from a dict
client_engine_settings_from_dict = ClientEngineSettings.from_dict(client_engine_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


