# CreateOrganisationWhitelistIpDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | IP address or CIDR range to whitelist | 
**description** | **str** | Description of the IP address | [optional] 

## Example

```python
from watchtowr_api_sdk.models.create_organisation_whitelist_ip_dto import CreateOrganisationWhitelistIpDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganisationWhitelistIpDto from a JSON string
create_organisation_whitelist_ip_dto_instance = CreateOrganisationWhitelistIpDto.from_json(json)
# print the JSON string representation of the object
print(CreateOrganisationWhitelistIpDto.to_json())

# convert the object into a dict
create_organisation_whitelist_ip_dto_dict = create_organisation_whitelist_ip_dto_instance.to_dict()
# create an instance of CreateOrganisationWhitelistIpDto from a dict
create_organisation_whitelist_ip_dto_from_dict = CreateOrganisationWhitelistIpDto.from_dict(create_organisation_whitelist_ip_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


