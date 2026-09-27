# ActiveDefenseWafRuleCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Condition type, where the provider uses one. | [optional] 
**category** | **str** | Category (e.g. huawei, imperva). | [optional] 
**contents** | **List[str]** | Match contents. | [optional] 
**logic_operation** | **str** | Logic operation joining contents. | [optional] 
**key** | **str** | Match key. | [optional] 
**op_value** | **str** | Comparison operator. | [optional] 
**values** | [**ActiveDefenseWafRuleConditionValues**](ActiveDefenseWafRuleConditionValues.md) |  | [optional] 
**group_operator** | **str** | Operator joining a nested condition group. | [optional] 
**positive_match** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **List[str]** |  | [optional] 
**value_wildcard** | **bool** |  | [optional] 
**sub_key** | **str** | Secondary match key (akamai). | [optional] 
**index** | **str** | Condition position within its group. | [optional] 
**conditions** | **List[Dict[str, object]]** | Nested condition group — same shape as this object, one level deeper. | [optional] 

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


