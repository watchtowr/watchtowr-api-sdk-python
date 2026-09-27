# AssetCriticalityAlreadySetConflictErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**status_code** | **float** |  | 
**error** | **str** |  | 

## Example

```python
from watchtowr_api_sdk.models.asset_criticality_already_set_conflict_error_response import AssetCriticalityAlreadySetConflictErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssetCriticalityAlreadySetConflictErrorResponse from a JSON string
asset_criticality_already_set_conflict_error_response_instance = AssetCriticalityAlreadySetConflictErrorResponse.from_json(json)
# print the JSON string representation of the object
print(AssetCriticalityAlreadySetConflictErrorResponse.to_json())

# convert the object into a dict
asset_criticality_already_set_conflict_error_response_dict = asset_criticality_already_set_conflict_error_response_instance.to_dict()
# create an instance of AssetCriticalityAlreadySetConflictErrorResponse from a dict
asset_criticality_already_set_conflict_error_response_from_dict = AssetCriticalityAlreadySetConflictErrorResponse.from_dict(asset_criticality_already_set_conflict_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


