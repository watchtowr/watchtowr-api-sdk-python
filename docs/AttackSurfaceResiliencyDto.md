# AttackSurfaceResiliencyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concerning_services** | **float** | Count of concerning network services | 
**concerning_points_of_interest** | **float** | Count of concerning points of interest | 
**valid_credentials** | **float** | Count of findings with valid credentials | 
**open_findings** | **float** | Total count of open findings | 

## Example

```python
from watchtowr_api_sdk.models.attack_surface_resiliency_dto import AttackSurfaceResiliencyDto

# TODO update the JSON string below
json = "{}"
# create an instance of AttackSurfaceResiliencyDto from a JSON string
attack_surface_resiliency_dto_instance = AttackSurfaceResiliencyDto.from_json(json)
# print the JSON string representation of the object
print(AttackSurfaceResiliencyDto.to_json())

# convert the object into a dict
attack_surface_resiliency_dto_dict = attack_surface_resiliency_dto_instance.to_dict()
# create an instance of AttackSurfaceResiliencyDto from a dict
attack_surface_resiliency_dto_from_dict = AttackSurfaceResiliencyDto.from_dict(attack_surface_resiliency_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


