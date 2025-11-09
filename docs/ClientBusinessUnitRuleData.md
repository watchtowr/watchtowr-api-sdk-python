# ClientBusinessUnitRuleData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientBusinessUnitRuleDetail**](ClientBusinessUnitRuleDetail.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.client_business_unit_rule_data import ClientBusinessUnitRuleData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientBusinessUnitRuleData from a JSON string
client_business_unit_rule_data_instance = ClientBusinessUnitRuleData.from_json(json)
# print the JSON string representation of the object
print(ClientBusinessUnitRuleData.to_json())

# convert the object into a dict
client_business_unit_rule_data_dict = client_business_unit_rule_data_instance.to_dict()
# create an instance of ClientBusinessUnitRuleData from a dict
client_business_unit_rule_data_from_dict = ClientBusinessUnitRuleData.from_dict(client_business_unit_rule_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


