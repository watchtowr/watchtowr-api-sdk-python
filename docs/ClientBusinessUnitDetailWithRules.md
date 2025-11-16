# ClientBusinessUnitDetailWithRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | ID | 
**name** | **str** | Name | 
**description** | **str** | Description | 
**type** | **str** | Business unit type | 
**parent_id** | **float** | Parent business unit ID | [optional] 
**user_ids** | **List[float]** | Array of user IDs assigned to this business unit | [optional] 
**created_at** | **object** | Created At | 
**updated_at** | **object** | Updated At | 
**rules** | **object** | Paginated rules for this business unit | 

## Example

```python
from watchtowr_api_sdk.models.client_business_unit_detail_with_rules import ClientBusinessUnitDetailWithRules

# TODO update the JSON string below
json = "{}"
# create an instance of ClientBusinessUnitDetailWithRules from a JSON string
client_business_unit_detail_with_rules_instance = ClientBusinessUnitDetailWithRules.from_json(json)
# print the JSON string representation of the object
print(ClientBusinessUnitDetailWithRules.to_json())

# convert the object into a dict
client_business_unit_detail_with_rules_dict = client_business_unit_detail_with_rules_instance.to_dict()
# create an instance of ClientBusinessUnitDetailWithRules from a dict
client_business_unit_detail_with_rules_from_dict = ClientBusinessUnitDetailWithRules.from_dict(client_business_unit_detail_with_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


