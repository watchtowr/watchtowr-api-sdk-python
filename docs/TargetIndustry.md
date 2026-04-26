# TargetIndustry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**count** | **float** |  | [optional] 

## Example

```python
from watchtowr_api_sdk.models.target_industry import TargetIndustry

# TODO update the JSON string below
json = "{}"
# create an instance of TargetIndustry from a JSON string
target_industry_instance = TargetIndustry.from_json(json)
# print the JSON string representation of the object
print(TargetIndustry.to_json())

# convert the object into a dict
target_industry_dict = target_industry_instance.to_dict()
# create an instance of TargetIndustry from a dict
target_industry_from_dict = TargetIndustry.from_dict(target_industry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


