# InviteClientUsersBodyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[InviteClientUserDto]**](InviteClientUserDto.md) | List of users to invite | 

## Example

```python
from watchtowr_api_sdk.models.invite_client_users_body_dto import InviteClientUsersBodyDto

# TODO update the JSON string below
json = "{}"
# create an instance of InviteClientUsersBodyDto from a JSON string
invite_client_users_body_dto_instance = InviteClientUsersBodyDto.from_json(json)
# print the JSON string representation of the object
print(InviteClientUsersBodyDto.to_json())

# convert the object into a dict
invite_client_users_body_dto_dict = invite_client_users_body_dto_instance.to_dict()
# create an instance of InviteClientUsersBodyDto from a dict
invite_client_users_body_dto_from_dict = InviteClientUsersBodyDto.from_dict(invite_client_users_body_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


