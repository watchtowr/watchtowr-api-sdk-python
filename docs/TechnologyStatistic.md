# TechnologyStatistic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Technology name | 
**count** | **float** | Number of services using this technology | 

## Example

```python
from watchtowr_api_sdk.models.technology_statistic import TechnologyStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of TechnologyStatistic from a JSON string
technology_statistic_instance = TechnologyStatistic.from_json(json)
# print the JSON string representation of the object
print(TechnologyStatistic.to_json())

# convert the object into a dict
technology_statistic_dict = technology_statistic_instance.to_dict()
# create an instance of TechnologyStatistic from a dict
technology_statistic_from_dict = TechnologyStatistic.from_dict(technology_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


