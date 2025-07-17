# watchtowr_api_sdk.SuspiciousDomainsApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_suspicious_domain**](SuspiciousDomainsApi.md#get_list_suspicious_domain) | **GET** /api/client/suspicious-domain/list | List Suspicious Domains
[**get_suspicious_domain_details**](SuspiciousDomainsApi.md#get_suspicious_domain_details) | **GET** /api/client/suspicious-domain/show/{id} | Get Suspicious Domain Details


# **get_list_suspicious_domain**
> PaginatedSuspiciousDomain get_list_suspicious_domain(page=page, page_size=page_size, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, search=search, discovery_reason=discovery_reason, whois_search=whois_search, statuses=statuses)

List Suspicious Domains

List all discovered suspicious domain assets, ordered by discovery date.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.paginated_suspicious_domain import PaginatedSuspiciousDomain
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
    api_instance = watchtowr_api_sdk.SuspiciousDomainsApi(api_client)
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)
    created_from = '2013-10-20T19:20:30+01:00' # datetime | Filter suspicious domains created after a given date and time. (optional)
    created_to = '2013-10-20T19:20:30+01:00' # datetime | Filter suspicious domains created before a given date and time. (optional)
    updated_from = '2013-10-20T19:20:30+01:00' # datetime | Filter suspicious domains updated after a given date and time. (optional)
    updated_to = '2013-10-20T19:20:30+01:00' # datetime | Filter suspicious domains updated before a given date and time. (optional)
    search = 'watchtowr.com' # str | Search suspicious domains by text within the domain. (optional)
    discovery_reason = 'suspicious-words' # str | Search suspicious domains by discovery reason. (optional)
    whois_search = 'Name%20Server:%20malicious.ns.com' # str | Search suspicious domains by contents of Whois data. (optional)
    statuses = 'pending,malicious,legitimate,benign' # str | Filter suspicious domains by a list of comma separated statuses that asset is tagged with. (optional)

    try:
        # List Suspicious Domains
        api_response = api_instance.get_list_suspicious_domain(page=page, page_size=page_size, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, search=search, discovery_reason=discovery_reason, whois_search=whois_search, statuses=statuses)
        print("The response of SuspiciousDomainsApi->get_list_suspicious_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuspiciousDomainsApi->get_list_suspicious_domain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | [optional] 
 **created_from** | **datetime**| Filter suspicious domains created after a given date and time. | [optional] 
 **created_to** | **datetime**| Filter suspicious domains created before a given date and time. | [optional] 
 **updated_from** | **datetime**| Filter suspicious domains updated after a given date and time. | [optional] 
 **updated_to** | **datetime**| Filter suspicious domains updated before a given date and time. | [optional] 
 **search** | **str**| Search suspicious domains by text within the domain. | [optional] 
 **discovery_reason** | **str**| Search suspicious domains by discovery reason. | [optional] 
 **whois_search** | **str**| Search suspicious domains by contents of Whois data. | [optional] 
 **statuses** | **str**| Filter suspicious domains by a list of comma separated statuses that asset is tagged with. | [optional] 

### Return type

[**PaginatedSuspiciousDomain**](PaginatedSuspiciousDomain.md)

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

# **get_suspicious_domain_details**
> ClientSuspiciousDomainData get_suspicious_domain_details(id)

Get Suspicious Domain Details

Get the details of a specific suspicious domain.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_suspicious_domain_data import ClientSuspiciousDomainData
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
    api_instance = watchtowr_api_sdk.SuspiciousDomainsApi(api_client)
    id = 3.4 # float | The ID of the suspicious domain to retrieve.

    try:
        # Get Suspicious Domain Details
        api_response = api_instance.get_suspicious_domain_details(id)
        print("The response of SuspiciousDomainsApi->get_suspicious_domain_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SuspiciousDomainsApi->get_suspicious_domain_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The ID of the suspicious domain to retrieve. | 

### Return type

[**ClientSuspiciousDomainData**](ClientSuspiciousDomainData.md)

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

