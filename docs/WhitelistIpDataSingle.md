# WhitelistIpDataSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**WhitelistIpData**](WhitelistIpData.md) | Whitelisted IP details | 

## Example

```python
from watchtowr_api_sdk.models.whitelist_ip_data_single import WhitelistIpDataSingle

# TODO update the JSON string below
json = "{}"
# create an instance of WhitelistIpDataSingle from a JSON string
whitelist_ip_data_single_instance = WhitelistIpDataSingle.from_json(json)
# print the JSON string representation of the object
print(WhitelistIpDataSingle.to_json())

# convert the object into a dict
whitelist_ip_data_single_dict = whitelist_ip_data_single_instance.to_dict()
# create an instance of WhitelistIpDataSingle from a dict
whitelist_ip_data_single_from_dict = WhitelistIpDataSingle.from_dict(whitelist_ip_data_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


