# ActiveDefenseWafRuleConditionValues

Match values — some providers emit a single string rather than a list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from watchtowr_api_sdk.models.active_defense_waf_rule_condition_values import ActiveDefenseWafRuleConditionValues

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDefenseWafRuleConditionValues from a JSON string
active_defense_waf_rule_condition_values_instance = ActiveDefenseWafRuleConditionValues.from_json(json)
# print the JSON string representation of the object
print(ActiveDefenseWafRuleConditionValues.to_json())

# convert the object into a dict
active_defense_waf_rule_condition_values_dict = active_defense_waf_rule_condition_values_instance.to_dict()
# create an instance of ActiveDefenseWafRuleConditionValues from a dict
active_defense_waf_rule_condition_values_from_dict = ActiveDefenseWafRuleConditionValues.from_dict(active_defense_waf_rule_condition_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


