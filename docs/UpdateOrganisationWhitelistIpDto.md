# UpdateOrganisationWhitelistIpDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | IP address ID | 
**ip** | **str** | IP address or CIDR range to whitelist | 
**description** | **str** | Description of the IP address | [optional] 

## Example

```python
from watchtowr_api_sdk.models.update_organisation_whitelist_ip_dto import UpdateOrganisationWhitelistIpDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrganisationWhitelistIpDto from a JSON string
update_organisation_whitelist_ip_dto_instance = UpdateOrganisationWhitelistIpDto.from_json(json)
# print the JSON string representation of the object
print(UpdateOrganisationWhitelistIpDto.to_json())

# convert the object into a dict
update_organisation_whitelist_ip_dto_dict = update_organisation_whitelist_ip_dto_instance.to_dict()
# create an instance of UpdateOrganisationWhitelistIpDto from a dict
update_organisation_whitelist_ip_dto_from_dict = UpdateOrganisationWhitelistIpDto.from_dict(update_organisation_whitelist_ip_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


