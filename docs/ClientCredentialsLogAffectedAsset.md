# ClientCredentialsLogAffectedAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Asset ID | 
**name** | **str** | Asset name | 
**type** | **str** | Asset type | 

## Example

```python
from watchtowr_api_sdk.models.client_credentials_log_affected_asset import ClientCredentialsLogAffectedAsset

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCredentialsLogAffectedAsset from a JSON string
client_credentials_log_affected_asset_instance = ClientCredentialsLogAffectedAsset.from_json(json)
# print the JSON string representation of the object
print(ClientCredentialsLogAffectedAsset.to_json())

# convert the object into a dict
client_credentials_log_affected_asset_dict = client_credentials_log_affected_asset_instance.to_dict()
# create an instance of ClientCredentialsLogAffectedAsset from a dict
client_credentials_log_affected_asset_from_dict = ClientCredentialsLogAffectedAsset.from_dict(client_credentials_log_affected_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


