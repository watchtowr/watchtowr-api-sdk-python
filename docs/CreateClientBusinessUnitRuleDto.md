# CreateClientBusinessUnitRuleDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Rule name | 
**type** | **str** | Rule type | 
**keyword_matcher** | **str** | Keyword for matching domains/subdomains (required when type is keyword) | [optional] 
**country_code** | **str** | Geographical location 2-letter country code (ISO 3166-1 alpha-2) for matching IPs (required when type is country). Examples: SG, US, GB, AU | [optional] 
**integration_type** | **str** | Integration type for matching cloud assets (required when type is integration). Valid values: aws, azure, googlecloud, cloudflare, alibabacloud, prismacloud, prismacloudapigee, huaweicloud, tencentcloud, wiz, servicenowcmdb, akamaiedge, armiscentrix, qualysvmdr, tenable | [optional] 
**integration_id** | **float** | Integration ID for matching cloud assets (required when type is integration) | [optional] 
**cascade_subdomain** | **bool** | Whether to cascade rule to subdomains | [optional] [default to True]
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


