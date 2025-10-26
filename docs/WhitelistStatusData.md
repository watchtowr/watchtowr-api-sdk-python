# WhitelistStatusData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Current whitelisting status | 

## Example

```python
from watchtowr_api_sdk.models.whitelist_status_data import WhitelistStatusData

# TODO update the JSON string below
json = "{}"
# create an instance of WhitelistStatusData from a JSON string
whitelist_status_data_instance = WhitelistStatusData.from_json(json)
# print the JSON string representation of the object
print(WhitelistStatusData.to_json())

# convert the object into a dict
whitelist_status_data_dict = whitelist_status_data_instance.to_dict()
# create an instance of WhitelistStatusData from a dict
whitelist_status_data_from_dict = WhitelistStatusData.from_dict(whitelist_status_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


