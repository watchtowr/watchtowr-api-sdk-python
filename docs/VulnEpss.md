# VulnEpss


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **float** |  | [optional] 
**percentile** | **float** |  | [optional] 
**epss_score_level** | **str** |  | [optional] 

## Example

```python
from watchtowr_api_sdk.models.vuln_epss import VulnEpss

# TODO update the JSON string below
json = "{}"
# create an instance of VulnEpss from a JSON string
vuln_epss_instance = VulnEpss.from_json(json)
# print the JSON string representation of the object
print(VulnEpss.to_json())

# convert the object into a dict
vuln_epss_dict = vuln_epss_instance.to_dict()
# create an instance of VulnEpss from a dict
vuln_epss_from_dict = VulnEpss.from_dict(vuln_epss_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


