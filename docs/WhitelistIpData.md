# WhitelistIpData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | IP address ID | 
**ip** | **str** | IP address or CIDR range | 
**description** | **str** | Description of the IP address | 
**created_at** | **datetime** | Creation timestamp | 
**updated_at** | **datetime** | Last update timestamp | 

## Example

```python
from watchtowr_api_sdk.models.whitelist_ip_data import WhitelistIpData

# TODO update the JSON string below
json = "{}"
# create an instance of WhitelistIpData from a JSON string
whitelist_ip_data_instance = WhitelistIpData.from_json(json)
# print the JSON string representation of the object
print(WhitelistIpData.to_json())

# convert the object into a dict
whitelist_ip_data_dict = whitelist_ip_data_instance.to_dict()
# create an instance of WhitelistIpData from a dict
whitelist_ip_data_from_dict = WhitelistIpData.from_dict(whitelist_ip_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


