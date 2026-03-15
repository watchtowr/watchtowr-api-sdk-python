# ClientFindingManualTicket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**user_id** | **float** |  | 
**finding_id** | **float** |  | 
**organisation_id** | **float** |  | 
**board_name** | **str** |  | 
**issue_link** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from watchtowr_api_sdk.models.client_finding_manual_ticket import ClientFindingManualTicket

# TODO update the JSON string below
json = "{}"
# create an instance of ClientFindingManualTicket from a JSON string
client_finding_manual_ticket_instance = ClientFindingManualTicket.from_json(json)
# print the JSON string representation of the object
print(ClientFindingManualTicket.to_json())

# convert the object into a dict
client_finding_manual_ticket_dict = client_finding_manual_ticket_instance.to_dict()
# create an instance of ClientFindingManualTicket from a dict
client_finding_manual_ticket_from_dict = ClientFindingManualTicket.from_dict(client_finding_manual_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


