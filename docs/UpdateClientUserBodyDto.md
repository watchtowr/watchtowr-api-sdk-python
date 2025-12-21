# UpdateClientUserBodyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_type** | **str** | Role type to assign to the user | 
**business_unit_ids** | **List[float]** | Business Unit IDs to assign (required for BU_USER roles) | 
**locked** | **bool** | Whether the user is locked (prevented from logging in) | 

## Example

```python
from watchtowr_api_sdk.models.update_client_user_body_dto import UpdateClientUserBodyDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClientUserBodyDto from a JSON string
update_client_user_body_dto_instance = UpdateClientUserBodyDto.from_json(json)
# print the JSON string representation of the object
print(UpdateClientUserBodyDto.to_json())

# convert the object into a dict
update_client_user_body_dto_dict = update_client_user_body_dto_instance.to_dict()
# create an instance of UpdateClientUserBodyDto from a dict
update_client_user_body_dto_from_dict = UpdateClientUserBodyDto.from_dict(update_client_user_body_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


