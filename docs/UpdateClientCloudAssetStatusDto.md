# UpdateClientCloudAssetStatusDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Target status to update. | 
**status_reason** | **str** | Reason for updating status. | [optional] 

## Example

```python
from openapi_client.models.update_client_cloud_asset_status_dto import UpdateClientCloudAssetStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClientCloudAssetStatusDto from a JSON string
update_client_cloud_asset_status_dto_instance = UpdateClientCloudAssetStatusDto.from_json(json)
# print the JSON string representation of the object
print(UpdateClientCloudAssetStatusDto.to_json())

# convert the object into a dict
update_client_cloud_asset_status_dto_dict = update_client_cloud_asset_status_dto_instance.to_dict()
# create an instance of UpdateClientCloudAssetStatusDto from a dict
update_client_cloud_asset_status_dto_from_dict = UpdateClientCloudAssetStatusDto.from_dict(update_client_cloud_asset_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


