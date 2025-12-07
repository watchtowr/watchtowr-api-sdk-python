# ClientSeedDataUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | User ID | 
**name** | **str** | User name | 
**email** | **str** | User email | 

## Example

```python
from watchtowr_api_sdk.models.client_seed_data_user import ClientSeedDataUser

# TODO update the JSON string below
json = "{}"
# create an instance of ClientSeedDataUser from a JSON string
client_seed_data_user_instance = ClientSeedDataUser.from_json(json)
# print the JSON string representation of the object
print(ClientSeedDataUser.to_json())

# convert the object into a dict
client_seed_data_user_dict = client_seed_data_user_instance.to_dict()
# create an instance of ClientSeedDataUser from a dict
client_seed_data_user_from_dict = ClientSeedDataUser.from_dict(client_seed_data_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


