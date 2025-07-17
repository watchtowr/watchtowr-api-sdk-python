# HostnameBusinessUnitIDsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_unit_ids** | **List[str]** | List of business unit IDs to assign the asset to. | 
**cascade_subdomain** | **bool** | Cascade business units to domain&#39;s subdomains | 
**cascade_ip** | **bool** | Cascade business units to domain&#39;s ipaddresses | 

## Example

```python
from openapi_client.models.hostname_business_unit_ids_dto import HostnameBusinessUnitIDsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of HostnameBusinessUnitIDsDTO from a JSON string
hostname_business_unit_ids_dto_instance = HostnameBusinessUnitIDsDTO.from_json(json)
# print the JSON string representation of the object
print(HostnameBusinessUnitIDsDTO.to_json())

# convert the object into a dict
hostname_business_unit_ids_dto_dict = hostname_business_unit_ids_dto_instance.to_dict()
# create an instance of HostnameBusinessUnitIDsDTO from a dict
hostname_business_unit_ids_dto_from_dict = HostnameBusinessUnitIDsDTO.from_dict(hostname_business_unit_ids_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


