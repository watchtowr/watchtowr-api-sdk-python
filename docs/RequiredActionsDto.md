# RequiredActionsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actively_exploited_findings** | **float** | Count of open findings currently being actively exploited | 
**unresolved_rapid_reaction_hunts** | **float** | Count of unresolved rapid reaction hunts | 

## Example

```python
from watchtowr_api_sdk.models.required_actions_dto import RequiredActionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of RequiredActionsDto from a JSON string
required_actions_dto_instance = RequiredActionsDto.from_json(json)
# print the JSON string representation of the object
print(RequiredActionsDto.to_json())

# convert the object into a dict
required_actions_dto_dict = required_actions_dto_instance.to_dict()
# create an instance of RequiredActionsDto from a dict
required_actions_dto_from_dict = RequiredActionsDto.from_dict(required_actions_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


