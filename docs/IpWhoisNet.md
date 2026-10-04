# IpWhoisNet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidr** | **str** | CIDR of the network block. | [optional] 
**name** | **str** | Network name registered for the block (NetName or netname). | [optional] 
**handle** | **str** | Registry handle of the network block. | [optional] 
**range** | **str** | First and last address of the network block. | [optional] 
**description** | **str** | Organization name or description lines of the block, joined with newlines. | [optional] 
**country** | **str** | Country code. | [optional] 
**state** | **str** | State or province. | [optional] 
**city** | **str** | City. | [optional] 
**address** | **str** | Street address; may span several lines. | [optional] 
**postal_code** | **str** | Postal code. | [optional] 
**emails** | **List[str]** | Contact emails listed for the block. | [optional] 
**created** | **str** | Registration date, as the registry reports it. | [optional] 
**updated** | **str** | Last update date, as the registry reports it. | [optional] 

## Example

```python
from watchtowr_api_sdk.models.ip_whois_net import IpWhoisNet

# TODO update the JSON string below
json = "{}"
# create an instance of IpWhoisNet from a JSON string
ip_whois_net_instance = IpWhoisNet.from_json(json)
# print the JSON string representation of the object
print(IpWhoisNet.to_json())

# convert the object into a dict
ip_whois_net_dict = ip_whois_net_instance.to_dict()
# create an instance of IpWhoisNet from a dict
ip_whois_net_from_dict = IpWhoisNet.from_dict(ip_whois_net_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


