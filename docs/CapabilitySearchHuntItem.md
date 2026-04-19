# CapabilitySearchHuntItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | ID | 
**type** | **str** | Type | 
**created_at** | **datetime** | Created at | 
**updated_at** | **datetime** | Updated at | 
**total_findings** | **float** | Total findings related to this hunt | 
**total_assets** | **float** | Total assets related to this hunt | 
**hunt_request_type** | **str** | Hunt request type | 
**rapid_exposure_mechanism** | **str** | Rapid exposure mechanism | [optional] 
**title** | **str** | Title | 
**status** | **str** | Status | 
**cve_ids** | **List[str]** | CVE IDs associated with this hunt | 

## Example

```python
from watchtowr_api_sdk.models.capability_search_hunt_item import CapabilitySearchHuntItem

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilitySearchHuntItem from a JSON string
capability_search_hunt_item_instance = CapabilitySearchHuntItem.from_json(json)
# print the JSON string representation of the object
print(CapabilitySearchHuntItem.to_json())

# convert the object into a dict
capability_search_hunt_item_dict = capability_search_hunt_item_instance.to_dict()
# create an instance of CapabilitySearchHuntItem from a dict
capability_search_hunt_item_from_dict = CapabilitySearchHuntItem.from_dict(capability_search_hunt_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


