# watchtowr_api_sdk.PlatformWhitelistingApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_platform_api_whitelist_ip**](PlatformWhitelistingApi.md#create_platform_api_whitelist_ip) | **POST** /api/client/platform/whitelisting/api | Add API Whitelisted IP
[**create_platform_dashboard_whitelist_ip**](PlatformWhitelistingApi.md#create_platform_dashboard_whitelist_ip) | **POST** /api/client/platform/whitelisting/dashboard | Add Dashboard Whitelisted IP
[**delete_platform_api_whitelist_ip**](PlatformWhitelistingApi.md#delete_platform_api_whitelist_ip) | **DELETE** /api/client/platform/whitelisting/api/{id} | Remove API Whitelisted IP
[**delete_platform_dashboard_whitelist_ip**](PlatformWhitelistingApi.md#delete_platform_dashboard_whitelist_ip) | **DELETE** /api/client/platform/whitelisting/dashboard/{id} | Remove Dashboard Whitelisted IP
[**get_platform_api_whitelist_ips**](PlatformWhitelistingApi.md#get_platform_api_whitelist_ips) | **GET** /api/client/platform/whitelisting/api | List API Whitelisted IPs
[**get_platform_api_whitelist_status**](PlatformWhitelistingApi.md#get_platform_api_whitelist_status) | **GET** /api/client/platform/whitelisting/api/status | Get API Whitelisting Status
[**get_platform_dashboard_whitelist_ips**](PlatformWhitelistingApi.md#get_platform_dashboard_whitelist_ips) | **GET** /api/client/platform/whitelisting/dashboard | List Dashboard Whitelisted IPs
[**get_platform_dashboard_whitelist_status**](PlatformWhitelistingApi.md#get_platform_dashboard_whitelist_status) | **GET** /api/client/platform/whitelisting/dashboard/status | Get Dashboard Whitelisting Status
[**update_platform_api_whitelist_ip**](PlatformWhitelistingApi.md#update_platform_api_whitelist_ip) | **PUT** /api/client/platform/whitelisting/api/{id} | Update API Whitelisted IP
[**update_platform_api_whitelist_status**](PlatformWhitelistingApi.md#update_platform_api_whitelist_status) | **PUT** /api/client/platform/whitelisting/api/status | Update API Whitelisting Status
[**update_platform_dashboard_whitelist_ip**](PlatformWhitelistingApi.md#update_platform_dashboard_whitelist_ip) | **PUT** /api/client/platform/whitelisting/dashboard/{id} | Update Dashboard Whitelisted IP
[**update_platform_dashboard_whitelist_status**](PlatformWhitelistingApi.md#update_platform_dashboard_whitelist_status) | **PUT** /api/client/platform/whitelisting/dashboard/status | Update Dashboard Whitelisting Status


# **create_platform_api_whitelist_ip**
> WhitelistIpDataSingle create_platform_api_whitelist_ip(create_organisation_whitelist_ip_dto)

Add API Whitelisted IP

Add a new IP address to the API whitelist. Admin role required.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.create_organisation_whitelist_ip_dto import CreateOrganisationWhitelistIpDto
from watchtowr_api_sdk.models.whitelist_ip_data_single import WhitelistIpDataSingle
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
    api_instance = watchtowr_api_sdk.PlatformWhitelistingApi(api_client)
    create_organisation_whitelist_ip_dto = watchtowr_api_sdk.CreateOrganisationWhitelistIpDto() # CreateOrganisationWhitelistIpDto | 

    try:
        # Add API Whitelisted IP
        api_response = api_instance.create_platform_api_whitelist_ip(create_organisation_whitelist_ip_dto)
        print("The response of PlatformWhitelistingApi->create_platform_api_whitelist_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformWhitelistingApi->create_platform_api_whitelist_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_organisation_whitelist_ip_dto** | [**CreateOrganisationWhitelistIpDto**](CreateOrganisationWhitelistIpDto.md)|  | 

### Return type

[**WhitelistIpDataSingle**](WhitelistIpDataSingle.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - Admin role required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_platform_dashboard_whitelist_ip**
> WhitelistIpDataSingle create_platform_dashboard_whitelist_ip(create_organisation_whitelist_ip_dto)

Add Dashboard Whitelisted IP

Add a new IP address to the dashboard whitelist. Admin role required.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.create_organisation_whitelist_ip_dto import CreateOrganisationWhitelistIpDto
from watchtowr_api_sdk.models.whitelist_ip_data_single import WhitelistIpDataSingle
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
    api_instance = watchtowr_api_sdk.PlatformWhitelistingApi(api_client)
    create_organisation_whitelist_ip_dto = watchtowr_api_sdk.CreateOrganisationWhitelistIpDto() # CreateOrganisationWhitelistIpDto | 

    try:
        # Add Dashboard Whitelisted IP
        api_response = api_instance.create_platform_dashboard_whitelist_ip(create_organisation_whitelist_ip_dto)
        print("The response of PlatformWhitelistingApi->create_platform_dashboard_whitelist_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformWhitelistingApi->create_platform_dashboard_whitelist_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_organisation_whitelist_ip_dto** | [**CreateOrganisationWhitelistIpDto**](CreateOrganisationWhitelistIpDto.md)|  | 

### Return type

[**WhitelistIpDataSingle**](WhitelistIpDataSingle.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - Admin role required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_platform_api_whitelist_ip**
> DeleteWhitelistIpData delete_platform_api_whitelist_ip(id)

Remove API Whitelisted IP

Remove an IP address from the API whitelist. Admin role required.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.delete_whitelist_ip_data import DeleteWhitelistIpData
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
    api_instance = watchtowr_api_sdk.PlatformWhitelistingApi(api_client)
    id = 3.4 # float | 

    try:
        # Remove API Whitelisted IP
        api_response = api_instance.delete_platform_api_whitelist_ip(id)
        print("The response of PlatformWhitelistingApi->delete_platform_api_whitelist_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformWhitelistingApi->delete_platform_api_whitelist_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 

### Return type

[**DeleteWhitelistIpData**](DeleteWhitelistIpData.md)

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
**403** | Forbidden - Admin role required |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_platform_dashboard_whitelist_ip**
> DeleteWhitelistIpData delete_platform_dashboard_whitelist_ip(id)

Remove Dashboard Whitelisted IP

Remove an IP address from the dashboard whitelist. Admin role required.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.delete_whitelist_ip_data import DeleteWhitelistIpData
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
    api_instance = watchtowr_api_sdk.PlatformWhitelistingApi(api_client)
    id = 3.4 # float | 

    try:
        # Remove Dashboard Whitelisted IP
        api_response = api_instance.delete_platform_dashboard_whitelist_ip(id)
        print("The response of PlatformWhitelistingApi->delete_platform_dashboard_whitelist_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformWhitelistingApi->delete_platform_dashboard_whitelist_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 

### Return type

[**DeleteWhitelistIpData**](DeleteWhitelistIpData.md)

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
**403** | Forbidden - Admin role required |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_platform_api_whitelist_ips**
> WhitelistIpListData get_platform_api_whitelist_ips()

List API Whitelisted IPs

Get all IP addresses whitelisted for API access. Admin role required.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.whitelist_ip_list_data import WhitelistIpListData
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
    api_instance = watchtowr_api_sdk.PlatformWhitelistingApi(api_client)

    try:
        # List API Whitelisted IPs
        api_response = api_instance.get_platform_api_whitelist_ips()
        print("The response of PlatformWhitelistingApi->get_platform_api_whitelist_ips:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformWhitelistingApi->get_platform_api_whitelist_ips: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WhitelistIpListData**](WhitelistIpListData.md)

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
**403** | Forbidden - Admin role required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_platform_api_whitelist_status**
> WhitelistStatusData get_platform_api_whitelist_status()

Get API Whitelisting Status

Get the current status of API IP whitelisting. Admin role required.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.whitelist_status_data import WhitelistStatusData
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
    api_instance = watchtowr_api_sdk.PlatformWhitelistingApi(api_client)

    try:
        # Get API Whitelisting Status
        api_response = api_instance.get_platform_api_whitelist_status()
        print("The response of PlatformWhitelistingApi->get_platform_api_whitelist_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformWhitelistingApi->get_platform_api_whitelist_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WhitelistStatusData**](WhitelistStatusData.md)

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
**403** | Forbidden - Admin role required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_platform_dashboard_whitelist_ips**
> WhitelistIpListData get_platform_dashboard_whitelist_ips()

List Dashboard Whitelisted IPs

Get all IP addresses whitelisted for dashboard access. Admin role required.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.whitelist_ip_list_data import WhitelistIpListData
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
    api_instance = watchtowr_api_sdk.PlatformWhitelistingApi(api_client)

    try:
        # List Dashboard Whitelisted IPs
        api_response = api_instance.get_platform_dashboard_whitelist_ips()
        print("The response of PlatformWhitelistingApi->get_platform_dashboard_whitelist_ips:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformWhitelistingApi->get_platform_dashboard_whitelist_ips: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WhitelistIpListData**](WhitelistIpListData.md)

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
**403** | Forbidden - Admin role required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_platform_dashboard_whitelist_status**
> WhitelistStatusData get_platform_dashboard_whitelist_status()

Get Dashboard Whitelisting Status

Get the current status of dashboard IP whitelisting. Admin role required.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.whitelist_status_data import WhitelistStatusData
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
    api_instance = watchtowr_api_sdk.PlatformWhitelistingApi(api_client)

    try:
        # Get Dashboard Whitelisting Status
        api_response = api_instance.get_platform_dashboard_whitelist_status()
        print("The response of PlatformWhitelistingApi->get_platform_dashboard_whitelist_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformWhitelistingApi->get_platform_dashboard_whitelist_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WhitelistStatusData**](WhitelistStatusData.md)

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
**403** | Forbidden - Admin role required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_platform_api_whitelist_ip**
> WhitelistIpDataSingle update_platform_api_whitelist_ip(id, update_organisation_whitelist_ip_dto)

Update API Whitelisted IP

Update an existing API whitelisted IP address. Admin role required.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.update_organisation_whitelist_ip_dto import UpdateOrganisationWhitelistIpDto
from watchtowr_api_sdk.models.whitelist_ip_data_single import WhitelistIpDataSingle
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
    api_instance = watchtowr_api_sdk.PlatformWhitelistingApi(api_client)
    id = 3.4 # float | 
    update_organisation_whitelist_ip_dto = watchtowr_api_sdk.UpdateOrganisationWhitelistIpDto() # UpdateOrganisationWhitelistIpDto | 

    try:
        # Update API Whitelisted IP
        api_response = api_instance.update_platform_api_whitelist_ip(id, update_organisation_whitelist_ip_dto)
        print("The response of PlatformWhitelistingApi->update_platform_api_whitelist_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformWhitelistingApi->update_platform_api_whitelist_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 
 **update_organisation_whitelist_ip_dto** | [**UpdateOrganisationWhitelistIpDto**](UpdateOrganisationWhitelistIpDto.md)|  | 

### Return type

[**WhitelistIpDataSingle**](WhitelistIpDataSingle.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - Admin role required |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_platform_api_whitelist_status**
> WhitelistStatusData update_platform_api_whitelist_status(whitelist_status_dto)

Update API Whitelisting Status

Enable or disable API IP whitelisting. Admin role required.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.whitelist_status_data import WhitelistStatusData
from watchtowr_api_sdk.models.whitelist_status_dto import WhitelistStatusDto
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
    api_instance = watchtowr_api_sdk.PlatformWhitelistingApi(api_client)
    whitelist_status_dto = watchtowr_api_sdk.WhitelistStatusDto() # WhitelistStatusDto | 

    try:
        # Update API Whitelisting Status
        api_response = api_instance.update_platform_api_whitelist_status(whitelist_status_dto)
        print("The response of PlatformWhitelistingApi->update_platform_api_whitelist_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformWhitelistingApi->update_platform_api_whitelist_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **whitelist_status_dto** | [**WhitelistStatusDto**](WhitelistStatusDto.md)|  | 

### Return type

[**WhitelistStatusData**](WhitelistStatusData.md)

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
**403** | Forbidden - Admin role required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_platform_dashboard_whitelist_ip**
> WhitelistIpDataSingle update_platform_dashboard_whitelist_ip(id, update_organisation_whitelist_ip_dto)

Update Dashboard Whitelisted IP

Update an existing dashboard whitelisted IP address. Admin role required.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.update_organisation_whitelist_ip_dto import UpdateOrganisationWhitelistIpDto
from watchtowr_api_sdk.models.whitelist_ip_data_single import WhitelistIpDataSingle
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
    api_instance = watchtowr_api_sdk.PlatformWhitelistingApi(api_client)
    id = 3.4 # float | 
    update_organisation_whitelist_ip_dto = watchtowr_api_sdk.UpdateOrganisationWhitelistIpDto() # UpdateOrganisationWhitelistIpDto | 

    try:
        # Update Dashboard Whitelisted IP
        api_response = api_instance.update_platform_dashboard_whitelist_ip(id, update_organisation_whitelist_ip_dto)
        print("The response of PlatformWhitelistingApi->update_platform_dashboard_whitelist_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformWhitelistingApi->update_platform_dashboard_whitelist_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | 
 **update_organisation_whitelist_ip_dto** | [**UpdateOrganisationWhitelistIpDto**](UpdateOrganisationWhitelistIpDto.md)|  | 

### Return type

[**WhitelistIpDataSingle**](WhitelistIpDataSingle.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden - Admin role required |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_platform_dashboard_whitelist_status**
> WhitelistStatusData update_platform_dashboard_whitelist_status(whitelist_status_dto)

Update Dashboard Whitelisting Status

Enable or disable dashboard IP whitelisting. Admin role required.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.whitelist_status_data import WhitelistStatusData
from watchtowr_api_sdk.models.whitelist_status_dto import WhitelistStatusDto
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
    api_instance = watchtowr_api_sdk.PlatformWhitelistingApi(api_client)
    whitelist_status_dto = watchtowr_api_sdk.WhitelistStatusDto() # WhitelistStatusDto | 

    try:
        # Update Dashboard Whitelisting Status
        api_response = api_instance.update_platform_dashboard_whitelist_status(whitelist_status_dto)
        print("The response of PlatformWhitelistingApi->update_platform_dashboard_whitelist_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlatformWhitelistingApi->update_platform_dashboard_whitelist_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **whitelist_status_dto** | [**WhitelistStatusDto**](WhitelistStatusDto.md)|  | 

### Return type

[**WhitelistStatusData**](WhitelistStatusData.md)

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
**403** | Forbidden - Admin role required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

