# watchtowr_api_sdk.AddAssetApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_submitted_assets**](AddAssetApi.md#list_submitted_assets) | **GET** /api/client/seeddata/list | List Submitted Assets
[**submit_asset**](AddAssetApi.md#submit_asset) | **POST** /api/client/seeddata | Submit Seed Data


# **list_submitted_assets**
> PaginatedClientSeedData list_submitted_assets(page=page, page_size=page_size, business_unit_ids=business_unit_ids)

List Submitted Assets

List all submitted seed data assets with pagination and filtering support.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.paginated_client_seed_data import PaginatedClientSeedData
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
    api_instance = watchtowr_api_sdk.AddAssetApi(api_client)
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 20 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 20. The maximum for pageSize is 100. (optional)
    business_unit_ids = '1,2,3' # str | Filter by a list of comma separated business unit IDs that the seed data is related to. (optional)

    try:
        # List Submitted Assets
        api_response = api_instance.list_submitted_assets(page=page, page_size=page_size, business_unit_ids=business_unit_ids)
        print("The response of AddAssetApi->list_submitted_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddAssetApi->list_submitted_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 20. The maximum for pageSize is 100. | [optional] 
 **business_unit_ids** | **str**| Filter by a list of comma separated business unit IDs that the seed data is related to. | [optional] 

### Return type

[**PaginatedClientSeedData**](PaginatedClientSeedData.md)

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

# **submit_asset**
> ClientSeedDataData submit_asset(create_client_seed_data_request_body)

Submit Seed Data

Submit one or more seed data assets to your attack surface for review.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_seed_data_data import ClientSeedDataData
from watchtowr_api_sdk.models.create_client_seed_data_request_body import CreateClientSeedDataRequestBody
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
    api_instance = watchtowr_api_sdk.AddAssetApi(api_client)
    create_client_seed_data_request_body = watchtowr_api_sdk.CreateClientSeedDataRequestBody() # CreateClientSeedDataRequestBody | 

    try:
        # Submit Seed Data
        api_response = api_instance.submit_asset(create_client_seed_data_request_body)
        print("The response of AddAssetApi->submit_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddAssetApi->submit_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_client_seed_data_request_body** | [**CreateClientSeedDataRequestBody**](CreateClientSeedDataRequestBody.md)|  | 

### Return type

[**ClientSeedDataData**](ClientSeedDataData.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

