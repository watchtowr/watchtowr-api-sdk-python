# PaginatedClientCompromisedEndpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientCompromisedEndpoint]**](ClientCompromisedEndpoint.md) | List of compromised endpoints | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.paginated_client_compromised_endpoint import PaginatedClientCompromisedEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClientCompromisedEndpoint from a JSON string
paginated_client_compromised_endpoint_instance = PaginatedClientCompromisedEndpoint.from_json(json)
# print the JSON string representation of the object
print(PaginatedClientCompromisedEndpoint.to_json())

# convert the object into a dict
paginated_client_compromised_endpoint_dict = paginated_client_compromised_endpoint_instance.to_dict()
# create an instance of PaginatedClientCompromisedEndpoint from a dict
paginated_client_compromised_endpoint_from_dict = PaginatedClientCompromisedEndpoint.from_dict(paginated_client_compromised_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


