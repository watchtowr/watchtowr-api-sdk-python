# LatestExecutedHuntDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Hunt identifier | 
**title** | **str** | Hunt title | 
**status** | **str** | Hunt status | 
**total_findings** | **float** | Number of findings discovered | 
**total_assets** | **float** | Number of assets affected | 
**need_investigation** | **bool** | Whether manual investigation is required | 
**request_type** | **str** | Type of hunt request | 
**resolved_status** | **bool** | Whether the hunt has been resolved | 
**acknowledgement** | [**HuntAcknowledgementDto**](HuntAcknowledgementDto.md) | Hunt acknowledgement data | 
**threat_actors** | [**List[ThreatActorDto]**](ThreatActorDto.md) | Associated threat actors | 

## Example

```python
from watchtowr_api_sdk.models.latest_executed_hunt_dto import LatestExecutedHuntDto

# TODO update the JSON string below
json = "{}"
# create an instance of LatestExecutedHuntDto from a JSON string
latest_executed_hunt_dto_instance = LatestExecutedHuntDto.from_json(json)
# print the JSON string representation of the object
print(LatestExecutedHuntDto.to_json())

# convert the object into a dict
latest_executed_hunt_dto_dict = latest_executed_hunt_dto_instance.to_dict()
# create an instance of LatestExecutedHuntDto from a dict
latest_executed_hunt_dto_from_dict = LatestExecutedHuntDto.from_dict(latest_executed_hunt_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


