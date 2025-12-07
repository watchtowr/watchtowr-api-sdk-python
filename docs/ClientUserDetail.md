# ClientUserDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | User ID | 
**name** | **str** | User name | 
**email** | **str** | User email | 
**title** | **str** | User title | 
**mobile_phone_number** | **str** | Mobile phone number (masked) | 
**office_phone_number** | **str** | Office phone number (masked) | 
**created_at** | **datetime** | Created at timestamp | 
**locked** | **bool** | Whether user is locked | 
**role** | **object** | User role information | 
**business_units** | [**List[ClientUserDetailBusinessUnitsInner]**](ClientUserDetailBusinessUnitsInner.md) | User business unit assignments | 

## Example

```python
from watchtowr_api_sdk.models.client_user_detail import ClientUserDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ClientUserDetail from a JSON string
client_user_detail_instance = ClientUserDetail.from_json(json)
# print the JSON string representation of the object
print(ClientUserDetail.to_json())

# convert the object into a dict
client_user_detail_dict = client_user_detail_instance.to_dict()
# create an instance of ClientUserDetail from a dict
client_user_detail_from_dict = ClientUserDetail.from_dict(client_user_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


