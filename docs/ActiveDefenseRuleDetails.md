# ActiveDefenseRuleDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**zero_day** | **bool** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**rules** | [**List[ActiveDefenseRuleTemplate]**](ActiveDefenseRuleTemplate.md) |  | 
**vulnerability** | [**ActiveDefenseRuleVulnerability**](ActiveDefenseRuleVulnerability.md) |  | [optional] 
**findings_count** | **int** | Count of confirmed open findings against the rule&#39;s vulnerability. Scoped to the requesting user&#39;s business units and the organization&#39;s finding impact threshold. | 
**affected_kb_entry_ids** | **List[int]** | KB entry IDs covered by this rule that have confirmed open findings, scoped to the requesting user&#39;s business units. | 
**findings** | [**List[ActiveDefenseRuleFinding]**](ActiveDefenseRuleFinding.md) | Confirmed open findings against the rule&#39;s vulnerability, scoped the same way as findingsCount. Empty when there are none. | 

## Example

```python
from watchtowr_api_sdk.models.active_defense_rule_details import ActiveDefenseRuleDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDefenseRuleDetails from a JSON string
active_defense_rule_details_instance = ActiveDefenseRuleDetails.from_json(json)
# print the JSON string representation of the object
print(ActiveDefenseRuleDetails.to_json())

# convert the object into a dict
active_defense_rule_details_dict = active_defense_rule_details_instance.to_dict()
# create an instance of ActiveDefenseRuleDetails from a dict
active_defense_rule_details_from_dict = ActiveDefenseRuleDetails.from_dict(active_defense_rule_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


