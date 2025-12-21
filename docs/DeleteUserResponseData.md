# DeleteUserResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeleteUserResponse**](DeleteUserResponse.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.delete_user_response_data import DeleteUserResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteUserResponseData from a JSON string
delete_user_response_data_instance = DeleteUserResponseData.from_json(json)
# print the JSON string representation of the object
print(DeleteUserResponseData.to_json())

# convert the object into a dict
delete_user_response_data_dict = delete_user_response_data_instance.to_dict()
# create an instance of DeleteUserResponseData from a dict
delete_user_response_data_from_dict = DeleteUserResponseData.from_dict(delete_user_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


