# ThreatActorDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attacker_name** | **str** | Threat actor name | 
**country** | **str** | Country code | 

## Example

```python
from watchtowr_api_sdk.models.threat_actor_dto import ThreatActorDto

# TODO update the JSON string below
json = "{}"
# create an instance of ThreatActorDto from a JSON string
threat_actor_dto_instance = ThreatActorDto.from_json(json)
# print the JSON string representation of the object
print(ThreatActorDto.to_json())

# convert the object into a dict
threat_actor_dto_dict = threat_actor_dto_instance.to_dict()
# create an instance of ThreatActorDto from a dict
threat_actor_dto_from_dict = ThreatActorDto.from_dict(threat_actor_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


