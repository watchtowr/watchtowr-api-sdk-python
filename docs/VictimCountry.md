# VictimCountry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** |  | [optional] 
**country_name** | **str** |  | [optional] 
**count** | **float** |  | [optional] 

## Example

```python
from watchtowr_api_sdk.models.victim_country import VictimCountry

# TODO update the JSON string below
json = "{}"
# create an instance of VictimCountry from a JSON string
victim_country_instance = VictimCountry.from_json(json)
# print the JSON string representation of the object
print(VictimCountry.to_json())

# convert the object into a dict
victim_country_dict = victim_country_instance.to_dict()
# create an instance of VictimCountry from a dict
victim_country_from_dict = VictimCountry.from_dict(victim_country_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


