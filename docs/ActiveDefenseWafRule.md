# ActiveDefenseWafRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**action_category** | **str** | Action category (mod_security). | [optional] 
**action_type** | **str** | Action type (oci_waf). | [optional] 
**attack_type** | **str** | Attack classification (f5_bigip_advanced_waf). | [optional] 
**condition** | **str** | Single-condition expression (oci_waf, mod_security). | [optional] 
**enabled** | **bool** | Whether the rule is enabled (imperva). | [optional] 
**group_operator** | **str** | Operator joining conditions. | [optional] 
**message** | **str** | Rule message. | [optional] 
**msg** | **str** | Short rule message (mod_security &#x60;msg&#x60;). | [optional] 
**response_code** | **int** | HTTP status returned (oci_waf). | [optional] 
**risk** | **float** | Risk score (f5_bigip_advanced_waf). | [optional] 
**rule** | **str** | Raw rule body (snort, yara, sigma). | [optional] 
**secrule** | **str** | ModSecurity SecRule body. | [optional] 
**severity** | **str** | Severity (fortiweb, imperva). | [optional] 
**signature** | **str** | Signature body (f5_bigip_advanced_waf). | [optional] 
**software_version** | **str** | Target software version. | [optional] 
**strategies** | **List[Dict[str, object]]** | Provider-specific match strategies (tencent_cloud_waf). | [optional] 
**match_criteria** | **List[Dict[str, object]]** | Provider-specific match criteria (imperva_waf_gateway). | [optional] 
**display_response_page** | **bool** | Imperva: show a response page. | [optional] 
**one_alert_per_session** | **bool** | Imperva: alert once per session. | [optional] 
**preview** | **bool** | Whether the rule is a preview/monitor-only variant (google_cloud_armor). | [optional] 
**name** | **str** |  | [optional] 
**template** | **str** | Deployable template body (AWS CloudFormation YAML or Azure ARM JSON). | [optional] 
**description** | **str** |  | [optional] 
**expression** | **str** |  | [optional] 
**filter** | **str** |  | [optional] 
**vcl** | **str** |  | [optional] 
**action** | **str** |  | [optional] 
**tag** | **List[str]** |  | [optional] 
**operation** | **str** |  | [optional] 
**structured** | **bool** |  | [optional] 
**conditions** | [**List[ActiveDefenseWafRuleCondition]**](ActiveDefenseWafRuleCondition.md) |  | [optional] 

## Example

```python
from watchtowr_api_sdk.models.active_defense_waf_rule import ActiveDefenseWafRule

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDefenseWafRule from a JSON string
active_defense_waf_rule_instance = ActiveDefenseWafRule.from_json(json)
# print the JSON string representation of the object
print(ActiveDefenseWafRule.to_json())

# convert the object into a dict
active_defense_waf_rule_dict = active_defense_waf_rule_instance.to_dict()
# create an instance of ActiveDefenseWafRule from a dict
active_defense_waf_rule_from_dict = ActiveDefenseWafRule.from_dict(active_defense_waf_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


