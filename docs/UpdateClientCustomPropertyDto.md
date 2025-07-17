# UpdateClientCustomPropertyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the custom property. Key provided must not be empty and must be unique for the model type. If is_preset is true, key must belong to one of watchTowr&#39;s preset custom properties. Accepted preset keys include: &#39;Criticality&#39;. | 
**value** | **str** | The value of the custom property. If existing custom property&#39;s preset is true, the value supplied must belong to one of the valid watchTowr preset values. Accepted preset values are &#39;Low&#39;, &#39;Medium&#39;, &#39;High&#39;, &#39;Unknown&#39; for key: &#39;Criticality&#39;. | 

## Example

```python
from watchtowr_api_sdk.models.update_client_custom_property_dto import UpdateClientCustomPropertyDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClientCustomPropertyDto from a JSON string
update_client_custom_property_dto_instance = UpdateClientCustomPropertyDto.from_json(json)
# print the JSON string representation of the object
print(UpdateClientCustomPropertyDto.to_json())

# convert the object into a dict
update_client_custom_property_dto_dict = update_client_custom_property_dto_instance.to_dict()
# create an instance of UpdateClientCustomPropertyDto from a dict
update_client_custom_property_dto_from_dict = UpdateClientCustomPropertyDto.from_dict(update_client_custom_property_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


