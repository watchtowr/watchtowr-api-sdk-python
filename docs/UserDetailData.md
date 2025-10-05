# UserDetailData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientUserDetail**](ClientUserDetail.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.user_detail_data import UserDetailData

# TODO update the JSON string below
json = "{}"
# create an instance of UserDetailData from a JSON string
user_detail_data_instance = UserDetailData.from_json(json)
# print the JSON string representation of the object
print(UserDetailData.to_json())

# convert the object into a dict
user_detail_data_dict = user_detail_data_instance.to_dict()
# create an instance of UserDetailData from a dict
user_detail_data_from_dict = UserDetailData.from_dict(user_detail_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


