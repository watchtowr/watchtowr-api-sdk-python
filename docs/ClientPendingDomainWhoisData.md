# ClientPendingDomainWhoisData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw** | **str** | Raw WHOIS data | 
**data** | **object** | Formatted WHOIS data | 

## Example

```python
from watchtowr_api_sdk.models.client_pending_domain_whois_data import ClientPendingDomainWhoisData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientPendingDomainWhoisData from a JSON string
client_pending_domain_whois_data_instance = ClientPendingDomainWhoisData.from_json(json)
# print the JSON string representation of the object
print(ClientPendingDomainWhoisData.to_json())

# convert the object into a dict
client_pending_domain_whois_data_dict = client_pending_domain_whois_data_instance.to_dict()
# create an instance of ClientPendingDomainWhoisData from a dict
client_pending_domain_whois_data_from_dict = ClientPendingDomainWhoisData.from_dict(client_pending_domain_whois_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


