# watchtowr_api_sdk.KillSwitchApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_kill_switch_status**](KillSwitchApi.md#get_kill_switch_status) | **GET** /api/client/kill-switch | Get Kill Switch Status
[**update_kill_switch**](KillSwitchApi.md#update_kill_switch) | **PUT** /api/client/kill-switch | Update Kill Switch


# **get_kill_switch_status**
> KillSwitchStatusData get_kill_switch_status()

Get Kill Switch Status

Get the current status of the kill switch and whether client control is allowed.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.kill_switch_status_data import KillSwitchStatusData
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
    api_instance = watchtowr_api_sdk.KillSwitchApi(api_client)

    try:
        # Get Kill Switch Status
        api_response = api_instance.get_kill_switch_status()
        print("The response of KillSwitchApi->get_kill_switch_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KillSwitchApi->get_kill_switch_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**KillSwitchStatusData**](KillSwitchStatusData.md)

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
**403** | Forbidden - Administrator or User role required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kill_switch**
> UpdateKillSwitchData update_kill_switch(update_kill_switch_request_dto)

Update Kill Switch

Enable or disable the kill switch. Administrator or User role required.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.update_kill_switch_data import UpdateKillSwitchData
from watchtowr_api_sdk.models.update_kill_switch_request_dto import UpdateKillSwitchRequestDto
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
    api_instance = watchtowr_api_sdk.KillSwitchApi(api_client)
    update_kill_switch_request_dto = watchtowr_api_sdk.UpdateKillSwitchRequestDto() # UpdateKillSwitchRequestDto | 

    try:
        # Update Kill Switch
        api_response = api_instance.update_kill_switch(update_kill_switch_request_dto)
        print("The response of KillSwitchApi->update_kill_switch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KillSwitchApi->update_kill_switch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_kill_switch_request_dto** | [**UpdateKillSwitchRequestDto**](UpdateKillSwitchRequestDto.md)|  | 

### Return type

[**UpdateKillSwitchData**](UpdateKillSwitchData.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Kill switch updated successfully |  -  |
**400** | Bad Request - Kill switch control not allowed |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - Administrator or User role required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

