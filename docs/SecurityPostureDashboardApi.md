# watchtowr_api_sdk.SecurityPostureDashboardApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_security_posture_dashboard**](SecurityPostureDashboardApi.md#get_security_posture_dashboard) | **GET** /api/client/dashboard/security-posture | Get Security Posture Dashboard


# **get_security_posture_dashboard**
> SecurityPostureDashboardResponse get_security_posture_dashboard()

Get Security Posture Dashboard

Retrieve consolidated security posture dashboard statistics

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.security_posture_dashboard_response import SecurityPostureDashboardResponse
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
    api_instance = watchtowr_api_sdk.SecurityPostureDashboardApi(api_client)

    try:
        # Get Security Posture Dashboard
        api_response = api_instance.get_security_posture_dashboard()
        print("The response of SecurityPostureDashboardApi->get_security_posture_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityPostureDashboardApi->get_security_posture_dashboard: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SecurityPostureDashboardResponse**](SecurityPostureDashboardResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

