# watchtowr_api_sdk.ServiceDiscoveryApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_service_listing**](ServiceDiscoveryApi.md#get_list_service_listing) | **GET** /api/client/service-listing/list | List Services


# **get_list_service_listing**
> PaginatedServiceListing get_list_service_listing(page=page, page_size=page_size, include_closed_port=include_closed_port, include_no_service=include_no_service, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, search=search, countries=countries, technology=technology, ports=ports, port_numbers=port_numbers, port_types=port_types, port_services=port_services, service_type_ids=service_type_ids, business_unit_ids=business_unit_ids, sort_by=sort_by, order_by=order_by, suppression_filter=suppression_filter)

List Services

List all discovered service assets, ordered by last seen date.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.paginated_service_listing import PaginatedServiceListing
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
    api_instance = watchtowr_api_sdk.ServiceDiscoveryApi(api_client)
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)
    include_closed_port = True # bool | Include listings with closed ports. (optional)
    include_no_service = True # bool | Include listings without a service (optional)
    created_from = '2013-10-20T19:20:30+01:00' # datetime | Filter services created after a given date and time. (optional)
    created_to = '2013-10-20T19:20:30+01:00' # datetime | Filter services created before a given date and time. (optional)
    updated_from = '2013-10-20T19:20:30+01:00' # datetime | Filter services updated after a given date and time. (optional)
    updated_to = '2013-10-20T19:20:30+01:00' # datetime | Filter services updated before a given date and time. (optional)
    search = '1.2.3.4' # str | Search services by IP address. (optional)
    countries = 'US,UK' # str | Filter services by a list of comma separated subject countries that they're related to. (optional)
    technology = 'react' # str | Filter services by technology name. (optional)
    ports = '22/TCP,443/TCP,3389/UDP' # str | Filter services by a list of comma separated port/protocols. (optional)
    port_numbers = '80,443' # str | Filter services by a list of comma separated ports. (optional)
    port_types = 'TCP,UDP' # str | Filter services by a list of comma separated transport layer protocols (e.g. UDP/TCP). (optional)
    port_services = 'SSH,HTTP' # str | Filter services by a list of comma separated services. (optional)
    service_type_ids = '1,2,3' # str | Filter services by a list of comma separated service type IDs. (optional)
    business_unit_ids = '1,2,3' # str | Filter services by a list of comma separated business unit IDs they're related to. (optional)
    sort_by = 'last_seen' # str | Sort services. (optional)
    order_by = 'DESC' # str | Order services. (optional)
    suppression_filter = 'non-suppressed' # str | Filter services by suppression status. (optional)

    try:
        # List Services
        api_response = api_instance.get_list_service_listing(page=page, page_size=page_size, include_closed_port=include_closed_port, include_no_service=include_no_service, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, search=search, countries=countries, technology=technology, ports=ports, port_numbers=port_numbers, port_types=port_types, port_services=port_services, service_type_ids=service_type_ids, business_unit_ids=business_unit_ids, sort_by=sort_by, order_by=order_by, suppression_filter=suppression_filter)
        print("The response of ServiceDiscoveryApi->get_list_service_listing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceDiscoveryApi->get_list_service_listing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | [optional] 
 **include_closed_port** | **bool**| Include listings with closed ports. | [optional] 
 **include_no_service** | **bool**| Include listings without a service | [optional] 
 **created_from** | **datetime**| Filter services created after a given date and time. | [optional] 
 **created_to** | **datetime**| Filter services created before a given date and time. | [optional] 
 **updated_from** | **datetime**| Filter services updated after a given date and time. | [optional] 
 **updated_to** | **datetime**| Filter services updated before a given date and time. | [optional] 
 **search** | **str**| Search services by IP address. | [optional] 
 **countries** | **str**| Filter services by a list of comma separated subject countries that they&#39;re related to. | [optional] 
 **technology** | **str**| Filter services by technology name. | [optional] 
 **ports** | **str**| Filter services by a list of comma separated port/protocols. | [optional] 
 **port_numbers** | **str**| Filter services by a list of comma separated ports. | [optional] 
 **port_types** | **str**| Filter services by a list of comma separated transport layer protocols (e.g. UDP/TCP). | [optional] 
 **port_services** | **str**| Filter services by a list of comma separated services. | [optional] 
 **service_type_ids** | **str**| Filter services by a list of comma separated service type IDs. | [optional] 
 **business_unit_ids** | **str**| Filter services by a list of comma separated business unit IDs they&#39;re related to. | [optional] 
 **sort_by** | **str**| Sort services. | [optional] 
 **order_by** | **str**| Order services. | [optional] 
 **suppression_filter** | **str**| Filter services by suppression status. | [optional] 

### Return type

[**PaginatedServiceListing**](PaginatedServiceListing.md)

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

