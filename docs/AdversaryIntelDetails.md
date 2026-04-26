# AdversaryIntelDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attacker_id** | **float** |  | 
**name** | **str** |  | 
**type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**aliases** | **List[str]** |  | [optional] 
**country_code** | **str** |  | [optional] 
**first_reported_date** | **datetime** |  | [optional] 
**vulnerability_last_updated** | **datetime** |  | [optional] 
**mitre_last_updated** | **datetime** |  | [optional] 
**victim_countries** | [**VictimCountrySummary**](VictimCountrySummary.md) |  | [optional] 
**target_industries** | [**TargetIndustrySummary**](TargetIndustrySummary.md) |  | [optional] 
**latest_media** | [**List[Media]**](Media.md) |  | [optional] 
**is_affected** | **bool** | Whether the user has confirmed open findings against vulnerabilities exploited by this adversary. Scoped to the requesting user&#39;s business units and the organization&#39;s finding impact threshold. | 
**affected_kb_entry_ids** | **List[float]** | KB entry IDs that drive the &#x60;isAffected&#x60; flag, scoped to the requesting user&#39;s business units. | 

## Example

```python
from watchtowr_api_sdk.models.adversary_intel_details import AdversaryIntelDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AdversaryIntelDetails from a JSON string
adversary_intel_details_instance = AdversaryIntelDetails.from_json(json)
# print the JSON string representation of the object
print(AdversaryIntelDetails.to_json())

# convert the object into a dict
adversary_intel_details_dict = adversary_intel_details_instance.to_dict()
# create an instance of AdversaryIntelDetails from a dict
adversary_intel_details_from_dict = AdversaryIntelDetails.from_dict(adversary_intel_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


