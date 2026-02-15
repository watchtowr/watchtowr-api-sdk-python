# PaginatedTechnologyStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TechnologyStatistic]**](TechnologyStatistic.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.paginated_technology_statistics import PaginatedTechnologyStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTechnologyStatistics from a JSON string
paginated_technology_statistics_instance = PaginatedTechnologyStatistics.from_json(json)
# print the JSON string representation of the object
print(PaginatedTechnologyStatistics.to_json())

# convert the object into a dict
paginated_technology_statistics_dict = paginated_technology_statistics_instance.to_dict()
# create an instance of PaginatedTechnologyStatistics from a dict
paginated_technology_statistics_from_dict = PaginatedTechnologyStatistics.from_dict(paginated_technology_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


