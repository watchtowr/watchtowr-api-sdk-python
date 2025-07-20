# AssetBusinessUnitIdsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_unit_ids** | **List[str]** | List of business unit IDs to assign the asset to. | 

## Example

```python
from watchtowr_api_sdk.models.asset_business_unit_ids_dto import AssetBusinessUnitIdsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AssetBusinessUnitIdsDTO from a JSON string
asset_business_unit_ids_dto_instance = AssetBusinessUnitIdsDTO.from_json(json)
# print the JSON string representation of the object
print(AssetBusinessUnitIdsDTO.to_json())

# convert the object into a dict
asset_business_unit_ids_dto_dict = asset_business_unit_ids_dto_instance.to_dict()
# create an instance of AssetBusinessUnitIdsDTO from a dict
asset_business_unit_ids_dto_from_dict = AssetBusinessUnitIdsDTO.from_dict(asset_business_unit_ids_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


