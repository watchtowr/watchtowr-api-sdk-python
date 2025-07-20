# PaginatedClientFindingRetestHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientFindingRetestHistory]**](ClientFindingRetestHistory.md) | List of finding retest history items | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.paginated_client_finding_retest_history import PaginatedClientFindingRetestHistory

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClientFindingRetestHistory from a JSON string
paginated_client_finding_retest_history_instance = PaginatedClientFindingRetestHistory.from_json(json)
# print the JSON string representation of the object
print(PaginatedClientFindingRetestHistory.to_json())

# convert the object into a dict
paginated_client_finding_retest_history_dict = paginated_client_finding_retest_history_instance.to_dict()
# create an instance of PaginatedClientFindingRetestHistory from a dict
paginated_client_finding_retest_history_from_dict = PaginatedClientFindingRetestHistory.from_dict(paginated_client_finding_retest_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


