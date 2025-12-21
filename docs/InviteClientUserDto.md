# InviteClientUserDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address of the user to invite | 
**role_type** | **str** | Role type for the user | 
**business_unit_ids** | **List[float]** | Business Unit IDs to assign (required for BU_USER roles) | [optional] 

## Example

```python
from watchtowr_api_sdk.models.invite_client_user_dto import InviteClientUserDto

# TODO update the JSON string below
json = "{}"
# create an instance of InviteClientUserDto from a JSON string
invite_client_user_dto_instance = InviteClientUserDto.from_json(json)
# print the JSON string representation of the object
print(InviteClientUserDto.to_json())

# convert the object into a dict
invite_client_user_dto_dict = invite_client_user_dto_instance.to_dict()
# create an instance of InviteClientUserDto from a dict
invite_client_user_dto_from_dict = InviteClientUserDto.from_dict(invite_client_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


