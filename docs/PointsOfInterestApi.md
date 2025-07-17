# watchtowr_api_sdk.PointsOfInterestApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_points_of_interest**](PointsOfInterestApi.md#get_list_points_of_interest) | **GET** /api/client/points-of-interest/list | List Points of Interest


# **get_list_points_of_interest**
> PaginatedPointOfInterest get_list_points_of_interest(page=page, page_size=page_size, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, discovered_date_order=discovered_date_order, search=search, types=types, has_finding=has_finding, start_date=start_date, end_date=end_date, asset_statuses=asset_statuses, business_unit_ids=business_unit_ids)

List Points of Interest

List all discovered Points of Interest assets, ordered by discovery date.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.paginated_point_of_interest import PaginatedPointOfInterest
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
    api_instance = watchtowr_api_sdk.PointsOfInterestApi(api_client)
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)
    created_from = '2013-10-20T19:20:30+01:00' # datetime | Filter points of interest created after a given date and time. (optional)
    created_to = '2013-10-20T19:20:30+01:00' # datetime | Filter points of interest created before a given date and time. (optional)
    updated_from = '2013-10-20T19:20:30+01:00' # datetime | Filter points of interest updated after a given date and time. (optional)
    updated_to = '2013-10-20T19:20:30+01:00' # datetime | Filter points of interest updated before a given date and time. (optional)
    discovered_date_order = 'DESC' # str | Order points of interest by their discovery date. (optional)
    search = 'Apache%20Airflow%20Admin%20Login' # str | Search Points of Interest by name or URL. (optional)
    types = 'admin-panel,open-directory' # str | Filter by a comma separated list of types. (optional)
    has_finding = false # bool | Filter points of interest that have findings. (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Filter points of interest by start date. (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Filter points of interest by end date. (optional)
    asset_statuses = 'verified,Unregistered,Parked,Incorrect Identification,pending,VerifiedOutOfScope,VerifiedReducedAttack,Tracked,CDN,Hanging Cloud IP,VerifiedHoneypot,Third Party' # str | Filter points of interest by a comma separated list of asset statuses. (optional)
    business_unit_ids = '1,2,3' # str | Filter points of interest by a comma separated list of business unit IDs. (optional)

    try:
        # List Points of Interest
        api_response = api_instance.get_list_points_of_interest(page=page, page_size=page_size, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, discovered_date_order=discovered_date_order, search=search, types=types, has_finding=has_finding, start_date=start_date, end_date=end_date, asset_statuses=asset_statuses, business_unit_ids=business_unit_ids)
        print("The response of PointsOfInterestApi->get_list_points_of_interest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsOfInterestApi->get_list_points_of_interest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | [optional] 
 **created_from** | **datetime**| Filter points of interest created after a given date and time. | [optional] 
 **created_to** | **datetime**| Filter points of interest created before a given date and time. | [optional] 
 **updated_from** | **datetime**| Filter points of interest updated after a given date and time. | [optional] 
 **updated_to** | **datetime**| Filter points of interest updated before a given date and time. | [optional] 
 **discovered_date_order** | **str**| Order points of interest by their discovery date. | [optional] 
 **search** | **str**| Search Points of Interest by name or URL. | [optional] 
 **types** | **str**| Filter by a comma separated list of types. | [optional] 
 **has_finding** | **bool**| Filter points of interest that have findings. | [optional] 
 **start_date** | **datetime**| Filter points of interest by start date. | [optional] 
 **end_date** | **datetime**| Filter points of interest by end date. | [optional] 
 **asset_statuses** | **str**| Filter points of interest by a comma separated list of asset statuses. | [optional] 
 **business_unit_ids** | **str**| Filter points of interest by a comma separated list of business unit IDs. | [optional] 

### Return type

[**PaginatedPointOfInterest**](PaginatedPointOfInterest.md)

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

