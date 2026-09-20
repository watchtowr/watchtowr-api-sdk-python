# PaginatedClientCompromisedEndpointHarvestedCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientCompromisedEndpointHarvestedCredential]**](ClientCompromisedEndpointHarvestedCredential.md) | List of harvested credentials | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.paginated_client_compromised_endpoint_harvested_credentials import PaginatedClientCompromisedEndpointHarvestedCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClientCompromisedEndpointHarvestedCredentials from a JSON string
paginated_client_compromised_endpoint_harvested_credentials_instance = PaginatedClientCompromisedEndpointHarvestedCredentials.from_json(json)
# print the JSON string representation of the object
print(PaginatedClientCompromisedEndpointHarvestedCredentials.to_json())

# convert the object into a dict
paginated_client_compromised_endpoint_harvested_credentials_dict = paginated_client_compromised_endpoint_harvested_credentials_instance.to_dict()
# create an instance of PaginatedClientCompromisedEndpointHarvestedCredentials from a dict
paginated_client_compromised_endpoint_harvested_credentials_from_dict = PaginatedClientCompromisedEndpointHarvestedCredentials.from_dict(paginated_client_compromised_endpoint_harvested_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


