# TargetIndustrySummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TargetIndustry]**](TargetIndustry.md) |  | [optional] 
**total_count** | **float** |  | [optional] 

## Example

```python
from watchtowr_api_sdk.models.target_industry_summary import TargetIndustrySummary

# TODO update the JSON string below
json = "{}"
# create an instance of TargetIndustrySummary from a JSON string
target_industry_summary_instance = TargetIndustrySummary.from_json(json)
# print the JSON string representation of the object
print(TargetIndustrySummary.to_json())

# convert the object into a dict
target_industry_summary_dict = target_industry_summary_instance.to_dict()
# create an instance of TargetIndustrySummary from a dict
target_industry_summary_from_dict = TargetIndustrySummary.from_dict(target_industry_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


