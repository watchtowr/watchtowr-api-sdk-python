# ClientFindingRetestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ClientFinding**](ClientFinding.md) |  | 
**dns_connected_retests_triggered** | **int** | Number of additional DNS-connected findings retested alongside the requested finding (present when &#x60;includeDnsConnected&#x3D;true&#x60;). | [optional] 

## Example

```python
from watchtowr_api_sdk.models.client_finding_retest_response import ClientFindingRetestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClientFindingRetestResponse from a JSON string
client_finding_retest_response_instance = ClientFindingRetestResponse.from_json(json)
# print the JSON string representation of the object
print(ClientFindingRetestResponse.to_json())

# convert the object into a dict
client_finding_retest_response_dict = client_finding_retest_response_instance.to_dict()
# create an instance of ClientFindingRetestResponse from a dict
client_finding_retest_response_from_dict = ClientFindingRetestResponse.from_dict(client_finding_retest_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


