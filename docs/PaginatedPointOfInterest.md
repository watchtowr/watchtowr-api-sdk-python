# PaginatedPointOfInterest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PointsOfInterest]**](PointsOfInterest.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.paginated_point_of_interest import PaginatedPointOfInterest

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPointOfInterest from a JSON string
paginated_point_of_interest_instance = PaginatedPointOfInterest.from_json(json)
# print the JSON string representation of the object
print(PaginatedPointOfInterest.to_json())

# convert the object into a dict
paginated_point_of_interest_dict = paginated_point_of_interest_instance.to_dict()
# create an instance of PaginatedPointOfInterest from a dict
paginated_point_of_interest_from_dict = PaginatedPointOfInterest.from_dict(paginated_point_of_interest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


