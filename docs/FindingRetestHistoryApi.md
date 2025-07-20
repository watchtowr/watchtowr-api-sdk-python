# watchtowr_api_sdk.FindingRetestHistoryApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_finding_retest_history**](FindingRetestHistoryApi.md#get_list_finding_retest_history) | **GET** /api/client/finding-retest-history/list | List Finding Retest History


# **get_list_finding_retest_history**
> PaginatedClientFindingRetestHistory get_list_finding_retest_history(page=page, page_size=page_size, business_unit_ids=business_unit_ids, sort_by=sort_by, sort_order=sort_order)

List Finding Retest History

List all finding retest history entries, ordered by creation date.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.paginated_client_finding_retest_history import PaginatedClientFindingRetestHistory
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
    api_instance = watchtowr_api_sdk.FindingRetestHistoryApi(api_client)
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)
    business_unit_ids = '1,2,3' # str | Filter assets by a list of comma separated business unit IDs that the asset is related to. (optional)
    sort_by = created_at # str | Sort by field (optional) (default to created_at)
    sort_order = DESC # str | Sort order (optional) (default to DESC)

    try:
        # List Finding Retest History
        api_response = api_instance.get_list_finding_retest_history(page=page, page_size=page_size, business_unit_ids=business_unit_ids, sort_by=sort_by, sort_order=sort_order)
        print("The response of FindingRetestHistoryApi->get_list_finding_retest_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingRetestHistoryApi->get_list_finding_retest_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | [optional] 
 **business_unit_ids** | **str**| Filter assets by a list of comma separated business unit IDs that the asset is related to. | [optional] 
 **sort_by** | **str**| Sort by field | [optional] [default to created_at]
 **sort_order** | **str**| Sort order | [optional] [default to DESC]

### Return type

[**PaginatedClientFindingRetestHistory**](PaginatedClientFindingRetestHistory.md)

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

