# VulnDetailKev


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cisa_kev_date_added** | **datetime** |  | [optional] 
**vulncheck_kev_date_added** | **datetime** |  | [optional] 
**watchtowr_kev_date_added** | **datetime** |  | [optional] 

## Example

```python
from watchtowr_api_sdk.models.vuln_detail_kev import VulnDetailKev

# TODO update the JSON string below
json = "{}"
# create an instance of VulnDetailKev from a JSON string
vuln_detail_kev_instance = VulnDetailKev.from_json(json)
# print the JSON string representation of the object
print(VulnDetailKev.to_json())

# convert the object into a dict
vuln_detail_kev_dict = vuln_detail_kev_instance.to_dict()
# create an instance of VulnDetailKev from a dict
vuln_detail_kev_from_dict = VulnDetailKev.from_dict(vuln_detail_kev_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


