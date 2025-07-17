# OrganizationSummaryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attack_surface** | [**AttackSurfaceDto**](AttackSurfaceDto.md) | Attack surface metrics | 
**open_findings** | [**OpenFindingsDto**](OpenFindingsDto.md) | Breakdown of findings by severity level | 
**mttr_metrics** | [**MttrMetricsDto**](MttrMetricsDto.md) | Mean Time To Remediation metrics | 
**findings_summary** | [**FindingsSummaryDto**](FindingsSummaryDto.md) | Historical and categorized finding metrics | 

## Example

```python
from watchtowr_api_sdk.models.organization_summary_dto import OrganizationSummaryDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationSummaryDto from a JSON string
organization_summary_dto_instance = OrganizationSummaryDto.from_json(json)
# print the JSON string representation of the object
print(OrganizationSummaryDto.to_json())

# convert the object into a dict
organization_summary_dto_dict = organization_summary_dto_instance.to_dict()
# create an instance of OrganizationSummaryDto from a dict
organization_summary_dto_from_dict = OrganizationSummaryDto.from_dict(organization_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


