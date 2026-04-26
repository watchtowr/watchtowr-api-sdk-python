# AttackerTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apt_group** | **bool** |  | 
**ransomware** | **bool** |  | 
**botnet** | **bool** |  | 

## Example

```python
from watchtowr_api_sdk.models.attacker_types import AttackerTypes

# TODO update the JSON string below
json = "{}"
# create an instance of AttackerTypes from a JSON string
attacker_types_instance = AttackerTypes.from_json(json)
# print the JSON string representation of the object
print(AttackerTypes.to_json())

# convert the object into a dict
attacker_types_dict = attacker_types_instance.to_dict()
# create an instance of AttackerTypes from a dict
attacker_types_from_dict = AttackerTypes.from_dict(attacker_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


