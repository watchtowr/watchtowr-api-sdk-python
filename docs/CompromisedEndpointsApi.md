# watchtowr_api_sdk.CompromisedEndpointsApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_compromised_endpoint_harvested_credentials**](CompromisedEndpointsApi.md#get_list_compromised_endpoint_harvested_credentials) | **GET** /api/client/compromised-endpoints/show/{id}/harvested-credentials | List Harvested Credentials
[**get_list_compromised_endpoints**](CompromisedEndpointsApi.md#get_list_compromised_endpoints) | **GET** /api/client/compromised-endpoints/list | List Compromised Endpoints


# **get_list_compromised_endpoint_harvested_credentials**
> PaginatedClientCompromisedEndpointHarvestedCredentials get_list_compromised_endpoint_harvested_credentials(id, page=page, page_size=page_size, query=query, usernames=usernames, sort_by=sort_by, sort_order=sort_order)

List Harvested Credentials

List paginated harvested credentials for a specified compromised endpoint.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.paginated_client_compromised_endpoint_harvested_credentials import PaginatedClientCompromisedEndpointHarvestedCredentials
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
    api_instance = watchtowr_api_sdk.CompromisedEndpointsApi(api_client)
    id = 3.4 # float | Compromised endpoint ID
    page = 1 # float | Page number (optional) (default to 1)
    page_size = 10 # float | Number of items per page (optional) (default to 10)
    query = 'query_example' # str | Filter by username or URL (partial matching) (optional)
    usernames = ['usernames_example'] # List[str] | Filter by usernames (optional)
    sort_by = username # str | Sort by field (optional) (default to username)
    sort_order = DESC # str | Sort order (optional) (default to DESC)

    try:
        # List Harvested Credentials
        api_response = api_instance.get_list_compromised_endpoint_harvested_credentials(id, page=page, page_size=page_size, query=query, usernames=usernames, sort_by=sort_by, sort_order=sort_order)
        print("The response of CompromisedEndpointsApi->get_list_compromised_endpoint_harvested_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompromisedEndpointsApi->get_list_compromised_endpoint_harvested_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| Compromised endpoint ID | 
 **page** | **float**| Page number | [optional] [default to 1]
 **page_size** | **float**| Number of items per page | [optional] [default to 10]
 **query** | **str**| Filter by username or URL (partial matching) | [optional] 
 **usernames** | [**List[str]**](str.md)| Filter by usernames | [optional] 
 **sort_by** | **str**| Sort by field | [optional] [default to username]
 **sort_order** | **str**| Sort order | [optional] [default to DESC]

### Return type

[**PaginatedClientCompromisedEndpointHarvestedCredentials**](PaginatedClientCompromisedEndpointHarvestedCredentials.md)

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
**404** | Compromised endpoint not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_compromised_endpoints**
> PaginatedClientCompromisedEndpoint get_list_compromised_endpoints(page=page, page_size=page_size, query=query, stealer_families=stealer_families, operating_systems=operating_systems, countries=countries, statuses=statuses, compromised_from=compromised_from, compromised_to=compromised_to, created_from=created_from, created_to=created_to, sort_by=sort_by, sort_order=sort_order)

List Compromised Endpoints

List all discovered compromised endpoints from data breaches and stealer malware, ordered by date compromised.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.paginated_client_compromised_endpoint import PaginatedClientCompromisedEndpoint
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
    api_instance = watchtowr_api_sdk.CompromisedEndpointsApi(api_client)
    page = 1 # float | Page number (optional) (default to 1)
    page_size = 10 # float | Number of items per page (optional) (default to 10)
    query = 'query_example' # str | Filter by hostname or IP address (supports partial matching) (optional)
    stealer_families = ['stealer_families_example'] # List[str] | Filter by stealer families (optional)
    operating_systems = ['operating_systems_example'] # List[str] | Filter by operating systems (optional)
    countries = ['countries_example'] # List[str] | Filter by countries (optional)
    statuses = ['statuses_example'] # List[str] | Filter by statuses (optional)
    compromised_from = '2022-02-22T22:00:00.000Z' # str | Filter compromised endpoints compromised after a given date and time. (optional)
    compromised_to = '2022-02-23T22:00:00.000Z' # str | Filter compromised endpoints compromised before a given date and time. (optional)
    created_from = '2022-02-22T22:00:00.000Z' # str | Filter compromised endpoints created after a given date and time. (optional)
    created_to = '2022-02-23T22:00:00.000Z' # str | Filter compromised endpoints created before a given date and time. (optional)
    sort_by = date_compromised # str | Sort by field (optional) (default to date_compromised)
    sort_order = DESC # str | Sort order (optional) (default to DESC)

    try:
        # List Compromised Endpoints
        api_response = api_instance.get_list_compromised_endpoints(page=page, page_size=page_size, query=query, stealer_families=stealer_families, operating_systems=operating_systems, countries=countries, statuses=statuses, compromised_from=compromised_from, compromised_to=compromised_to, created_from=created_from, created_to=created_to, sort_by=sort_by, sort_order=sort_order)
        print("The response of CompromisedEndpointsApi->get_list_compromised_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompromisedEndpointsApi->get_list_compromised_endpoints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| Page number | [optional] [default to 1]
 **page_size** | **float**| Number of items per page | [optional] [default to 10]
 **query** | **str**| Filter by hostname or IP address (supports partial matching) | [optional] 
 **stealer_families** | [**List[str]**](str.md)| Filter by stealer families | [optional] 
 **operating_systems** | [**List[str]**](str.md)| Filter by operating systems | [optional] 
 **countries** | [**List[str]**](str.md)| Filter by countries | [optional] 
 **statuses** | [**List[str]**](str.md)| Filter by statuses | [optional] 
 **compromised_from** | **str**| Filter compromised endpoints compromised after a given date and time. | [optional] 
 **compromised_to** | **str**| Filter compromised endpoints compromised before a given date and time. | [optional] 
 **created_from** | **str**| Filter compromised endpoints created after a given date and time. | [optional] 
 **created_to** | **str**| Filter compromised endpoints created before a given date and time. | [optional] 
 **sort_by** | **str**| Sort by field | [optional] [default to date_compromised]
 **sort_order** | **str**| Sort order | [optional] [default to DESC]

### Return type

[**PaginatedClientCompromisedEndpoint**](PaginatedClientCompromisedEndpoint.md)

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

