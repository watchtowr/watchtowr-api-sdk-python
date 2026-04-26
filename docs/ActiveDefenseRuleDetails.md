# ActiveDefenseRuleDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**zero_day** | **bool** |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 
**rules** | [**List[ActiveDefenseRuleTemplate]**](ActiveDefenseRuleTemplate.md) |  | 
**vulnerability** | [**ActiveDefenseRuleVulnerability**](ActiveDefenseRuleVulnerability.md) |  | [optional] 
**findings_count** | **float** | Count of confirmed open findings against the rule&#39;s vulnerability. Scoped to the requesting user&#39;s business units and the organization&#39;s finding impact threshold. | 
**affected_kb_entry_ids** | **List[float]** | KB entry IDs covered by this rule that have confirmed open findings, scoped to the requesting user&#39;s business units. | 

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


