# MttrMetricsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mttr** | **float** | Mean Time To Remediation in hours | 
**mttrae** | **float** | Mean Time To Remediation After Exploitation in hours | 

## Example

```python
from watchtowr_api_sdk.models.mttr_metrics_dto import MttrMetricsDto

# TODO update the JSON string below
json = "{}"
# create an instance of MttrMetricsDto from a JSON string
mttr_metrics_dto_instance = MttrMetricsDto.from_json(json)
# print the JSON string representation of the object
print(MttrMetricsDto.to_json())

# convert the object into a dict
mttr_metrics_dto_dict = mttr_metrics_dto_instance.to_dict()
# create an instance of MttrMetricsDto from a dict
mttr_metrics_dto_from_dict = MttrMetricsDto.from_dict(mttr_metrics_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


