# IpWhoisDataObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | **str** | Number of the autonomous system (ASN) that announces the IP. | [optional] 
**asn_cidr** | **str** | Network block (CIDR) the ASN lookup matched. | [optional] 
**asn_country_code** | **str** | Country code from the ASN lookup. | [optional] 
**asn_date** | **str** | Allocation date from the ASN lookup. | [optional] 
**asn_description** | **str** | Name of the autonomous system. | [optional] 
**asn_registry** | **str** | Regional internet registry. | [optional] 
**query** | **str** | IP address that was looked up. For an IP range, an address inside the range. | [optional] 
**nets** | [**List[IpWhoisNet]**](IpWhoisNet.md) | Network blocks parsed from the registry WHOIS record. | [optional] 
**nir** | **object** | National internet registry details, when the registry refers to one. | [optional] 
**referral** | **object** | Referral WHOIS details, when the registry refers to another server. | [optional] 
**raw_referral** | **str** | Raw referral WHOIS text. | [optional] 
**message** | **str** | Explains why no WHOIS record is present. When set, it is the only field returned. | [optional] 

## Example

```python
from watchtowr_api_sdk.models.ip_whois_data_object import IpWhoisDataObject

# TODO update the JSON string below
json = "{}"
# create an instance of IpWhoisDataObject from a JSON string
ip_whois_data_object_instance = IpWhoisDataObject.from_json(json)
# print the JSON string representation of the object
print(IpWhoisDataObject.to_json())

# convert the object into a dict
ip_whois_data_object_dict = ip_whois_data_object_instance.to_dict()
# create an instance of IpWhoisDataObject from a dict
ip_whois_data_object_from_dict = IpWhoisDataObject.from_dict(ip_whois_data_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


