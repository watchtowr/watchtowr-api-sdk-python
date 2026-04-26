# ActiveDefenseRuleTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**content** | **Dict[str, object]** | Provider-specific rule content (shape varies by provider). | 

## Example

```python
from watchtowr_api_sdk.models.active_defense_rule_template import ActiveDefenseRuleTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDefenseRuleTemplate from a JSON string
active_defense_rule_template_instance = ActiveDefenseRuleTemplate.from_json(json)
# print the JSON string representation of the object
print(ActiveDefenseRuleTemplate.to_json())

# convert the object into a dict
active_defense_rule_template_dict = active_defense_rule_template_instance.to_dict()
# create an instance of ActiveDefenseRuleTemplate from a dict
active_defense_rule_template_from_dict = ActiveDefenseRuleTemplate.from_dict(active_defense_rule_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


