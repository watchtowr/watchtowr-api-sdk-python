# ClientApiDocumentationAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**type** | **str** |  | 
**name** | **str** |  | 
**source** | **str** |  | 
**platform** | **str** |  | 
**status** | **str** |  | 
**created_at** | [**DatetimeDate**](datetime.date.md) |  | 
**url** | **str** |  | 
**custom_properties** | [**List[ClientCustomProperty]**](ClientCustomProperty.md) |  | 
**criticality** | **str** |  | 

## Example

```python
from watchtowr_api_sdk.models.client_api_documentation_asset import ClientApiDocumentationAsset

# TODO update the JSON string below
json = "{}"
# create an instance of ClientApiDocumentationAsset from a JSON string
client_api_documentation_asset_instance = ClientApiDocumentationAsset.from_json(json)
# print the JSON string representation of the object
print(ClientApiDocumentationAsset.to_json())

# convert the object into a dict
client_api_documentation_asset_dict = client_api_documentation_asset_instance.to_dict()
# create an instance of ClientApiDocumentationAsset from a dict
client_api_documentation_asset_from_dict = ClientApiDocumentationAsset.from_dict(client_api_documentation_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


