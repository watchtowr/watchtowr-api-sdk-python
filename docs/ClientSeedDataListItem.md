# ClientSeedDataListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Seed Data ID | 
**title** | **str** | Descriptive title for the asset | 
**type** | **str** | Asset Type. Valid asset types are: [domain, subdomain, ip, ipRange, repository, cloudStorage, container, mobileApp, saasPlatform, cloudAsset, apiDocumentation, packageManager] | 
**value** | **str** | Value for the asset | [optional] 
**values** | **object** | JSON values for the asset | [optional] 
**status_name** | **str** | Status name of the seed data | 
**status_reason** | **str** | Status reason for the seed data | [optional] 
**created_at** | **datetime** | Creation date | 
**user** | [**ClientSeedDataUser**](ClientSeedDataUser.md) | User who submitted the seed data | 
**business_units** | [**List[ClientSeedDataBusinessUnit]**](ClientSeedDataBusinessUnit.md) | Business units associated with the seed data | 

## Example

```python
from watchtowr_api_sdk.models.client_seed_data_list_item import ClientSeedDataListItem

# TODO update the JSON string below
json = "{}"
# create an instance of ClientSeedDataListItem from a JSON string
client_seed_data_list_item_instance = ClientSeedDataListItem.from_json(json)
# print the JSON string representation of the object
print(ClientSeedDataListItem.to_json())

# convert the object into a dict
client_seed_data_list_item_dict = client_seed_data_list_item_instance.to_dict()
# create an instance of ClientSeedDataListItem from a dict
client_seed_data_list_item_from_dict = ClientSeedDataListItem.from_dict(client_seed_data_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


