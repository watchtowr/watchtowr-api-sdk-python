# ClientFinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**title** | **str** |  | 
**platform_url** | **str** | Link to this finding in the watchTowr platform. | 
**description** | **str** |  | 
**impact** | **str** |  | 
**finding_impact** | **str** |  | 
**tags** | [**List[ClientFindingImpactTag]**](ClientFindingImpactTag.md) |  | 
**evidence** | **str** |  | 
**recommendation** | **str** |  | 
**severity** | **str** |  | 
**cvssv3_score** | **float** |  | 
**cvssv3_metrics** | **str** |  | 
**references** | **str** | Finding references from the knowledge base entry, or &#x60;\&quot;No references.\&quot;&#x60; when none exist. | 
**status** | **str** |  | 
**state** | **str** | Different to status, this is about tracking how the finding is being handled | [optional] 
**created_at** | **datetime** |  | 
**affected** | [**ClientFindingAffected**](ClientFindingAffected.md) | Affected asset envelope. The asset object is nested under &#x60;data&#x60;; shape varies by asset type. | 
**cve_id** | **str** |  | [optional] 
**epss_score** | **float** |  | [optional] 
**retest** | [**Retest**](Retest.md) |  | [optional] 
**retest_history** | [**List[FindingRetestResponseDto]**](FindingRetestResponseDto.md) |  | [optional] 
**assigned_user** | [**ClientFindingAssignee**](ClientFindingAssignee.md) |  | [optional] 
**last_seen** | **datetime** |  | [optional] 
**last_status_updated_at** | **datetime** |  | 
**age** | **int** |  | [optional] 
**criticality** | **str** |  | [optional] 
**custom_properties** | [**List[ClientCustomProperty]**](ClientCustomProperty.md) |  | 
**detection_rules** | **List[object]** |  | 

## Example

```python
from watchtowr_api_sdk.models.client_finding import ClientFinding

# TODO update the JSON string below
json = "{}"
# create an instance of ClientFinding from a JSON string
client_finding_instance = ClientFinding.from_json(json)
# print the JSON string representation of the object
print(ClientFinding.to_json())

# convert the object into a dict
client_finding_dict = client_finding_instance.to_dict()
# create an instance of ClientFinding from a dict
client_finding_from_dict = ClientFinding.from_dict(client_finding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


