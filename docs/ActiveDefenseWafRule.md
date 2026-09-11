# ActiveDefenseWafRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | [optional] 
**template** | **str** | Deployable template body (AWS CloudFormation YAML or Azure ARM JSON). | [optional] 
**description** | **str** |  | [optional] 
**expression** | **str** |  | [optional] 
**filter** | **str** |  | [optional] 
**vcl** | **str** |  | [optional] 
**action** | **str** |  | [optional] 
**tag** | **List[str]** |  | [optional] 
**operation** | **str** |  | [optional] 
**structured** | **bool** |  | [optional] 
**conditions** | [**List[ActiveDefenseWafRuleCondition]**](ActiveDefenseWafRuleCondition.md) |  | [optional] 

## Example

```python
from watchtowr_api_sdk.models.active_defense_waf_rule import ActiveDefenseWafRule

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDefenseWafRule from a JSON string
active_defense_waf_rule_instance = ActiveDefenseWafRule.from_json(json)
# print the JSON string representation of the object
print(ActiveDefenseWafRule.to_json())

# convert the object into a dict
active_defense_waf_rule_dict = active_defense_waf_rule_instance.to_dict()
# create an instance of ActiveDefenseWafRule from a dict
active_defense_waf_rule_from_dict = ActiveDefenseWafRule.from_dict(active_defense_waf_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


