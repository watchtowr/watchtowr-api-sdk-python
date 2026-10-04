# IpWhoisData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | The unique identifier for the WHOIS record. | 
**data** | [**IpWhoisDataObject**](IpWhoisDataObject.md) |  | 
**raw** | **str** | The full WHOIS text of the record. | 

## Example

```python
from watchtowr_api_sdk.models.ip_whois_data import IpWhoisData

# TODO update the JSON string below
json = "{}"
# create an instance of IpWhoisData from a JSON string
ip_whois_data_instance = IpWhoisData.from_json(json)
# print the JSON string representation of the object
print(IpWhoisData.to_json())

# convert the object into a dict
ip_whois_data_dict = ip_whois_data_instance.to_dict()
# create an instance of IpWhoisData from a dict
ip_whois_data_from_dict = IpWhoisData.from_dict(ip_whois_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


