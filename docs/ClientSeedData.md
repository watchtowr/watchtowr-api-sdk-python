# ClientSeedData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Descriptive title for the new asset | 
**type** | **str** | Asset Type for the new asset. Valid asset types are: [] | 
**value** | **str** | Value for the asset to be added. | 

## Example

```python
from watchtowr_api_sdk.models.client_seed_data import ClientSeedData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientSeedData from a JSON string
client_seed_data_instance = ClientSeedData.from_json(json)
# print the JSON string representation of the object
print(ClientSeedData.to_json())

# convert the object into a dict
client_seed_data_dict = client_seed_data_instance.to_dict()
# create an instance of ClientSeedData from a dict
client_seed_data_from_dict = ClientSeedData.from_dict(client_seed_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


