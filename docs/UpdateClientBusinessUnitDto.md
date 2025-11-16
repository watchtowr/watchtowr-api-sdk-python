# UpdateClientBusinessUnitDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Business unit name | 
**description** | **str** | Business unit description | [optional] 
**type** | **str** | Business unit type | 
**parent_id** | **float** | Parent business unit ID. Set to null to remove parent relationship. | [optional] 
**user_ids** | **List[float]** | Array of user IDs to assign to this business unit | [optional] 

## Example

```python
from watchtowr_api_sdk.models.update_client_business_unit_dto import UpdateClientBusinessUnitDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClientBusinessUnitDto from a JSON string
update_client_business_unit_dto_instance = UpdateClientBusinessUnitDto.from_json(json)
# print the JSON string representation of the object
print(UpdateClientBusinessUnitDto.to_json())

# convert the object into a dict
update_client_business_unit_dto_dict = update_client_business_unit_dto_instance.to_dict()
# create an instance of UpdateClientBusinessUnitDto from a dict
update_client_business_unit_dto_from_dict = UpdateClientBusinessUnitDto.from_dict(update_client_business_unit_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


