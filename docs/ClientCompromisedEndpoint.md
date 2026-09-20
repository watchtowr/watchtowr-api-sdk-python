# ClientCompromisedEndpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Compromised endpoint ID | 
**hostname** | **str** | Hostname of the compromised endpoint | 
**ip** | **str** | IP address of the compromised endpoint | 
**stealer_id** | **str** | Unique stealer identifier | 
**stealer_family** | **str** | Stealer malware family | 
**status** | **str** | Status of the compromised endpoint | 
**date_compromised** | **str** | Date and time when the endpoint was compromised | 
**operating_system** | **str** | Operating system of the compromised endpoint | 
**malware_path** | **str** | File path where the malware was located | 
**country** | **str** | Country where the compromised endpoint is located | 
**discovery_type** | **str** | Method used to discover the compromised endpoint | 
**discovery_value** | **str** | Value used for discovery (e.g., credential, domain) | 
**created_at** | **str** | Date when the endpoint was first discovered | 
**updated_at** | **str** | Date when the endpoint record was last updated | 

## Example

```python
from watchtowr_api_sdk.models.client_compromised_endpoint import ClientCompromisedEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCompromisedEndpoint from a JSON string
client_compromised_endpoint_instance = ClientCompromisedEndpoint.from_json(json)
# print the JSON string representation of the object
print(ClientCompromisedEndpoint.to_json())

# convert the object into a dict
client_compromised_endpoint_dict = client_compromised_endpoint_instance.to_dict()
# create an instance of ClientCompromisedEndpoint from a dict
client_compromised_endpoint_from_dict = ClientCompromisedEndpoint.from_dict(client_compromised_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


