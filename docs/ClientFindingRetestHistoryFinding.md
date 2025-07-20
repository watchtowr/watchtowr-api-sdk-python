# ClientFindingRetestHistoryFinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Finding ID | 
**title** | **str** | Finding title | 
**severity** | **str** | Finding severity | 
**status** | **str** | Finding status | 

## Example

```python
from watchtowr_api_sdk.models.client_finding_retest_history_finding import ClientFindingRetestHistoryFinding

# TODO update the JSON string below
json = "{}"
# create an instance of ClientFindingRetestHistoryFinding from a JSON string
client_finding_retest_history_finding_instance = ClientFindingRetestHistoryFinding.from_json(json)
# print the JSON string representation of the object
print(ClientFindingRetestHistoryFinding.to_json())

# convert the object into a dict
client_finding_retest_history_finding_dict = client_finding_retest_history_finding_instance.to_dict()
# create an instance of ClientFindingRetestHistoryFinding from a dict
client_finding_retest_history_finding_from_dict = ClientFindingRetestHistoryFinding.from_dict(client_finding_retest_history_finding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


