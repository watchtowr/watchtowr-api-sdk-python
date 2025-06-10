# ClientCustomProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**key** | **str** | The key of the custom property. Key provided must not be empty and must be unique for the model type. If is_preset is true, key must belong to one of watchTowr&#39;s preset custom properties. Accepted preset keys include: &#39;Criticality&#39;. | 
**value** | **str** | The value of the custom property. Any string value is accepted if preset is false. If existing custom property&#39;s preset is true, the value supplied must belong to one of the valid watchTowr preset values. Accepted values are &#39;Low&#39;, &#39;Medium&#39;, &#39;High&#39;, &#39;Unknown&#39; for key: &#39;Criticality&#39;. | 
**is_preset** | **bool** | Indicates whether this is a watchTowr preset custom property. | 

## Example

```python
from openapi_client.models.client_custom_property import ClientCustomProperty

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCustomProperty from a JSON string
client_custom_property_instance = ClientCustomProperty.from_json(json)
# print the JSON string representation of the object
print(ClientCustomProperty.to_json())

# convert the object into a dict
client_custom_property_dict = client_custom_property_instance.to_dict()
# create an instance of ClientCustomProperty from a dict
client_custom_property_from_dict = ClientCustomProperty.from_dict(client_custom_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


