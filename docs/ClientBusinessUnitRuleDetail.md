# ClientBusinessUnitRuleDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | ID | 
**name** | **str** | Rule name | 
**keyword_matcher** | **str** | Keyword for matching assets. Supports wildcard patterns: %.sg, %abc%, %abc.com, abc.com. Wildcards can be defined using %. | [optional] 
**keyword_rule_type** | **str** | Keyword rule type. HOSTNAME: matches domain/subdomain names (default). CNAME: matches CNAME DNS record values. TLS_SSL: matches TLS/SSL certificate subject names. | [optional] 
**country** | **str** | Geographical location 2-letter country code (ISO 3166-1 alpha-2). Examples: SG, US, GB, AU | [optional] 
**cascade_subdomain** | **bool** | Whether to cascade to subdomains | 
**cascade_ip** | **bool** | Whether to cascade to IPs | 
**integration_type** | **str** | Integration type. Valid values: aws, azure, googlecloud, cloudflare, alibabacloud, prismacloud, prismacloudapigee, huaweicloud, tencentcloud, wiz, servicenowcmdb, akamaiedge, armiscentrix, qualysvmdr, tenable | [optional] 
**integration_id** | **float** | Integration ID | [optional] 
**include_all_integrations** | **bool** | Whether to include all integrations | 
**created_at** | **object** | Created At | 

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


