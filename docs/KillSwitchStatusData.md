# KillSwitchStatusData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**KillSwitchStatusResponse**](KillSwitchStatusResponse.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.kill_switch_status_data import KillSwitchStatusData

# TODO update the JSON string below
json = "{}"
# create an instance of KillSwitchStatusData from a JSON string
kill_switch_status_data_instance = KillSwitchStatusData.from_json(json)
# print the JSON string representation of the object
print(KillSwitchStatusData.to_json())

# convert the object into a dict
kill_switch_status_data_dict = kill_switch_status_data_instance.to_dict()
# create an instance of KillSwitchStatusData from a dict
kill_switch_status_data_from_dict = KillSwitchStatusData.from_dict(kill_switch_status_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


