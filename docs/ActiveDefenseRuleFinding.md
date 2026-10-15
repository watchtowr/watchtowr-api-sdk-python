# ActiveDefenseRuleFinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Finding ID. | 
**active_defense_provider** | **str** | Active Defense provider associated with the finding. | [optional] 

## Example

```python
from watchtowr_api_sdk.models.active_defense_rule_finding import ActiveDefenseRuleFinding

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDefenseRuleFinding from a JSON string
active_defense_rule_finding_instance = ActiveDefenseRuleFinding.from_json(json)
# print the JSON string representation of the object
print(ActiveDefenseRuleFinding.to_json())

# convert the object into a dict
active_defense_rule_finding_dict = active_defense_rule_finding_instance.to_dict()
# create an instance of ActiveDefenseRuleFinding from a dict
active_defense_rule_finding_from_dict = ActiveDefenseRuleFinding.from_dict(active_defense_rule_finding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


