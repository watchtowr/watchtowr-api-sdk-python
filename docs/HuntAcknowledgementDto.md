# HuntAcknowledgementDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_acknowledged** | **bool** | Whether the hunt has been acknowledged | 
**number_of_seen** | **float** | Number of users who have seen the hunt | 

## Example

```python
from openapi_client.models.hunt_acknowledgement_dto import HuntAcknowledgementDto

# TODO update the JSON string below
json = "{}"
# create an instance of HuntAcknowledgementDto from a JSON string
hunt_acknowledgement_dto_instance = HuntAcknowledgementDto.from_json(json)
# print the JSON string representation of the object
print(HuntAcknowledgementDto.to_json())

# convert the object into a dict
hunt_acknowledgement_dto_dict = hunt_acknowledgement_dto_instance.to_dict()
# create an instance of HuntAcknowledgementDto from a dict
hunt_acknowledgement_dto_from_dict = HuntAcknowledgementDto.from_dict(hunt_acknowledgement_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


