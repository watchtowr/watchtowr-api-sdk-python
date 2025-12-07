# ClientSeedDataBusinessUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Business Unit ID | 
**name** | **str** | Business Unit name | 
**description** | **str** | Business Unit description | [optional] 
**type** | **str** | Business Unit type | 
**created_at** | **datetime** | Creation date | 
**updated_at** | **datetime** | Last update date | 

## Example

```python
from watchtowr_api_sdk.models.client_seed_data_business_unit import ClientSeedDataBusinessUnit

# TODO update the JSON string below
json = "{}"
# create an instance of ClientSeedDataBusinessUnit from a JSON string
client_seed_data_business_unit_instance = ClientSeedDataBusinessUnit.from_json(json)
# print the JSON string representation of the object
print(ClientSeedDataBusinessUnit.to_json())

# convert the object into a dict
client_seed_data_business_unit_dict = client_seed_data_business_unit_instance.to_dict()
# create an instance of ClientSeedDataBusinessUnit from a dict
client_seed_data_business_unit_from_dict = ClientSeedDataBusinessUnit.from_dict(client_seed_data_business_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


