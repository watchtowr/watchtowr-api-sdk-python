# watchtowr_api_sdk.BusinessUnitApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_business_unit_details**](BusinessUnitApi.md#get_business_unit_details) | **GET** /api/client/business-unit/show/{id} | Get Business Unit Details
[**get_list_business_unit**](BusinessUnitApi.md#get_list_business_unit) | **GET** /api/client/business-unit/list | List Business Units


# **get_business_unit_details**
> ClientBusinessUnitData get_business_unit_details(id)

Get Business Unit Details

Get the details of a specific business unit.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_business_unit_data import ClientBusinessUnitData
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
    api_instance = watchtowr_api_sdk.BusinessUnitApi(api_client)
    id = 3.4 # float | 

    try:
        # Get Business Unit Details
        api_response = api_instance.get_business_unit_details(id)
        print("The response of BusinessUnitApi->get_business_unit_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessUnitApi->get_business_unit_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 

### Return type

[**ClientBusinessUnitData**](ClientBusinessUnitData.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_business_unit**
> PaginatedBusinessUnit get_list_business_unit(page=page, page_size=page_size, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, search=search)

List Business Units

List all business units available to the current user.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.paginated_business_unit import PaginatedBusinessUnit
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
    api_instance = watchtowr_api_sdk.BusinessUnitApi(api_client)
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)
    created_from = '2013-10-20T19:20:30+01:00' # datetime | Filter business units created after a given date and time. (optional)
    created_to = '2013-10-20T19:20:30+01:00' # datetime | Filter business units created before a given date and time. (optional)
    updated_from = '2013-10-20T19:20:30+01:00' # datetime | Filter business units updated after a given date and time. (optional)
    updated_to = '2013-10-20T19:20:30+01:00' # datetime | Filter business units updated before a given date and time. (optional)
    search = 'Singapore Business Unit' # str | Search business units by name. (optional)

    try:
        # List Business Units
        api_response = api_instance.get_list_business_unit(page=page, page_size=page_size, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, search=search)
        print("The response of BusinessUnitApi->get_list_business_unit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessUnitApi->get_list_business_unit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | [optional] 
 **created_from** | **datetime**| Filter business units created after a given date and time. | [optional] 
 **created_to** | **datetime**| Filter business units created before a given date and time. | [optional] 
 **updated_from** | **datetime**| Filter business units updated after a given date and time. | [optional] 
 **updated_to** | **datetime**| Filter business units updated before a given date and time. | [optional] 
 **search** | **str**| Search business units by name. | [optional] 

### Return type

[**PaginatedBusinessUnit**](PaginatedBusinessUnit.md)

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

