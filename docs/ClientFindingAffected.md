# ClientFindingAffected


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** | The affected asset object. Shape varies by asset type (domain, subdomain, ip, port, etc.). | [optional] 

## Example

```python
from watchtowr_api_sdk.models.client_finding_affected import ClientFindingAffected

# TODO update the JSON string below
json = "{}"
# create an instance of ClientFindingAffected from a JSON string
client_finding_affected_instance = ClientFindingAffected.from_json(json)
# print the JSON string representation of the object
print(ClientFindingAffected.to_json())

# convert the object into a dict
client_finding_affected_dict = client_finding_affected_instance.to_dict()
# create an instance of ClientFindingAffected from a dict
client_finding_affected_from_dict = ClientFindingAffected.from_dict(client_finding_affected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


