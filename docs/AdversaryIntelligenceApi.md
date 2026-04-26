# watchtowr_api_sdk.AdversaryIntelligenceApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_adversary_intelligence_details**](AdversaryIntelligenceApi.md#get_adversary_intelligence_details) | **GET** /api/client/adversary-intelligence/show/{attackerId} | Get Adversary Details
[**get_list_adversary_intelligence**](AdversaryIntelligenceApi.md#get_list_adversary_intelligence) | **GET** /api/client/adversary-intelligence/list | List Adversaries


# **get_adversary_intelligence_details**
> ClientAdversaryIntelData get_adversary_intelligence_details(attacker_id)

Get Adversary Details

Get the details of a specific adversary by attacker ID. The `isAffected` flag and `affectedKbEntryIds` are scoped to the requesting user’s business units and the organization’s finding impact threshold.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_adversary_intel_data import ClientAdversaryIntelData
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
    api_instance = watchtowr_api_sdk.AdversaryIntelligenceApi(api_client)
    attacker_id = 3.4 # float | The numeric attacker ID of the adversary to retrieve.

    try:
        # Get Adversary Details
        api_response = api_instance.get_adversary_intelligence_details(attacker_id)
        print("The response of AdversaryIntelligenceApi->get_adversary_intelligence_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdversaryIntelligenceApi->get_adversary_intelligence_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attacker_id** | **float**| The numeric attacker ID of the adversary to retrieve. | 

### Return type

[**ClientAdversaryIntelData**](ClientAdversaryIntelData.md)

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
**404** | Adversary not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_adversary_intelligence**
> PaginatedAdversaryIntel get_list_adversary_intelligence(page=page, page_size=page_size, search=search)

List Adversaries

List adversaries (threat actors) tracked by the watchTowr Adversary Intelligence engine. The `isAffected` flag is scoped to the requesting user’s business units and the organization’s finding impact threshold.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.paginated_adversary_intel import PaginatedAdversaryIntel
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
    api_instance = watchtowr_api_sdk.AdversaryIntelligenceApi(api_client)
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)
    search = 'Cl0p' # str | Search adversaries by name or alias. (optional)

    try:
        # List Adversaries
        api_response = api_instance.get_list_adversary_intelligence(page=page, page_size=page_size, search=search)
        print("The response of AdversaryIntelligenceApi->get_list_adversary_intelligence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdversaryIntelligenceApi->get_list_adversary_intelligence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | [optional] 
 **search** | **str**| Search adversaries by name or alias. | [optional] 

### Return type

[**PaginatedAdversaryIntel**](PaginatedAdversaryIntel.md)

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

