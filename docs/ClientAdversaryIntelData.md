# ClientAdversaryIntelData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AdversaryIntelDetails**](AdversaryIntelDetails.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.client_adversary_intel_data import ClientAdversaryIntelData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientAdversaryIntelData from a JSON string
client_adversary_intel_data_instance = ClientAdversaryIntelData.from_json(json)
# print the JSON string representation of the object
print(ClientAdversaryIntelData.to_json())

# convert the object into a dict
client_adversary_intel_data_dict = client_adversary_intel_data_instance.to_dict()
# create an instance of ClientAdversaryIntelData from a dict
client_adversary_intel_data_from_dict = ClientAdversaryIntelData.from_dict(client_adversary_intel_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


