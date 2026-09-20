# PaginatedClientCredentialsLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientCredentialsLog]**](ClientCredentialsLog.md) | List of credential attempt logs | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from watchtowr_api_sdk.models.paginated_client_credentials_log import PaginatedClientCredentialsLog

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedClientCredentialsLog from a JSON string
paginated_client_credentials_log_instance = PaginatedClientCredentialsLog.from_json(json)
# print the JSON string representation of the object
print(PaginatedClientCredentialsLog.to_json())

# convert the object into a dict
paginated_client_credentials_log_dict = paginated_client_credentials_log_instance.to_dict()
# create an instance of PaginatedClientCredentialsLog from a dict
paginated_client_credentials_log_from_dict = PaginatedClientCredentialsLog.from_dict(paginated_client_credentials_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


