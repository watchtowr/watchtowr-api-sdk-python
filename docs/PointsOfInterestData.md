# PointsOfInterestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PointsOfInterest**](PointsOfInterest.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.points_of_interest_data import PointsOfInterestData

# TODO update the JSON string below
json = "{}"
# create an instance of PointsOfInterestData from a JSON string
points_of_interest_data_instance = PointsOfInterestData.from_json(json)
# print the JSON string representation of the object
print(PointsOfInterestData.to_json())

# convert the object into a dict
points_of_interest_data_dict = points_of_interest_data_instance.to_dict()
# create an instance of PointsOfInterestData from a dict
points_of_interest_data_from_dict = PointsOfInterestData.from_dict(points_of_interest_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


