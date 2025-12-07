# UpdateClientFindingStateRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | Finding state. Different to status, this is about tracking how the finding is being handled. | 

## Example

```python
from watchtowr_api_sdk.models.update_client_finding_state_request_body import UpdateClientFindingStateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClientFindingStateRequestBody from a JSON string
update_client_finding_state_request_body_instance = UpdateClientFindingStateRequestBody.from_json(json)
# print the JSON string representation of the object
print(UpdateClientFindingStateRequestBody.to_json())

# convert the object into a dict
update_client_finding_state_request_body_dict = update_client_finding_state_request_body_instance.to_dict()
# create an instance of UpdateClientFindingStateRequestBody from a dict
update_client_finding_state_request_body_from_dict = UpdateClientFindingStateRequestBody.from_dict(update_client_finding_state_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


