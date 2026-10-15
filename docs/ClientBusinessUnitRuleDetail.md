# ClientBusinessUnitRuleDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | 
**name** | **str** | Rule name | 
**keyword_matcher** | **str** | Keyword for matching assets. Supports wildcard patterns: %.sg, %abc%, %abc.com, abc.com. Wildcards can be defined using %. | [optional] 
**keyword_rule_type** | **str** | Keyword rule type. HOSTNAME: matches domain/subdomain names (default). CNAME: matches CNAME DNS record values. TLS_SSL: matches TLS/SSL certificate subject names. | [optional] 
**country** | **str** | Geographical location 2-letter country code (ISO 3166-1 alpha-2). Examples: SG, US, GB, AU | [optional] 
**cascade_subdomain** | **bool** | Whether to cascade to subdomains. New CNAME and TLS_SSL keyword rules always have false. Older rules of these types can show true. | 
**cascade_ip** | **bool** | Whether to cascade to IPs | 
**integration_type** | **str** | Integration type (deprecated — use integrations[0].integration_type instead) | [optional] 
**integration_id** | **int** | Integration ID (deprecated — use integrations[0].integration_id instead) | [optional] 
**integrations** | [**List[ClientIntegrationItemDto]**](ClientIntegrationItemDto.md) | List of integrations matched by this rule | [optional] 
**include_all_integrations** | **bool** | Whether to include all integrations | 
**created_at** | **datetime** | Created At | 

## Example

```python
from watchtowr_api_sdk.models.client_business_unit_rule_detail import ClientBusinessUnitRuleDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ClientBusinessUnitRuleDetail from a JSON string
client_business_unit_rule_detail_instance = ClientBusinessUnitRuleDetail.from_json(json)
# print the JSON string representation of the object
print(ClientBusinessUnitRuleDetail.to_json())

# convert the object into a dict
client_business_unit_rule_detail_dict = client_business_unit_rule_detail_instance.to_dict()
# create an instance of ClientBusinessUnitRuleDetail from a dict
client_business_unit_rule_detail_from_dict = ClientBusinessUnitRuleDetail.from_dict(client_business_unit_rule_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


