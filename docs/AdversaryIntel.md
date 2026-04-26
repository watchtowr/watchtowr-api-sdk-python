# AdversaryIntel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attacker_id** | **float** |  | 
**name** | **str** |  | 
**aliases** | **List[str]** |  | [optional] 
**type** | **str** |  | 
**origin_country_code** | **str** |  | [optional] 
**last_reported_date** | **datetime** |  | [optional] 
**victim_countries** | [**VictimCountrySummary**](VictimCountrySummary.md) |  | [optional] 
**target_industries** | [**TargetIndustrySummary**](TargetIndustrySummary.md) |  | [optional] 
**affected_tracked_hunts_count** | **float** |  | [optional] 
**affected_open_findings_count** | **float** |  | [optional] 
**is_affected** | **bool** | Whether the user has confirmed open findings against vulnerabilities exploited by this adversary. Scoped to the requesting user&#39;s business units and the organization&#39;s finding impact threshold. | 
**affected_kb_entry_ids** | **List[float]** | KB entry IDs that drive the &#x60;isAffected&#x60; flag, scoped to the requesting user&#39;s business units. | [optional] 

## Example

```python
from watchtowr_api_sdk.models.adversary_intel import AdversaryIntel

# TODO update the JSON string below
json = "{}"
# create an instance of AdversaryIntel from a JSON string
adversary_intel_instance = AdversaryIntel.from_json(json)
# print the JSON string representation of the object
print(AdversaryIntel.to_json())

# convert the object into a dict
adversary_intel_dict = adversary_intel_instance.to_dict()
# create an instance of AdversaryIntel from a dict
adversary_intel_from_dict = AdversaryIntel.from_dict(adversary_intel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


