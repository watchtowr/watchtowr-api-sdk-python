# ClientUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | User ID | 
**name** | **str** | User name | 
**email** | **str** | User email (masked) | 
**title** | **str** | User title | 
**mobile_phone_number** | **str** | Mobile phone number (masked) | 
**office_phone_number** | **str** | Office phone number (masked) | 
**created_at** | **datetime** | Created at timestamp | 
**locked** | **bool** | Whether user is locked | 

## Example

```python
from watchtowr_api_sdk.models.client_user import ClientUser

# TODO update the JSON string below
json = "{}"
# create an instance of ClientUser from a JSON string
client_user_instance = ClientUser.from_json(json)
# print the JSON string representation of the object
print(ClientUser.to_json())

# convert the object into a dict
client_user_dict = client_user_instance.to_dict()
# create an instance of ClientUser from a dict
client_user_from_dict = ClientUser.from_dict(client_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


