# ClientSeedDataAssetLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the resolved asset | 
**type** | **str** | Type of the resolved asset. Matches the asset type values used elsewhere in the API (e.g. domain, subdomain, ip, ipRange, saasPlatform, ...). | 

## Example

```python
from watchtowr_api_sdk.models.client_seed_data_asset_link import ClientSeedDataAssetLink

# TODO update the JSON string below
json = "{}"
# create an instance of ClientSeedDataAssetLink from a JSON string
client_seed_data_asset_link_instance = ClientSeedDataAssetLink.from_json(json)
# print the JSON string representation of the object
print(ClientSeedDataAssetLink.to_json())

# convert the object into a dict
client_seed_data_asset_link_dict = client_seed_data_asset_link_instance.to_dict()
# create an instance of ClientSeedDataAssetLink from a dict
client_seed_data_asset_link_from_dict = ClientSeedDataAssetLink.from_dict(client_seed_data_asset_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


