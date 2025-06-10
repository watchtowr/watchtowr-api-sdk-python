# PaginatedApiDocumentation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientApiDocumentationAsset]**](ClientApiDocumentationAsset.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openapi_client.models.paginated_api_documentation import PaginatedApiDocumentation

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedApiDocumentation from a JSON string
paginated_api_documentation_instance = PaginatedApiDocumentation.from_json(json)
# print the JSON string representation of the object
print(PaginatedApiDocumentation.to_json())

# convert the object into a dict
paginated_api_documentation_dict = paginated_api_documentation_instance.to_dict()
# create an instance of PaginatedApiDocumentation from a dict
paginated_api_documentation_from_dict = PaginatedApiDocumentation.from_dict(paginated_api_documentation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


