# ClientSubdomain


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
**dns_records** | [**List[ClientAssetDnsRecord]**](ClientAssetDnsRecord.md) | DNS records for the subdomain. In list responses, included only when &#x60;includeDnsRecords&#x3D;true&#x60; (capped at 5 per asset). Always populated on the detail endpoints (&#x60;GET /assets/subdomain/show/{id}&#x60; and &#x60;GET /assets/subdomain/show/{id}/dns-records&#x60;). Not included in finding &#x60;affected&#x60; objects. | [optional] 
**metadata** | **object** | Cloud/IaaS integration metadata where available; defaults to an empty object. | 
**custom_properties** | [**List[ClientCustomProperty]**](ClientCustomProperty.md) |  | 
**criticality** | **str** |  | [optional] 
**infrastructure** | [**Infrastructure**](Infrastructure.md) |  | [optional] 
**engine_settings** | [**ClientEngineSettings**](ClientEngineSettings.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.client_subdomain import ClientSubdomain

# TODO update the JSON string below
json = "{}"
# create an instance of ClientSubdomain from a JSON string
client_subdomain_instance = ClientSubdomain.from_json(json)
# print the JSON string representation of the object
print(ClientSubdomain.to_json())

# convert the object into a dict
client_subdomain_dict = client_subdomain_instance.to_dict()
# create an instance of ClientSubdomain from a dict
client_subdomain_from_dict = ClientSubdomain.from_dict(client_subdomain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


