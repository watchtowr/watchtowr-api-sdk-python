# KillSwitchDisabledError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Error message | 
**error** | **str** | Error code | 
**status_code** | **float** | HTTP status code | 

## Example

```python
from openapi_client.models.kill_switch_disabled_error import KillSwitchDisabledError

# TODO update the JSON string below
json = "{}"
# create an instance of KillSwitchDisabledError from a JSON string
kill_switch_disabled_error_instance = KillSwitchDisabledError.from_json(json)
# print the JSON string representation of the object
print(KillSwitchDisabledError.to_json())

# convert the object into a dict
kill_switch_disabled_error_dict = kill_switch_disabled_error_instance.to_dict()
# create an instance of KillSwitchDisabledError from a dict
kill_switch_disabled_error_from_dict = KillSwitchDisabledError.from_dict(kill_switch_disabled_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


