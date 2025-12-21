# InviteUserResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**InviteUserResponse**](InviteUserResponse.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.invite_user_response_data import InviteUserResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of InviteUserResponseData from a JSON string
invite_user_response_data_instance = InviteUserResponseData.from_json(json)
# print the JSON string representation of the object
print(InviteUserResponseData.to_json())

# convert the object into a dict
invite_user_response_data_dict = invite_user_response_data_instance.to_dict()
# create an instance of InviteUserResponseData from a dict
invite_user_response_data_from_dict = InviteUserResponseData.from_dict(invite_user_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


