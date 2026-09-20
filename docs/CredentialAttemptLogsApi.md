# watchtowr_api_sdk.CredentialAttemptLogsApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_credential_attempt_logs**](CredentialAttemptLogsApi.md#get_list_credential_attempt_logs) | **GET** /api/client/credential-attempt-logs/list | List Credential Attempt Logs


# **get_list_credential_attempt_logs**
> PaginatedClientCredentialsLog get_list_credential_attempt_logs(page=page, page_size=page_size, technologies=technologies, asset_name=asset_name, username=username, statuses=statuses, created_from=created_from, created_to=created_to, sort_by=sort_by, sort_order=sort_order, sources=sources, business_unit_ids=business_unit_ids)

List Credential Attempt Logs

List all credential attempt log entries, ordered by attempted date.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.paginated_client_credentials_log import PaginatedClientCredentialsLog
from watchtowr_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://your-tenant-id.sg.client.watchtowr.io
# See configuration.py for a list of all supported configuration parameters.
configuration = watchtowr_api_sdk.Configuration(
    host = "https://your-tenant-id.sg.client.watchtowr.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API_TOKEN): bearer
configuration = watchtowr_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with watchtowr_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = watchtowr_api_sdk.CredentialAttemptLogsApi(api_client)
    page = 1 # float | Page number (optional) (default to 1)
    page_size = 10 # float | Number of items per page (optional) (default to 10)
    technologies = ['technologies_example'] # List[str] | Filter by technologies (optional)
    asset_name = 'asset_name_example' # str | Filter by asset name (supports partial matching) (optional)
    username = 'username_example' # str | Filter by username (supports partial matching) (optional)
    statuses = ['statuses_example'] # List[str] | Filter by statuses (optional)
    created_from = '2022-02-22T22:00:00.000Z' # str | Filter credential attempt logs created after a given date and time. (optional)
    created_to = '2022-02-23T22:00:00.000Z' # str | Filter credential attempt logs created before a given date and time. (optional)
    sort_by = attempted_at # str | Sort by field (optional) (default to attempted_at)
    sort_order = DESC # str | Sort order (optional) (default to DESC)
    sources = ['sources_example'] # List[str] | Filter by sources (optional)
    business_unit_ids = [3.4] # List[float] | Filter by business unit IDs (for users with business unit restrictions) (optional)

    try:
        # List Credential Attempt Logs
        api_response = api_instance.get_list_credential_attempt_logs(page=page, page_size=page_size, technologies=technologies, asset_name=asset_name, username=username, statuses=statuses, created_from=created_from, created_to=created_to, sort_by=sort_by, sort_order=sort_order, sources=sources, business_unit_ids=business_unit_ids)
        print("The response of CredentialAttemptLogsApi->get_list_credential_attempt_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialAttemptLogsApi->get_list_credential_attempt_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| Page number | [optional] [default to 1]
 **page_size** | **float**| Number of items per page | [optional] [default to 10]
 **technologies** | [**List[str]**](str.md)| Filter by technologies | [optional] 
 **asset_name** | **str**| Filter by asset name (supports partial matching) | [optional] 
 **username** | **str**| Filter by username (supports partial matching) | [optional] 
 **statuses** | [**List[str]**](str.md)| Filter by statuses | [optional] 
 **created_from** | **str**| Filter credential attempt logs created after a given date and time. | [optional] 
 **created_to** | **str**| Filter credential attempt logs created before a given date and time. | [optional] 
 **sort_by** | **str**| Sort by field | [optional] [default to attempted_at]
 **sort_order** | **str**| Sort order | [optional] [default to DESC]
 **sources** | [**List[str]**](str.md)| Filter by sources | [optional] 
 **business_unit_ids** | [**List[float]**](float.md)| Filter by business unit IDs (for users with business unit restrictions) | [optional] 

### Return type

[**PaginatedClientCredentialsLog**](PaginatedClientCredentialsLog.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

