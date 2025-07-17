# UpdateKillSwitchRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **bool** | Kill switch value (true to enable, false to disable) | 
**reason** | **str** | Reason for enabling the kill switch (required when enabling) | [optional] 
**request_support** | **bool** | Whether to request support from watchTowr (optional, defaults to false) | [optional] 

## Example

```python
from watchtowr_api_sdk.models.update_kill_switch_request_dto import UpdateKillSwitchRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateKillSwitchRequestDto from a JSON string
update_kill_switch_request_dto_instance = UpdateKillSwitchRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateKillSwitchRequestDto.to_json())

# convert the object into a dict
update_kill_switch_request_dto_dict = update_kill_switch_request_dto_instance.to_dict()
# create an instance of UpdateKillSwitchRequestDto from a dict
update_kill_switch_request_dto_from_dict = UpdateKillSwitchRequestDto.from_dict(update_kill_switch_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


