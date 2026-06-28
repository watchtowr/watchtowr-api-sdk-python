# ClientIntegrationItemDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_type** | **str** | Integration type. Valid values: aws, azure, googlecloud, cloudflare, alibabacloud, prismacloud, prismacloudapigee, huaweicloud, tencentcloud, wiz, servicenowcmdb, akamaiedge, armiscentrix, qualysvmdr, tenable | 
**integration_id** | **float** | Integration ID | 

## Example

```python
from watchtowr_api_sdk.models.client_integration_item_dto import ClientIntegrationItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of ClientIntegrationItemDto from a JSON string
client_integration_item_dto_instance = ClientIntegrationItemDto.from_json(json)
# print the JSON string representation of the object
print(ClientIntegrationItemDto.to_json())

# convert the object into a dict
client_integration_item_dto_dict = client_integration_item_dto_instance.to_dict()
# create an instance of ClientIntegrationItemDto from a dict
client_integration_item_dto_from_dict = ClientIntegrationItemDto.from_dict(client_integration_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


