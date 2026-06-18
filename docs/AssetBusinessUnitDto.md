# AssetBusinessUnitDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Business Unit ID | 
**name** | **str** | Business Unit Name | 

## Example

```python
from watchtowr_api_sdk.models.asset_business_unit_dto import AssetBusinessUnitDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetBusinessUnitDto from a JSON string
asset_business_unit_dto_instance = AssetBusinessUnitDto.from_json(json)
# print the JSON string representation of the object
print(AssetBusinessUnitDto.to_json())

# convert the object into a dict
asset_business_unit_dto_dict = asset_business_unit_dto_instance.to_dict()
# create an instance of AssetBusinessUnitDto from a dict
asset_business_unit_dto_from_dict = AssetBusinessUnitDto.from_dict(asset_business_unit_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


