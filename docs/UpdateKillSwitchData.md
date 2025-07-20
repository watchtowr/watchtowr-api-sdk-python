# UpdateKillSwitchData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UpdateKillSwitchResponse**](UpdateKillSwitchResponse.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.update_kill_switch_data import UpdateKillSwitchData

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateKillSwitchData from a JSON string
update_kill_switch_data_instance = UpdateKillSwitchData.from_json(json)
# print the JSON string representation of the object
print(UpdateKillSwitchData.to_json())

# convert the object into a dict
update_kill_switch_data_dict = update_kill_switch_data_instance.to_dict()
# create an instance of UpdateKillSwitchData from a dict
update_kill_switch_data_from_dict = UpdateKillSwitchData.from_dict(update_kill_switch_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


