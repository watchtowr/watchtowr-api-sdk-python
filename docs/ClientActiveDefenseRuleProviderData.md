# ClientActiveDefenseRuleProviderData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ActiveDefenseRuleTemplate**](ActiveDefenseRuleTemplate.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.client_active_defense_rule_provider_data import ClientActiveDefenseRuleProviderData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientActiveDefenseRuleProviderData from a JSON string
client_active_defense_rule_provider_data_instance = ClientActiveDefenseRuleProviderData.from_json(json)
# print the JSON string representation of the object
print(ClientActiveDefenseRuleProviderData.to_json())

# convert the object into a dict
client_active_defense_rule_provider_data_dict = client_active_defense_rule_provider_data_instance.to_dict()
# create an instance of ClientActiveDefenseRuleProviderData from a dict
client_active_defense_rule_provider_data_from_dict = ClientActiveDefenseRuleProviderData.from_dict(client_active_defense_rule_provider_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


