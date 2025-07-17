# watchtowr_api_sdk.HuntsApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client_hunts**](HuntsApi.md#get_client_hunts) | **GET** /api/client/hunts/list | List Hunts
[**get_list_asset_by_hunt**](HuntsApi.md#get_list_asset_by_hunt) | **GET** /api/client/hunts/show/{id}/assets | List Assets
[**get_list_finding_by_hunt**](HuntsApi.md#get_list_finding_by_hunt) | **GET** /api/client/hunts/show/{id}/findings | List Hunt Findings
[**show_the_detail_hunt**](HuntsApi.md#show_the_detail_hunt) | **GET** /api/client/hunts/show/{id} | Get Hunt Details


# **get_client_hunts**
> PaginatedHunts get_client_hunts(page=page, page_size=page_size, statuses=statuses, hunt_search=hunt_search, types=types, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, priorities=priorities, general=general)

List Hunts

List all available hunt assets, ordered by creation date.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.paginated_hunts import PaginatedHunts
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
    api_instance = watchtowr_api_sdk.HuntsApi(api_client)
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)
    statuses = 'statuses_example' # str | Filter hunts by hunt status. (optional)
    hunt_search = 'remote%20code%20execution' # str | Search for hunts by text in hunt name. (optional)
    types = 'types_example' # str | Filter hunts by hunt types. (optional)
    created_from = '2013-10-20T19:20:30+01:00' # datetime | Filter hunts created after a given date and time. (optional)
    created_to = '2013-10-20T19:20:30+01:00' # datetime | Filter hunts created before a given date and time. (optional)
    updated_from = '2013-10-20T19:20:30+01:00' # datetime | Filter hunts updated after a given date and time. (optional)
    updated_to = '2013-10-20T19:20:30+01:00' # datetime | Filter hunts updated before a given date and time. (optional)
    priorities = 'priorities_example' # str | Filter hunts by hunt priority. (optional)
    general = 'general_example' # str | General (optional)

    try:
        # List Hunts
        api_response = api_instance.get_client_hunts(page=page, page_size=page_size, statuses=statuses, hunt_search=hunt_search, types=types, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, priorities=priorities, general=general)
        print("The response of HuntsApi->get_client_hunts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HuntsApi->get_client_hunts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | [optional] 
 **statuses** | **str**| Filter hunts by hunt status. | [optional] 
 **hunt_search** | **str**| Search for hunts by text in hunt name. | [optional] 
 **types** | **str**| Filter hunts by hunt types. | [optional] 
 **created_from** | **datetime**| Filter hunts created after a given date and time. | [optional] 
 **created_to** | **datetime**| Filter hunts created before a given date and time. | [optional] 
 **updated_from** | **datetime**| Filter hunts updated after a given date and time. | [optional] 
 **updated_to** | **datetime**| Filter hunts updated before a given date and time. | [optional] 
 **priorities** | **str**| Filter hunts by hunt priority. | [optional] 
 **general** | **str**| General | [optional] 

### Return type

[**PaginatedHunts**](PaginatedHunts.md)

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

# **get_list_asset_by_hunt**
> AssetsListResponse get_list_asset_by_hunt(id, page=page, page_size=page_size)

List Assets

Get a list of Assets for a specific Hunt.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.assets_list_response import AssetsListResponse
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
    api_instance = watchtowr_api_sdk.HuntsApi(api_client)
    id = 3.4 # float | Hunt ID of the hunt to retrieve assets from.
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)

    try:
        # List Assets
        api_response = api_instance.get_list_asset_by_hunt(id, page=page, page_size=page_size)
        print("The response of HuntsApi->get_list_asset_by_hunt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HuntsApi->get_list_asset_by_hunt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Hunt ID of the hunt to retrieve assets from. | 
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | [optional] 

### Return type

[**AssetsListResponse**](AssetsListResponse.md)

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

# **get_list_finding_by_hunt**
> FindingListResponse get_list_finding_by_hunt(id, page=page, page_size=page_size)

List Hunt Findings

List all findings for a specific hunt.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.finding_list_response import FindingListResponse
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
    api_instance = watchtowr_api_sdk.HuntsApi(api_client)
    id = 3.4 # float | The ID of the hunt to retrieve findings from.
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)

    try:
        # List Hunt Findings
        api_response = api_instance.get_list_finding_by_hunt(id, page=page, page_size=page_size)
        print("The response of HuntsApi->get_list_finding_by_hunt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HuntsApi->get_list_finding_by_hunt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The ID of the hunt to retrieve findings from. | 
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | [optional] 

### Return type

[**FindingListResponse**](FindingListResponse.md)

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

# **show_the_detail_hunt**
> HuntDetailResponse show_the_detail_hunt(id)

Get Hunt Details

Get the details of a specific hunt.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.hunt_detail_response import HuntDetailResponse
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
    api_instance = watchtowr_api_sdk.HuntsApi(api_client)
    id = 3.4 # float | The ID of the hunt to retrieve.

    try:
        # Get Hunt Details
        api_response = api_instance.show_the_detail_hunt(id)
        print("The response of HuntsApi->show_the_detail_hunt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HuntsApi->show_the_detail_hunt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The ID of the hunt to retrieve. | 

### Return type

[**HuntDetailResponse**](HuntDetailResponse.md)

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

