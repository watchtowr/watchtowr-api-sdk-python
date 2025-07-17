# KillSwitchForbiddenError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Error message | 
**error** | **str** | Error code | 
**status_code** | **float** | HTTP status code | 

## Example

```python
from watchtowr_api_sdk.models.kill_switch_forbidden_error import KillSwitchForbiddenError

# TODO update the JSON string below
json = "{}"
# create an instance of KillSwitchForbiddenError from a JSON string
kill_switch_forbidden_error_instance = KillSwitchForbiddenError.from_json(json)
# print the JSON string representation of the object
print(KillSwitchForbiddenError.to_json())

# convert the object into a dict
kill_switch_forbidden_error_dict = kill_switch_forbidden_error_instance.to_dict()
# create an instance of KillSwitchForbiddenError from a dict
kill_switch_forbidden_error_from_dict = KillSwitchForbiddenError.from_dict(kill_switch_forbidden_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


