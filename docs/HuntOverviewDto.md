# HuntOverviewDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_hunts_executed** | **float** | Total number of rapid reaction hunts executed | 
**total_unresolved_hunts** | **float** | Total number of unresolved hunts | 
**latest_executed_hunts** | [**List[LatestExecutedHuntDto]**](LatestExecutedHuntDto.md) | Array of latest executed hunts | 

## Example

```python
from openapi_client.models.hunt_overview_dto import HuntOverviewDto

# TODO update the JSON string below
json = "{}"
# create an instance of HuntOverviewDto from a JSON string
hunt_overview_dto_instance = HuntOverviewDto.from_json(json)
# print the JSON string representation of the object
print(HuntOverviewDto.to_json())

# convert the object into a dict
hunt_overview_dto_dict = hunt_overview_dto_instance.to_dict()
# create an instance of HuntOverviewDto from a dict
hunt_overview_dto_from_dict = HuntOverviewDto.from_dict(hunt_overview_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


