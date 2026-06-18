# ClientSeedDataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Descriptive title for the new asset | 
**type** | **str** | Asset Type for the new asset. Valid asset types are: [domain, subdomain, ip, ipRange, repository, cloudStorage, container, mobileApp, saasPlatform, apiDocumentation, packageManager] | 
**value** | **str** | Value for the asset to be added. | 
**values** | [**IpRangeValues**](IpRangeValues.md) | Values object for ipRange asset type. Must contain both cidr and asn fields. Required when type is ipRange. | [optional] 

## Example

```python
from watchtowr_api_sdk.models.client_seed_data_dto import ClientSeedDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of ClientSeedDataDto from a JSON string
client_seed_data_dto_instance = ClientSeedDataDto.from_json(json)
# print the JSON string representation of the object
print(ClientSeedDataDto.to_json())

# convert the object into a dict
client_seed_data_dto_dict = client_seed_data_dto_instance.to_dict()
# create an instance of ClientSeedDataDto from a dict
client_seed_data_dto_from_dict = ClientSeedDataDto.from_dict(client_seed_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


