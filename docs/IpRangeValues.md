# IpRangeValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidr** | **str** | CIDR for IP Range (e.g., \&quot;192.168.1.0/24\&quot;) | 
**asn** | **str** | ASN for IP Range (e.g., \&quot;AS16509\&quot;) | 

## Example

```python
from watchtowr_api_sdk.models.ip_range_values import IpRangeValues

# TODO update the JSON string below
json = "{}"
# create an instance of IpRangeValues from a JSON string
ip_range_values_instance = IpRangeValues.from_json(json)
# print the JSON string representation of the object
print(IpRangeValues.to_json())

# convert the object into a dict
ip_range_values_dict = ip_range_values_instance.to_dict()
# create an instance of IpRangeValues from a dict
ip_range_values_from_dict = IpRangeValues.from_dict(ip_range_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


