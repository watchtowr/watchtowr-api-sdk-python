# ClientFindingRetestHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Retest ID | 
**finding** | [**ClientFindingRetestHistoryFinding**](ClientFindingRetestHistoryFinding.md) | Finding information | 
**asset** | [**ClientFindingRetestHistoryAsset**](ClientFindingRetestHistoryAsset.md) | Affected asset information | 
**triggered_by** | [**ClientFindingRetestHistoryTriggeredBy**](ClientFindingRetestHistoryTriggeredBy.md) | User who triggered the retest | 
**current_retest_status** | **str** | Current retest status | 
**started_at** | **datetime** | Date and time when the retest was started | 
**completed_at** | **object** | Date and time when the retest was completed | 
**updated_at** | **datetime** | Date and time when the retest was last updated | 
**created_at** | **datetime** | Creation date | 

## Example

```python
from watchtowr_api_sdk.models.client_finding_retest_history import ClientFindingRetestHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ClientFindingRetestHistory from a JSON string
client_finding_retest_history_instance = ClientFindingRetestHistory.from_json(json)
# print the JSON string representation of the object
print(ClientFindingRetestHistory.to_json())

# convert the object into a dict
client_finding_retest_history_dict = client_finding_retest_history_instance.to_dict()
# create an instance of ClientFindingRetestHistory from a dict
client_finding_retest_history_from_dict = ClientFindingRetestHistory.from_dict(client_finding_retest_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


