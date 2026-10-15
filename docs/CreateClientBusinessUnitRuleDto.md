# CreateClientBusinessUnitRuleDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Rule name | 
**type** | **str** | Rule type | 
**keyword_matcher** | **str** | Keyword for matching assets (required when type is keyword). Supports wildcard patterns: %.sg, %abc%, %abc.com, abc.com. Wildcards can be defined using %. | [optional] 
**keyword_rule_type** | **str** | Keyword rule type (optional, defaults to HOSTNAME when keyword_matcher is provided). HOSTNAME: matches domain/subdomain names. CNAME: matches CNAME DNS record values. TLS_SSL: matches TLS/SSL certificate subject names. CNAME and TLS_SSL rules do not cascade to subdomains (cascade_subdomain is ignored). | [optional] 
**country_code** | **str** | Geographical location 2-letter country code (ISO 3166-1 alpha-2) for matching IPs (required when type is country). Examples: SG, US, GB, AU | [optional] 
**integrations** | [**List[ClientIntegrationItemDto]**](ClientIntegrationItemDto.md) | List of integrations for matching cloud assets (required when type is integration) | [optional] 
**cascade_subdomain** | **bool** | Whether to cascade rule to subdomains. Not supported for CNAME and TLS_SSL keyword rules: for these rule types the value is ignored and the rule is always created with cascade_subdomain set to false. To cover subdomains, create a HOSTNAME rule on the same pattern. | [optional] [default to True]
**cascade_ip** | **bool** | Whether to cascade rule to IPs | [optional] [default to True]
**include_all_integrations** | **bool** | Whether to include all integrations | [optional] [default to False]

## Example

```python
from watchtowr_api_sdk.models.create_client_business_unit_rule_dto import CreateClientBusinessUnitRuleDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClientBusinessUnitRuleDto from a JSON string
create_client_business_unit_rule_dto_instance = CreateClientBusinessUnitRuleDto.from_json(json)
# print the JSON string representation of the object
print(CreateClientBusinessUnitRuleDto.to_json())

# convert the object into a dict
create_client_business_unit_rule_dto_dict = create_client_business_unit_rule_dto_instance.to_dict()
# create an instance of CreateClientBusinessUnitRuleDto from a dict
create_client_business_unit_rule_dto_from_dict = CreateClientBusinessUnitRuleDto.from_dict(create_client_business_unit_rule_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


