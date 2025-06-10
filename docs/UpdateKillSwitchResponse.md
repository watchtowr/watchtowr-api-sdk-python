# UpdateKillSwitchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Updated kill switch status | 
**message** | **str** | Success message | 

## Example

```python
from openapi_client.models.update_kill_switch_response import UpdateKillSwitchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateKillSwitchResponse from a JSON string
update_kill_switch_response_instance = UpdateKillSwitchResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateKillSwitchResponse.to_json())

# convert the object into a dict
update_kill_switch_response_dict = update_kill_switch_response_instance.to_dict()
# create an instance of UpdateKillSwitchResponse from a dict
update_kill_switch_response_from_dict = UpdateKillSwitchResponse.from_dict(update_kill_switch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


