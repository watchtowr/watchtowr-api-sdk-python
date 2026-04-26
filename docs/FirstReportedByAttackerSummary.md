# FirstReportedByAttackerSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apt_group_first_reported** | **datetime** |  | [optional] 
**ransomware_first_reported** | **datetime** |  | [optional] 
**botnet_first_reported** | **datetime** |  | [optional] 

## Example

```python
from watchtowr_api_sdk.models.first_reported_by_attacker_summary import FirstReportedByAttackerSummary

# TODO update the JSON string below
json = "{}"
# create an instance of FirstReportedByAttackerSummary from a JSON string
first_reported_by_attacker_summary_instance = FirstReportedByAttackerSummary.from_json(json)
# print the JSON string representation of the object
print(FirstReportedByAttackerSummary.to_json())

# convert the object into a dict
first_reported_by_attacker_summary_dict = first_reported_by_attacker_summary_instance.to_dict()
# create an instance of FirstReportedByAttackerSummary from a dict
first_reported_by_attacker_summary_from_dict = FirstReportedByAttackerSummary.from_dict(first_reported_by_attacker_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


