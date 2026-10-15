# ClientCredentialsLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Credential attempt log ID | 
**technology** | **str** | Technology used | 
**raw_asset** | **str** | Raw asset string | 
**status** | **str** | Attempt status | 
**attempted_at** | **str** | Date and time when the attempt was made | 
**source** | **str** | Source of the credential attempt | 
**credentials** | [**ClientCredentialsLogCredentials**](ClientCredentialsLogCredentials.md) | Credentials used in the attempt | 
**affected_asset** | [**ClientCredentialsLogAffectedAsset**](ClientCredentialsLogAffectedAsset.md) | Affected asset information | 
**finding_id** | **int** | Finding ID if associated | 
**created_at** | **str** | Creation date | 
**source_metadata** | **object** | Source metadata containing additional contextual information about the credential attempt | 

## Example

```python
from watchtowr_api_sdk.models.client_credentials_log import ClientCredentialsLog

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCredentialsLog from a JSON string
client_credentials_log_instance = ClientCredentialsLog.from_json(json)
# print the JSON string representation of the object
print(ClientCredentialsLog.to_json())

# convert the object into a dict
client_credentials_log_dict = client_credentials_log_instance.to_dict()
# create an instance of ClientCredentialsLog from a dict
client_credentials_log_from_dict = ClientCredentialsLog.from_dict(client_credentials_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


