# ClientActiveDefenseRuleData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ActiveDefenseRuleDetails**](ActiveDefenseRuleDetails.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.client_active_defense_rule_data import ClientActiveDefenseRuleData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientActiveDefenseRuleData from a JSON string
client_active_defense_rule_data_instance = ClientActiveDefenseRuleData.from_json(json)
# print the JSON string representation of the object
print(ClientActiveDefenseRuleData.to_json())

# convert the object into a dict
client_active_defense_rule_data_dict = client_active_defense_rule_data_instance.to_dict()
# create an instance of ClientActiveDefenseRuleData from a dict
client_active_defense_rule_data_from_dict = ClientActiveDefenseRuleData.from_dict(client_active_defense_rule_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


