# watchtowr_api_sdk.PendingDomainsApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_pending_domains**](PendingDomainsApi.md#get_list_pending_domains) | **GET** /api/client/pending-domains/list | List Pending Domains


# **get_list_pending_domains**
> PaginatedClientPendingDomain get_list_pending_domains(page=page, page_size=page_size, name=name, source=source, start_date=start_date, end_date=end_date, sort_by=sort_by, sort_order=sort_order)

List Pending Domains

List all pending domain assets with filtering and pagination support.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.paginated_client_pending_domain import PaginatedClientPendingDomain
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
    api_instance = watchtowr_api_sdk.PendingDomainsApi(api_client)
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 100. (optional)
    name = 'example.com' # str | Filter by domain name (optional)
    source = 'example-source' # str | Filter by source that discovered the domain (optional)
    start_date = '2023-01-01T00:00Z' # datetime | Filter by start date (ISO format) (optional)
    end_date = '2023-12-31T23:59:59.999Z' # datetime | Filter by end date (ISO format) (optional)
    sort_by = created_at # str | Sort by field (optional) (default to created_at)
    sort_order = DESC # str | Sort order (optional) (default to DESC)

    try:
        # List Pending Domains
        api_response = api_instance.get_list_pending_domains(page=page, page_size=page_size, name=name, source=source, start_date=start_date, end_date=end_date, sort_by=sort_by, sort_order=sort_order)
        print("The response of PendingDomainsApi->get_list_pending_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PendingDomainsApi->get_list_pending_domains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 100. | [optional] 
 **name** | **str**| Filter by domain name | [optional] 
 **source** | **str**| Filter by source that discovered the domain | [optional] 
 **start_date** | **datetime**| Filter by start date (ISO format) | [optional] 
 **end_date** | **datetime**| Filter by end date (ISO format) | [optional] 
 **sort_by** | **str**| Sort by field | [optional] [default to created_at]
 **sort_order** | **str**| Sort order | [optional] [default to DESC]

### Return type

[**PaginatedClientPendingDomain**](PaginatedClientPendingDomain.md)

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

