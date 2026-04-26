# VulnCvssV3XMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vector** | **str** |  | [optional] 
**score** | **float** |  | [optional] 
**severity** | **str** |  | [optional] 

## Example

```python
from watchtowr_api_sdk.models.vuln_cvss_v3_x_metrics import VulnCvssV3XMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of VulnCvssV3XMetrics from a JSON string
vuln_cvss_v3_x_metrics_instance = VulnCvssV3XMetrics.from_json(json)
# print the JSON string representation of the object
print(VulnCvssV3XMetrics.to_json())

# convert the object into a dict
vuln_cvss_v3_x_metrics_dict = vuln_cvss_v3_x_metrics_instance.to_dict()
# create an instance of VulnCvssV3XMetrics from a dict
vuln_cvss_v3_x_metrics_from_dict = VulnCvssV3XMetrics.from_dict(vuln_cvss_v3_x_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


