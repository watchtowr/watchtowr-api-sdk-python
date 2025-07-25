# watchtowr_api_sdk.AddAssetApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submit_asset**](AddAssetApi.md#submit_asset) | **POST** /api/client/seeddata | Submit Seed Data


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

