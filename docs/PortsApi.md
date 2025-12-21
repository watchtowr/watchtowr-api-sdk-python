# watchtowr_api_sdk.PortsApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_port_details**](PortsApi.md#get_asset_port_details) | **GET** /api/client/assets/ip/port/show/{id} | Get Port
[**get_list_asset_ports**](PortsApi.md#get_list_asset_ports) | **GET** /api/client/assets/ip/port/list | List Ports


# **get_asset_port_details**
> ClientPortData get_asset_port_details(id)

Get Port

Get the details of a specific Port asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_port_data import ClientPortData
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
    api_instance = watchtowr_api_sdk.PortsApi(api_client)
    id = 3.4 # float | The asset ID of a Port to get.

    try:
        # Get Port
        api_response = api_instance.get_asset_port_details(id)
        print("The response of PortsApi->get_asset_port_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->get_asset_port_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of a Port to get. | 

### Return type

[**ClientPortData**](ClientPortData.md)

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

# **get_list_asset_ports**
> PaginatedClientPort get_list_asset_ports(page=page, page_size=page_size, include_closed_port=include_closed_port, include_no_service=include_no_service, created_from=created_from, created_to=created_to, asset_name=asset_name, business_unit_ids=business_unit_ids, custom_property_key=custom_property_key, custom_property_value=custom_property_value)

List Ports

List all discovered Ports for all IP Addresses, ordered by date identified.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.paginated_client_port import PaginatedClientPort
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
    api_instance = watchtowr_api_sdk.PortsApi(api_client)
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 100. (optional)
    include_closed_port = True # bool | Include listings with closed ports. (optional)
    include_no_service = True # bool | Include listings without a service (optional)
    created_from = '2013-10-20T19:20:30+01:00' # datetime | Filter ports created after a given date and time. (optional)
    created_to = '2013-10-20T19:20:30+01:00' # datetime | Filter ports created before a given date and time. (optional)
    asset_name = '80' # str | Search ports by port number. (optional)
    business_unit_ids = '1,2,3' # str | Filter assets by a list of comma separated business unit IDs that the asset is related to. (optional)
    custom_property_key = 'environment' # str | Filter assets by custom property key. (optional)
    custom_property_value = 'production' # str | Filter assets by custom property value. Must be used together with customPropertyKey. (optional)

    try:
        # List Ports
        api_response = api_instance.get_list_asset_ports(page=page, page_size=page_size, include_closed_port=include_closed_port, include_no_service=include_no_service, created_from=created_from, created_to=created_to, asset_name=asset_name, business_unit_ids=business_unit_ids, custom_property_key=custom_property_key, custom_property_value=custom_property_value)
        print("The response of PortsApi->get_list_asset_ports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortsApi->get_list_asset_ports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 100. | [optional] 
 **include_closed_port** | **bool**| Include listings with closed ports. | [optional] 
 **include_no_service** | **bool**| Include listings without a service | [optional] 
 **created_from** | **datetime**| Filter ports created after a given date and time. | [optional] 
 **created_to** | **datetime**| Filter ports created before a given date and time. | [optional] 
 **asset_name** | **str**| Search ports by port number. | [optional] 
 **business_unit_ids** | **str**| Filter assets by a list of comma separated business unit IDs that the asset is related to. | [optional] 
 **custom_property_key** | **str**| Filter assets by custom property key. | [optional] 
 **custom_property_value** | **str**| Filter assets by custom property value. Must be used together with customPropertyKey. | [optional] 

### Return type

[**PaginatedClientPort**](PaginatedClientPort.md)

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

