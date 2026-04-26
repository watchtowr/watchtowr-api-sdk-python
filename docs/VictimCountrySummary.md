# VictimCountrySummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[VictimCountry]**](VictimCountry.md) |  | [optional] 
**total_count** | **float** |  | [optional] 

## Example

```python
from watchtowr_api_sdk.models.victim_country_summary import VictimCountrySummary

# TODO update the JSON string below
json = "{}"
# create an instance of VictimCountrySummary from a JSON string
victim_country_summary_instance = VictimCountrySummary.from_json(json)
# print the JSON string representation of the object
print(VictimCountrySummary.to_json())

# convert the object into a dict
victim_country_summary_dict = victim_country_summary_instance.to_dict()
# create an instance of VictimCountrySummary from a dict
victim_country_summary_from_dict = VictimCountrySummary.from_dict(victim_country_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


