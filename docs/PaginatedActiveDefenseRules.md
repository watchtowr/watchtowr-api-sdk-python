# PaginatedActiveDefenseRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ActiveDefenseRule]**](ActiveDefenseRule.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.paginated_active_defense_rules import PaginatedActiveDefenseRules

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedActiveDefenseRules from a JSON string
paginated_active_defense_rules_instance = PaginatedActiveDefenseRules.from_json(json)
# print the JSON string representation of the object
print(PaginatedActiveDefenseRules.to_json())

# convert the object into a dict
paginated_active_defense_rules_dict = paginated_active_defense_rules_instance.to_dict()
# create an instance of PaginatedActiveDefenseRules from a dict
paginated_active_defense_rules_from_dict = PaginatedActiveDefenseRules.from_dict(paginated_active_defense_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


