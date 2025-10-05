# watchtowr_api_sdk.UserManagementApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_details**](UserManagementApi.md#get_user_details) | **GET** /api/client/users/show/{id} | Get User Details
[**list_users**](UserManagementApi.md#list_users) | **GET** /api/client/users/list | List Users


# **get_user_details**
> UserDetailData get_user_details(id)

Get User Details

Get detailed information about a specific user. Administrator role required.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.user_detail_data import UserDetailData
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
    api_instance = watchtowr_api_sdk.UserManagementApi(api_client)
    id = 3.4 # float | 

    try:
        # Get User Details
        api_response = api_instance.get_user_details(id)
        print("The response of UserManagementApi->get_user_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->get_user_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 

### Return type

[**UserDetailData**](UserDetailData.md)

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
**403** | Forbidden - Administrator role required |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> PaginatedUsers list_users(page=page, page_size=page_size, name=name, title=title, status=status, role_ids=role_ids, created_from=created_from, created_to=created_to)

List Users

Get a paginated list of users with filtering. Administrator role required.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.paginated_users import PaginatedUsers
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
    api_instance = watchtowr_api_sdk.UserManagementApi(api_client)
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)
    name = 'John Doe' # str | Search by user name (optional)
    title = 'Security Manager' # str | Search by user title (optional)
    status = ['[\"Active\"]'] # List[str] | Filter by user status (optional)
    role_ids = [[1,2]] # List[float] | Filter by role IDs (optional)
    created_from = '2023-01-01T00:00:00Z' # str | Filter by creation date start (optional)
    created_to = '2023-12-31T23:59:59Z' # str | Filter by creation date end (optional)

    try:
        # List Users
        api_response = api_instance.list_users(page=page, page_size=page_size, name=name, title=title, status=status, role_ids=role_ids, created_from=created_from, created_to=created_to)
        print("The response of UserManagementApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | [optional] 
 **name** | **str**| Search by user name | [optional] 
 **title** | **str**| Search by user title | [optional] 
 **status** | [**List[str]**](str.md)| Filter by user status | [optional] 
 **role_ids** | [**List[float]**](float.md)| Filter by role IDs | [optional] 
 **created_from** | **str**| Filter by creation date start | [optional] 
 **created_to** | **str**| Filter by creation date end | [optional] 

### Return type

[**PaginatedUsers**](PaginatedUsers.md)

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
**403** | Forbidden - Administrator role required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

