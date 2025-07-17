# AttackSurfaceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_verified_assets** | **float** | Total count of verified assets | 
**total_points_of_interest** | **float** | Total count of points of interest | 
**total_network_services** | **float** | Total count of network services | 
**total_certificates** | **float** | Total count of TLS/SSL certificates | 

## Example

```python
from openapi_client.models.attack_surface_dto import AttackSurfaceDto

# TODO update the JSON string below
json = "{}"
# create an instance of AttackSurfaceDto from a JSON string
attack_surface_dto_instance = AttackSurfaceDto.from_json(json)
# print the JSON string representation of the object
print(AttackSurfaceDto.to_json())

# convert the object into a dict
attack_surface_dto_dict = attack_surface_dto_instance.to_dict()
# create an instance of AttackSurfaceDto from a dict
attack_surface_dto_from_dict = AttackSurfaceDto.from_dict(attack_surface_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


