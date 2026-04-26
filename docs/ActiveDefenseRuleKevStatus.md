# ActiveDefenseRuleKevStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cisa** | **bool** |  | 
**vulncheck** | **bool** |  | 
**watchtowr** | **bool** |  | 

## Example

```python
from watchtowr_api_sdk.models.active_defense_rule_kev_status import ActiveDefenseRuleKevStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDefenseRuleKevStatus from a JSON string
active_defense_rule_kev_status_instance = ActiveDefenseRuleKevStatus.from_json(json)
# print the JSON string representation of the object
print(ActiveDefenseRuleKevStatus.to_json())

# convert the object into a dict
active_defense_rule_kev_status_dict = active_defense_rule_kev_status_instance.to_dict()
# create an instance of ActiveDefenseRuleKevStatus from a dict
active_defense_rule_kev_status_from_dict = ActiveDefenseRuleKevStatus.from_dict(active_defense_rule_kev_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


