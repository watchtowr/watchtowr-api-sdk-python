# CreateClientFindingManualTicketRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**board_name** | **str** | Name of the external board or ticketing system. | 
**issue_link** | **str** | URL of the manually created ticket. | 

## Example

```python
from watchtowr_api_sdk.models.create_client_finding_manual_ticket_request_body import CreateClientFindingManualTicketRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClientFindingManualTicketRequestBody from a JSON string
create_client_finding_manual_ticket_request_body_instance = CreateClientFindingManualTicketRequestBody.from_json(json)
# print the JSON string representation of the object
print(CreateClientFindingManualTicketRequestBody.to_json())

# convert the object into a dict
create_client_finding_manual_ticket_request_body_dict = create_client_finding_manual_ticket_request_body_instance.to_dict()
# create an instance of CreateClientFindingManualTicketRequestBody from a dict
create_client_finding_manual_ticket_request_body_from_dict = CreateClientFindingManualTicketRequestBody.from_dict(create_client_finding_manual_ticket_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


