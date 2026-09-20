# ClientCredentialsLogCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Username used in the credential attempt | 
**target_url** | **str** | Target URL for the credential attempt | 

## Example

```python
from watchtowr_api_sdk.models.client_credentials_log_credentials import ClientCredentialsLogCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCredentialsLogCredentials from a JSON string
client_credentials_log_credentials_instance = ClientCredentialsLogCredentials.from_json(json)
# print the JSON string representation of the object
print(ClientCredentialsLogCredentials.to_json())

# convert the object into a dict
client_credentials_log_credentials_dict = client_credentials_log_credentials_instance.to_dict()
# create an instance of ClientCredentialsLogCredentials from a dict
client_credentials_log_credentials_from_dict = ClientCredentialsLogCredentials.from_dict(client_credentials_log_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


