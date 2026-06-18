# FindingStatusesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[List[str]]** | Returns a single-element array containing all finding statuses. | 

## Example

```python
from watchtowr_api_sdk.models.finding_statuses_response import FindingStatusesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindingStatusesResponse from a JSON string
finding_statuses_response_instance = FindingStatusesResponse.from_json(json)
# print the JSON string representation of the object
print(FindingStatusesResponse.to_json())

# convert the object into a dict
finding_statuses_response_dict = finding_statuses_response_instance.to_dict()
# create an instance of FindingStatusesResponse from a dict
finding_statuses_response_from_dict = FindingStatusesResponse.from_dict(finding_statuses_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


