# WhitelistIpListData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[WhitelistIpData]**](WhitelistIpData.md) | List of whitelisted IPs | 

## Example

```python
from watchtowr_api_sdk.models.whitelist_ip_list_data import WhitelistIpListData

# TODO update the JSON string below
json = "{}"
# create an instance of WhitelistIpListData from a JSON string
whitelist_ip_list_data_instance = WhitelistIpListData.from_json(json)
# print the JSON string representation of the object
print(WhitelistIpListData.to_json())

# convert the object into a dict
whitelist_ip_list_data_dict = whitelist_ip_list_data_instance.to_dict()
# create an instance of WhitelistIpListData from a dict
whitelist_ip_list_data_from_dict = WhitelistIpListData.from_dict(whitelist_ip_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


