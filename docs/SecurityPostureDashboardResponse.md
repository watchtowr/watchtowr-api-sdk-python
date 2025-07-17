# SecurityPostureDashboardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SecurityPostureDashboardDto**](SecurityPostureDashboardDto.md) | Security posture dashboard data | 

## Example

```python
from openapi_client.models.security_posture_dashboard_response import SecurityPostureDashboardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityPostureDashboardResponse from a JSON string
security_posture_dashboard_response_instance = SecurityPostureDashboardResponse.from_json(json)
# print the JSON string representation of the object
print(SecurityPostureDashboardResponse.to_json())

# convert the object into a dict
security_posture_dashboard_response_dict = security_posture_dashboard_response_instance.to_dict()
# create an instance of SecurityPostureDashboardResponse from a dict
security_posture_dashboard_response_from_dict = SecurityPostureDashboardResponse.from_dict(security_posture_dashboard_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


