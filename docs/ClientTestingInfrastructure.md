# ClientTestingInfrastructure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**region** | **str** |  | [optional] 
**whitelist** | **bool** |  | 

## Example

```python
from watchtowr_api_sdk.models.client_testing_infrastructure import ClientTestingInfrastructure

# TODO update the JSON string below
json = "{}"
# create an instance of ClientTestingInfrastructure from a JSON string
client_testing_infrastructure_instance = ClientTestingInfrastructure.from_json(json)
# print the JSON string representation of the object
print(ClientTestingInfrastructure.to_json())

# convert the object into a dict
client_testing_infrastructure_dict = client_testing_infrastructure_instance.to_dict()
# create an instance of ClientTestingInfrastructure from a dict
client_testing_infrastructure_from_dict = ClientTestingInfrastructure.from_dict(client_testing_infrastructure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


