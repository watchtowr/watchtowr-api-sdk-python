# PaginatedClientCustomProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientCustomProperty]**](ClientCustomProperty.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openapi_client.models.paginated_client_custom_property import PaginatedClientCustomProperty

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClientCustomProperty from a JSON string
paginated_client_custom_property_instance = PaginatedClientCustomProperty.from_json(json)
# print the JSON string representation of the object
print(PaginatedClientCustomProperty.to_json())

# convert the object into a dict
paginated_client_custom_property_dict = paginated_client_custom_property_instance.to_dict()
# create an instance of PaginatedClientCustomProperty from a dict
paginated_client_custom_property_from_dict = PaginatedClientCustomProperty.from_dict(paginated_client_custom_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


