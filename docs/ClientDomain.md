# ClientDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discovery_reason** | **str** |  | [optional] 
**type** | **str** |  | 
**source** | **str** |  | 
**status** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**business_units** | [**List[ClientBusinessUnit]**](ClientBusinessUnit.md) |  | 
**live** | **bool** |  | 
**whois_data** | [**List[WhoisData]**](WhoisData.md) | WHOIS data for the domain | [optional] 
**dns_records** | [**List[ClientAssetDnsRecord]**](ClientAssetDnsRecord.md) | DNS records for the domain. In list responses, always present: an empty array by default, populated with up to 5 records per asset when &#x60;includeDnsRecords&#x3D;true&#x60;. Always populated on the detail endpoints (&#x60;GET /assets/domain/show/{id}&#x60; and &#x60;GET /assets/domain/show/{id}/dns-records&#x60;). Not included in finding &#x60;affected&#x60; objects. | [optional] 
**metadata** | **object** | Cloud/IaaS integration metadata where available; defaults to an empty object. | 
**custom_properties** | [**List[ClientCustomProperty]**](ClientCustomProperty.md) |  | 
**criticality** | **str** |  | [optional] 
**infrastructure** | [**Infrastructure**](Infrastructure.md) |  | [optional] 
**engine_settings** | [**ClientEngineSettings**](ClientEngineSettings.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.client_domain import ClientDomain

# TODO update the JSON string below
json = "{}"
# create an instance of ClientDomain from a JSON string
client_domain_instance = ClientDomain.from_json(json)
# print the JSON string representation of the object
print(ClientDomain.to_json())

# convert the object into a dict
client_domain_dict = client_domain_instance.to_dict()
# create an instance of ClientDomain from a dict
client_domain_from_dict = ClientDomain.from_dict(client_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


