# SecurityPostureDashboardDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required_actions** | [**RequiredActionsDto**](RequiredActionsDto.md) | Top priority items requiring immediate attention | 
**hunt_overview** | [**HuntOverviewDto**](HuntOverviewDto.md) | Hunt-related metrics and status | 
**attack_surface_resiliency** | [**AttackSurfaceResiliencyDto**](AttackSurfaceResiliencyDto.md) | Long-term security resilience metrics | 
**organization_summary** | [**OrganizationSummaryDto**](OrganizationSummaryDto.md) | Overall organization metrics and summary | 

## Example

```python
from openapi_client.models.security_posture_dashboard_dto import SecurityPostureDashboardDto

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityPostureDashboardDto from a JSON string
security_posture_dashboard_dto_instance = SecurityPostureDashboardDto.from_json(json)
# print the JSON string representation of the object
print(SecurityPostureDashboardDto.to_json())

# convert the object into a dict
security_posture_dashboard_dto_dict = security_posture_dashboard_dto_instance.to_dict()
# create an instance of SecurityPostureDashboardDto from a dict
security_posture_dashboard_dto_from_dict = SecurityPostureDashboardDto.from_dict(security_posture_dashboard_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


