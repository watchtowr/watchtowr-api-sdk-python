# FindingsSummaryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_resolved_findings** | **float** | Total count of resolved findings | 
**old_critical_high_findings** | **float** | Count of critical/high findings older than 30 days | 
**unacknowledged_critical_high_findings** | **float** | Count of unacknowledged critical/high findings | 

## Example

```python
from watchtowr_api_sdk.models.findings_summary_dto import FindingsSummaryDto

# TODO update the JSON string below
json = "{}"
# create an instance of FindingsSummaryDto from a JSON string
findings_summary_dto_instance = FindingsSummaryDto.from_json(json)
# print the JSON string representation of the object
print(FindingsSummaryDto.to_json())

# convert the object into a dict
findings_summary_dto_dict = findings_summary_dto_instance.to_dict()
# create an instance of FindingsSummaryDto from a dict
findings_summary_dto_from_dict = FindingsSummaryDto.from_dict(findings_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


