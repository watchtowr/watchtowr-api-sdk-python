# openapi_client.ActivityLogApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_activity_logs**](ActivityLogApi.md#get_list_activity_logs) | **GET** /api/client/activity-log/list | List Activity Logs


# **get_list_activity_logs**
> PaginatedClientActivityLog get_list_activity_logs(page=page, page_size=page_size, created_from=created_from, created_to=created_to, types=types, search=search, user_ids=user_ids)

List Activity Logs

List all activity log entries, ordered by creation date.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.paginated_client_activity_log import PaginatedClientActivityLog
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://your-tenant-id.sg.client.watchtowr.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://your-tenant-id.sg.client.watchtowr.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API_TOKEN): bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ActivityLogApi(api_client)
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)
    created_from = '2022-02-22 22:00:00' # datetime | Filter logs created after a given date and time. (optional)
    created_to = '2022-02-23 22:00:00' # datetime | Filter logs created before a given date and time. (optional)
    types = ['UserInvite,UserRoleType,UserLock,ResetUser2FA,SetupSSO,UpdateUserSessionTimeout,SuccessfulLogin,PasswordResetTriggered,UserDelete,UserCreated,UserBusinessUnit,IntegrationSetUp,IntegrationUpdated,IntegrationDeleted,KillSwitch,FindingSetting,TestingInfrastructureUpdate,UpdatePriorityPort,PlatformIpWhitelist,AutomaticRetestsUpdated,ReportGenerated,ReportGenerationRequest,ReportDownloaded,AutomaticOutOfScope,PrismaCloudApigeeAccountRemoved,PrismaCloudAccountNameUpdate,ServiceAccountCreated,ServiceAccountUpdated,ServiceAccountDeleted,ServiceAccountEnabled,ServiceAccountDisabled,ServiceAccountTokenRegenerated'] # List[str] | Filter logs by a comma separated list of types. (optional)
    search = 'requested%20to%20generate%20technical%20report' # str | Search logs across various fields such as user, or description. (optional)
    user_ids = ['1,2,3'] # List[str] | Filter logs by a comma separated list of user IDs. (optional)

    try:
        # List Activity Logs
        api_response = api_instance.get_list_activity_logs(page=page, page_size=page_size, created_from=created_from, created_to=created_to, types=types, search=search, user_ids=user_ids)
        print("The response of ActivityLogApi->get_list_activity_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityLogApi->get_list_activity_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | [optional] 
 **created_from** | **datetime**| Filter logs created after a given date and time. | [optional] 
 **created_to** | **datetime**| Filter logs created before a given date and time. | [optional] 
 **types** | [**List[str]**](str.md)| Filter logs by a comma separated list of types. | [optional] 
 **search** | **str**| Search logs across various fields such as user, or description. | [optional] 
 **user_ids** | [**List[str]**](str.md)| Filter logs by a comma separated list of user IDs. | [optional] 

### Return type

[**PaginatedClientActivityLog**](PaginatedClientActivityLog.md)

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

