# KevTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cisa** | **bool** |  | 
**vulncheck** | **bool** |  | 
**watchtowr** | **bool** |  | 

## Example

```python
from watchtowr_api_sdk.models.kev_types import KevTypes

# TODO update the JSON string below
json = "{}"
# create an instance of KevTypes from a JSON string
kev_types_instance = KevTypes.from_json(json)
# print the JSON string representation of the object
print(KevTypes.to_json())

# convert the object into a dict
kev_types_dict = kev_types_instance.to_dict()
# create an instance of KevTypes from a dict
kev_types_from_dict = KevTypes.from_dict(kev_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


