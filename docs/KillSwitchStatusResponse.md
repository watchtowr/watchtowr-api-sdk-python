# KillSwitchStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Current kill switch status | 
**allow_client_control** | **bool** | Whether client kill switch control is allowed | 

## Example

```python
from openapi_client.models.kill_switch_status_response import KillSwitchStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KillSwitchStatusResponse from a JSON string
kill_switch_status_response_instance = KillSwitchStatusResponse.from_json(json)
# print the JSON string representation of the object
print(KillSwitchStatusResponse.to_json())

# convert the object into a dict
kill_switch_status_response_dict = kill_switch_status_response_instance.to_dict()
# create an instance of KillSwitchStatusResponse from a dict
kill_switch_status_response_from_dict = KillSwitchStatusResponse.from_dict(kill_switch_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


