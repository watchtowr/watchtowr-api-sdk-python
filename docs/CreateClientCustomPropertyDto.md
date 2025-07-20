# CreateClientCustomPropertyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the custom property. Key provided must not be empty and must be unique for the model type. If is_preset is true, key must belong to one of watchTowr&#39;s preset custom properties. Accepted preset keys include: &#39;Criticality&#39;. | 
**value** | **object** | The value of the custom property. If existing custom property&#39;s preset is true, the value supplied must belong to one of the valid watchTowr preset values. Accepted preset values are &#39;Low&#39;, &#39;Medium&#39;, &#39;High&#39;, &#39;Unknown&#39; for key: &#39;Criticality&#39;. | 
**is_preset** | **bool** | Defaults to false. If true, custom property is a watchTowr preset custom property. | [optional] 

## Example

```python
from watchtowr_api_sdk.models.create_client_custom_property_dto import CreateClientCustomPropertyDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClientCustomPropertyDto from a JSON string
create_client_custom_property_dto_instance = CreateClientCustomPropertyDto.from_json(json)
# print the JSON string representation of the object
print(CreateClientCustomPropertyDto.to_json())

# convert the object into a dict
create_client_custom_property_dto_dict = create_client_custom_property_dto_instance.to_dict()
# create an instance of CreateClientCustomPropertyDto from a dict
create_client_custom_property_dto_from_dict = CreateClientCustomPropertyDto.from_dict(create_client_custom_property_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


