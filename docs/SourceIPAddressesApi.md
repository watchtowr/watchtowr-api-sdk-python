# openapi_client.SourceIPAddressesApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_source_ip_addresses**](SourceIPAddressesApi.md#get_list_source_ip_addresses) | **GET** /api/client/testing-infrastructure | List Testing Infrastructure


# **get_list_source_ip_addresses**
> ClientSourceIpsAddresses get_list_source_ip_addresses(whitelist=whitelist, region=region)

List Testing Infrastructure

List IP addresses and hostnames used by watchTowr for all outbound platform traffic.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.client_source_ips_addresses import ClientSourceIpsAddresses
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://your-tenant-id.sg.client.watchtowr.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://your-tenant-id.sg.client.watchtowr.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API_TOKEN): bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SourceIPAddressesApi(api_client)
    whitelist = True # bool | Filter by whitelist status (true for whitelisted items only) (optional)
    region = 'region_example' # str | Filter by region (optional)

    try:
        # List Testing Infrastructure
        api_response = api_instance.get_list_source_ip_addresses(whitelist=whitelist, region=region)
        print("The response of SourceIPAddressesApi->get_list_source_ip_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceIPAddressesApi->get_list_source_ip_addresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **whitelist** | **bool**| Filter by whitelist status (true for whitelisted items only) | [optional] 
 **region** | **str**| Filter by region | [optional] 

### Return type

[**ClientSourceIpsAddresses**](ClientSourceIpsAddresses.md)

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

