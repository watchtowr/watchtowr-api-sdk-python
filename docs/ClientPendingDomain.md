# ClientPendingDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Domain ID | 
**status** | **str** | Domain status | 
**name** | **str** | Domain name | 
**source** | **str** | Source that discovered the domain | 
**created_at** | **datetime** | Creation date | 
**whois_data** | [**ClientPendingDomainWhoisData**](ClientPendingDomainWhoisData.md) | WHOIS data for the domain | 

## Example

```python
from watchtowr_api_sdk.models.client_pending_domain import ClientPendingDomain

# TODO update the JSON string below
json = "{}"
# create an instance of ClientPendingDomain from a JSON string
client_pending_domain_instance = ClientPendingDomain.from_json(json)
# print the JSON string representation of the object
print(ClientPendingDomain.to_json())

# convert the object into a dict
client_pending_domain_dict = client_pending_domain_instance.to_dict()
# create an instance of ClientPendingDomain from a dict
client_pending_domain_from_dict = ClientPendingDomain.from_dict(client_pending_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


