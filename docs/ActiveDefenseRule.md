# ActiveDefenseRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**rule_name** | **str** |  | 
**cve_id** | **str** |  | [optional] 
**wt_id** | **float** |  | [optional] 
**type** | **str** |  | [optional] 
**kev_status** | [**ActiveDefenseRuleKevStatus**](ActiveDefenseRuleKevStatus.md) |  | 
**zero_day** | **bool** |  | 
**providers** | **List[str]** |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 

## Example

```python
from watchtowr_api_sdk.models.active_defense_rule import ActiveDefenseRule

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDefenseRule from a JSON string
active_defense_rule_instance = ActiveDefenseRule.from_json(json)
# print the JSON string representation of the object
print(ActiveDefenseRule.to_json())

# convert the object into a dict
active_defense_rule_dict = active_defense_rule_instance.to_dict()
# create an instance of ActiveDefenseRule from a dict
active_defense_rule_from_dict = ActiveDefenseRule.from_dict(active_defense_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


