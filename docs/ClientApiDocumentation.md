# ClientApiDocumentation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientApiDocumentationAsset**](ClientApiDocumentationAsset.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.client_api_documentation import ClientApiDocumentation

# TODO update the JSON string below
json = "{}"
# create an instance of ClientApiDocumentation from a JSON string
client_api_documentation_instance = ClientApiDocumentation.from_json(json)
# print the JSON string representation of the object
print(ClientApiDocumentation.to_json())

# convert the object into a dict
client_api_documentation_dict = client_api_documentation_instance.to_dict()
# create an instance of ClientApiDocumentation from a dict
client_api_documentation_from_dict = ClientApiDocumentation.from_dict(client_api_documentation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


