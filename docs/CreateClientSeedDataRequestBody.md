# CreateClientSeedDataRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientSeedData]**](ClientSeedData.md) | JSON array listing seed data assets to submit for review. | 
**business_units** | **List[object]** | List of business units to allocate new assets to. -1 indicates UNASSIGNED business unit | [optional] 

## Example

```python
from watchtowr_api_sdk.models.create_client_seed_data_request_body import CreateClientSeedDataRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClientSeedDataRequestBody from a JSON string
create_client_seed_data_request_body_instance = CreateClientSeedDataRequestBody.from_json(json)
# print the JSON string representation of the object
print(CreateClientSeedDataRequestBody.to_json())

# convert the object into a dict
create_client_seed_data_request_body_dict = create_client_seed_data_request_body_instance.to_dict()
# create an instance of CreateClientSeedDataRequestBody from a dict
create_client_seed_data_request_body_from_dict = CreateClientSeedDataRequestBody.from_dict(create_client_seed_data_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


