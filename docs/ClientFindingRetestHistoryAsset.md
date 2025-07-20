# ClientFindingRetestHistoryAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Asset ID | 
**name** | **str** | Asset name | 
**type** | **str** | Asset type | 

## Example

```python
from watchtowr_api_sdk.models.client_finding_retest_history_asset import ClientFindingRetestHistoryAsset

# TODO update the JSON string below
json = "{}"
# create an instance of ClientFindingRetestHistoryAsset from a JSON string
client_finding_retest_history_asset_instance = ClientFindingRetestHistoryAsset.from_json(json)
# print the JSON string representation of the object
print(ClientFindingRetestHistoryAsset.to_json())

# convert the object into a dict
client_finding_retest_history_asset_dict = client_finding_retest_history_asset_instance.to_dict()
# create an instance of ClientFindingRetestHistoryAsset from a dict
client_finding_retest_history_asset_from_dict = ClientFindingRetestHistoryAsset.from_dict(client_finding_retest_history_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


