# ClientIp


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
**country** | **str** |  | 
**live** | **bool** |  | 
**dns_records** | [**ClientIpDetailDnsRecords**](ClientIpDetailDnsRecords.md) | DNS records for the IP (owned PTR + pointing-at A records). In list responses, included only when &#x60;includeDnsRecords&#x3D;true&#x60; (capped at 5 each per IP). Always populated on the detail endpoints (&#x60;GET /assets/ip/show/{id}&#x60; and &#x60;GET /assets/ip/show/{id}/dns-records&#x60;). Not included in finding &#x60;affected&#x60; objects. | [optional] 
**metadata** | **object** | Cloud/IaaS integration metadata where available; defaults to an empty object. | 
**custom_properties** | [**List[ClientCustomProperty]**](ClientCustomProperty.md) |  | 
**criticality** | **str** |  | [optional] 
**infrastructure** | [**Infrastructure**](Infrastructure.md) |  | [optional] 
**engine_settings** | [**ClientEngineSettings**](ClientEngineSettings.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.client_ip import ClientIp

# TODO update the JSON string below
json = "{}"
# create an instance of ClientIp from a JSON string
client_ip_instance = ClientIp.from_json(json)
# print the JSON string representation of the object
print(ClientIp.to_json())

# convert the object into a dict
client_ip_dict = client_ip_instance.to_dict()
# create an instance of ClientIp from a dict
client_ip_from_dict = ClientIp.from_dict(client_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


