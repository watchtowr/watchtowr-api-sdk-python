# ClientCompromisedEndpointHarvestedCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Harvested credential ID | 
**type** | **str** | Credential type | 
**url** | **str** | URL associated with the credential | 
**username** | **str** | Username | 
**compromised_endpoint_id** | **int** | Compromised endpoint ID | 
**created_at** | **str** | Creation timestamp | 
**updated_at** | **str** | Last update timestamp | 

## Example

```python
from watchtowr_api_sdk.models.client_compromised_endpoint_harvested_credential import ClientCompromisedEndpointHarvestedCredential

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCompromisedEndpointHarvestedCredential from a JSON string
client_compromised_endpoint_harvested_credential_instance = ClientCompromisedEndpointHarvestedCredential.from_json(json)
# print the JSON string representation of the object
print(ClientCompromisedEndpointHarvestedCredential.to_json())

# convert the object into a dict
client_compromised_endpoint_harvested_credential_dict = client_compromised_endpoint_harvested_credential_instance.to_dict()
# create an instance of ClientCompromisedEndpointHarvestedCredential from a dict
client_compromised_endpoint_harvested_credential_from_dict = ClientCompromisedEndpointHarvestedCredential.from_dict(client_compromised_endpoint_harvested_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


