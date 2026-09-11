# ActiveDefenseWafRuleCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**positive_match** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **List[str]** |  | [optional] 
**value_wildcard** | **bool** |  | [optional] 

## Example

```python
from watchtowr_api_sdk.models.active_defense_waf_rule_condition import ActiveDefenseWafRuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDefenseWafRuleCondition from a JSON string
active_defense_waf_rule_condition_instance = ActiveDefenseWafRuleCondition.from_json(json)
# print the JSON string representation of the object
print(ActiveDefenseWafRuleCondition.to_json())

# convert the object into a dict
active_defense_waf_rule_condition_dict = active_defense_waf_rule_condition_instance.to_dict()
# create an instance of ActiveDefenseWafRuleCondition from a dict
active_defense_waf_rule_condition_from_dict = ActiveDefenseWafRuleCondition.from_dict(active_defense_waf_rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


