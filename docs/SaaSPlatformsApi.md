# watchtowr_api_sdk.SaaSPlatformsApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_saas_platform_to_business_units**](SaaSPlatformsApi.md#assign_saas_platform_to_business_units) | **POST** /api/client/assets/saasPlatform/show/{id}/business-units | Assign SaaS Platform to Business Units
[**create_custom_property_saas_platform**](SaaSPlatformsApi.md#create_custom_property_saas_platform) | **POST** /api/client/assets/saasPlatform/show/{id}/custom-property | Create Custom Property
[**create_note_saas_platform**](SaaSPlatformsApi.md#create_note_saas_platform) | **POST** /api/client/assets/saasPlatform/show/{id}/note | Create Note
[**delete_custom_property_saas_platform**](SaaSPlatformsApi.md#delete_custom_property_saas_platform) | **DELETE** /api/client/assets/saasPlatform/show/{id}/custom-property/{customPropertyId} | Delete Custom Property
[**delete_note_saas_platform**](SaaSPlatformsApi.md#delete_note_saas_platform) | **DELETE** /api/client/assets/saasPlatform/show/{id}/note/{noteId} | Delete Note
[**get_asset_saas_platform_details**](SaaSPlatformsApi.md#get_asset_saas_platform_details) | **GET** /api/client/assets/saasPlatform/show/{id} | Get SaaS Platform
[**get_asset_saas_platform_notes**](SaaSPlatformsApi.md#get_asset_saas_platform_notes) | **GET** /api/client/assets/saasPlatform/show/{id}/notes | List Notes
[**get_custom_properties_saas_platform**](SaaSPlatformsApi.md#get_custom_properties_saas_platform) | **GET** /api/client/assets/saasPlatform/show/{id}/custom-properties | List Custom Properties
[**get_list_asset_saas_platforms**](SaaSPlatformsApi.md#get_list_asset_saas_platforms) | **GET** /api/client/assets/saasPlatform/list | List SaaS Platforms
[**unassign_saas_platform_from_business_units**](SaaSPlatformsApi.md#unassign_saas_platform_from_business_units) | **DELETE** /api/client/assets/saasPlatform/show/{id}/business-units | Unassign SaaS Platform from Business Units
[**update_asset_saas_platform_status**](SaaSPlatformsApi.md#update_asset_saas_platform_status) | **PUT** /api/client/assets/saasPlatform/update-status/{id} | Update Status
[**update_custom_property_saas_platform**](SaaSPlatformsApi.md#update_custom_property_saas_platform) | **PUT** /api/client/assets/saasPlatform/show/{id}/custom-property/{customPropertyId} | Update Custom Property
[**update_note_saas_platform**](SaaSPlatformsApi.md#update_note_saas_platform) | **PUT** /api/client/assets/saasPlatform/show/{id}/note/{noteId} | Update Note


# **assign_saas_platform_to_business_units**
> ClientSaasPlatformData assign_saas_platform_to_business_units(id, asset_business_unit_ids_dto)

Assign SaaS Platform to Business Units

Assign a specific SaaS Platform asset to a list of Business Units

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.asset_business_unit_ids_dto import AssetBusinessUnitIdsDTO
from watchtowr_api_sdk.models.client_saas_platform_data import ClientSaasPlatformData
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
    api_instance = watchtowr_api_sdk.SaaSPlatformsApi(api_client)
    id = 3.4 # float | The SaaS Platform asset's ID.
    asset_business_unit_ids_dto = watchtowr_api_sdk.AssetBusinessUnitIdsDTO() # AssetBusinessUnitIdsDTO | 

    try:
        # Assign SaaS Platform to Business Units
        api_response = api_instance.assign_saas_platform_to_business_units(id, asset_business_unit_ids_dto)
        print("The response of SaaSPlatformsApi->assign_saas_platform_to_business_units:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaaSPlatformsApi->assign_saas_platform_to_business_units: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The SaaS Platform asset&#39;s ID. | 
 **asset_business_unit_ids_dto** | [**AssetBusinessUnitIdsDTO**](AssetBusinessUnitIdsDTO.md)|  | 

### Return type

[**ClientSaasPlatformData**](ClientSaasPlatformData.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_custom_property_saas_platform**
> ClientCustomProperty create_custom_property_saas_platform(id, create_client_custom_property_dto)

Create Custom Property

Create a Custom Property for a specific SaaS Platform asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_custom_property import ClientCustomProperty
from watchtowr_api_sdk.models.create_client_custom_property_dto import CreateClientCustomPropertyDto
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
    api_instance = watchtowr_api_sdk.SaaSPlatformsApi(api_client)
    id = 3.4 # float | The asset ID of the SaaS Platform to create a new custom property for.
    create_client_custom_property_dto = watchtowr_api_sdk.CreateClientCustomPropertyDto() # CreateClientCustomPropertyDto | 

    try:
        # Create Custom Property
        api_response = api_instance.create_custom_property_saas_platform(id, create_client_custom_property_dto)
        print("The response of SaaSPlatformsApi->create_custom_property_saas_platform:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaaSPlatformsApi->create_custom_property_saas_platform: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the SaaS Platform to create a new custom property for. | 
 **create_client_custom_property_dto** | [**CreateClientCustomPropertyDto**](CreateClientCustomPropertyDto.md)|  | 

### Return type

[**ClientCustomProperty**](ClientCustomProperty.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_note_saas_platform**
> ClientNoteData create_note_saas_platform(id, create_client_note_dto)

Create Note

Create a Note for a specific SaaS Platform asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_note_data import ClientNoteData
from watchtowr_api_sdk.models.create_client_note_dto import CreateClientNoteDto
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
    api_instance = watchtowr_api_sdk.SaaSPlatformsApi(api_client)
    id = 3.4 # float | The asset ID of the SaaS Platform to create a new note for.
    create_client_note_dto = watchtowr_api_sdk.CreateClientNoteDto() # CreateClientNoteDto | 

    try:
        # Create Note
        api_response = api_instance.create_note_saas_platform(id, create_client_note_dto)
        print("The response of SaaSPlatformsApi->create_note_saas_platform:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaaSPlatformsApi->create_note_saas_platform: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the SaaS Platform to create a new note for. | 
 **create_client_note_dto** | [**CreateClientNoteDto**](CreateClientNoteDto.md)|  | 

### Return type

[**ClientNoteData**](ClientNoteData.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_property_saas_platform**
> RemoveClientCustomPropertyResponseDto delete_custom_property_saas_platform(id, custom_property_id)

Delete Custom Property

Delete a Custom Property for a specific SaaS Platform asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.remove_client_custom_property_response_dto import RemoveClientCustomPropertyResponseDto
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
    api_instance = watchtowr_api_sdk.SaaSPlatformsApi(api_client)
    id = 3.4 # float | The asset ID of a SaaS Platform with a custom property to delete.
    custom_property_id = 3.4 # float | The ID of the custom property to delete.

    try:
        # Delete Custom Property
        api_response = api_instance.delete_custom_property_saas_platform(id, custom_property_id)
        print("The response of SaaSPlatformsApi->delete_custom_property_saas_platform:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaaSPlatformsApi->delete_custom_property_saas_platform: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of a SaaS Platform with a custom property to delete. | 
 **custom_property_id** | **float**| The ID of the custom property to delete. | 

### Return type

[**RemoveClientCustomPropertyResponseDto**](RemoveClientCustomPropertyResponseDto.md)

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

# **delete_note_saas_platform**
> DeleteNoteSucces delete_note_saas_platform(id, note_id)

Delete Note

Delete a Note for a specific SaaS Platform asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.delete_note_succes import DeleteNoteSucces
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
    api_instance = watchtowr_api_sdk.SaaSPlatformsApi(api_client)
    id = 3.4 # float | The asset ID of a SaaS Platform with a note to delete.
    note_id = 3.4 # float | The ID of the note to delete.

    try:
        # Delete Note
        api_response = api_instance.delete_note_saas_platform(id, note_id)
        print("The response of SaaSPlatformsApi->delete_note_saas_platform:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaaSPlatformsApi->delete_note_saas_platform: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of a SaaS Platform with a note to delete. | 
 **note_id** | **float**| The ID of the note to delete. | 

### Return type

[**DeleteNoteSucces**](DeleteNoteSucces.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_saas_platform_details**
> ClientSaasPlatformData get_asset_saas_platform_details(id)

Get SaaS Platform

Get the details of a specific SaaS Platform.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_saas_platform_data import ClientSaasPlatformData
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
    api_instance = watchtowr_api_sdk.SaaSPlatformsApi(api_client)
    id = 3.4 # float | The asset ID of the SaaS Platform to get.

    try:
        # Get SaaS Platform
        api_response = api_instance.get_asset_saas_platform_details(id)
        print("The response of SaaSPlatformsApi->get_asset_saas_platform_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaaSPlatformsApi->get_asset_saas_platform_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the SaaS Platform to get. | 

### Return type

[**ClientSaasPlatformData**](ClientSaasPlatformData.md)

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

# **get_asset_saas_platform_notes**
> ClientNoteListData get_asset_saas_platform_notes(id, page=page, page_size=page_size)

List Notes

List the Notes of a specific SaaS Platform asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_note_list_data import ClientNoteListData
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
    api_instance = watchtowr_api_sdk.SaaSPlatformsApi(api_client)
    id = 3.4 # float | The asset ID of the SaaS Platform to list notes of.
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)

    try:
        # List Notes
        api_response = api_instance.get_asset_saas_platform_notes(id, page=page, page_size=page_size)
        print("The response of SaaSPlatformsApi->get_asset_saas_platform_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaaSPlatformsApi->get_asset_saas_platform_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the SaaS Platform to list notes of. | 
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | [optional] 

### Return type

[**ClientNoteListData**](ClientNoteListData.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_properties_saas_platform**
> PaginatedClientCustomProperty get_custom_properties_saas_platform(id, page=page, page_size=page_size)

List Custom Properties

List the Custom Properties of a specific SaaS Platform asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.paginated_client_custom_property import PaginatedClientCustomProperty
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
    api_instance = watchtowr_api_sdk.SaaSPlatformsApi(api_client)
    id = 3.4 # float | The asset ID of the SaaS Platform to list custom properties of.
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)

    try:
        # List Custom Properties
        api_response = api_instance.get_custom_properties_saas_platform(id, page=page, page_size=page_size)
        print("The response of SaaSPlatformsApi->get_custom_properties_saas_platform:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaaSPlatformsApi->get_custom_properties_saas_platform: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the SaaS Platform to list custom properties of. | 
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | [optional] 

### Return type

[**PaginatedClientCustomProperty**](PaginatedClientCustomProperty.md)

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

# **get_list_asset_saas_platforms**
> PaginatedClientSaasPlatform get_list_asset_saas_platforms(page=page, page_size=page_size, asset_name=asset_name, statuses=statuses, source=source, integration_connections=integration_connections, business_unit_ids=business_unit_ids, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, custom_property_key=custom_property_key, custom_property_value=custom_property_value)

List SaaS Platforms

List all discovered SaaS Platforms, ordered by date identified.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.paginated_client_saas_platform import PaginatedClientSaasPlatform
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
    api_instance = watchtowr_api_sdk.SaaSPlatformsApi(api_client)
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)
    asset_name = 'example.slack.com' # str | Search SaaS platforms by URL. (optional)
    statuses = ['statuses_example'] # List[str] | Filter assets by one or more comma separated asset statuses. Valid statuses are:       * verified       * tracked       * incorrect identification       * pending       * verifiedOutOfScope  (optional)
    source = 'module-adversarysight-postman-workspace-saas-discovery' # str | Filter assets by the source that discovered the asset. (optional)
    integration_connections = '123:aws,456:azure,789:googlecloud' # str | Filter assets by integration connections (comma-separated list of integrationId:integrationType pairs).  Valid integration types: aws, googlecloud, azure, cloudflare, alibabacloud, prismacloud, prismacloudapigee, huaweicloud, tencentcloud, wiz, servicenowcmdb, akamaiedge, armiscentrix, qualysvmdr, tenable  Format: integrationId:integrationType (e.g., 123:aws) Multiple connections: separate with commas (e.g., 123:aws,456:azure,789:googlecloud) (optional)
    business_unit_ids = '1,2,3' # str | Filter assets by a list of comma separated business unit IDs that the asset is related to. (optional)
    created_from = '2013-10-20T19:20:30+01:00' # datetime | Filter assets created after a given date and time. (optional)
    created_to = '2013-10-20T19:20:30+01:00' # datetime | Filter assets created before a given date and time. (optional)
    updated_from = '2013-10-20T19:20:30+01:00' # datetime | Filter assets updated after a given date and time. (optional)
    updated_to = '2013-10-20T19:20:30+01:00' # datetime | Filter assets updated before a given date and time. (optional)
    custom_property_key = 'environment' # str | Filter assets by custom property key. (optional)
    custom_property_value = 'production' # str | Filter assets by custom property value. Must be used together with customPropertyKey. (optional)

    try:
        # List SaaS Platforms
        api_response = api_instance.get_list_asset_saas_platforms(page=page, page_size=page_size, asset_name=asset_name, statuses=statuses, source=source, integration_connections=integration_connections, business_unit_ids=business_unit_ids, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, custom_property_key=custom_property_key, custom_property_value=custom_property_value)
        print("The response of SaaSPlatformsApi->get_list_asset_saas_platforms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaaSPlatformsApi->get_list_asset_saas_platforms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | [optional] 
 **asset_name** | **str**| Search SaaS platforms by URL. | [optional] 
 **statuses** | [**List[str]**](str.md)| Filter assets by one or more comma separated asset statuses. Valid statuses are:       * verified       * tracked       * incorrect identification       * pending       * verifiedOutOfScope  | [optional] 
 **source** | **str**| Filter assets by the source that discovered the asset. | [optional] 
 **integration_connections** | **str**| Filter assets by integration connections (comma-separated list of integrationId:integrationType pairs).  Valid integration types: aws, googlecloud, azure, cloudflare, alibabacloud, prismacloud, prismacloudapigee, huaweicloud, tencentcloud, wiz, servicenowcmdb, akamaiedge, armiscentrix, qualysvmdr, tenable  Format: integrationId:integrationType (e.g., 123:aws) Multiple connections: separate with commas (e.g., 123:aws,456:azure,789:googlecloud) | [optional] 
 **business_unit_ids** | **str**| Filter assets by a list of comma separated business unit IDs that the asset is related to. | [optional] 
 **created_from** | **datetime**| Filter assets created after a given date and time. | [optional] 
 **created_to** | **datetime**| Filter assets created before a given date and time. | [optional] 
 **updated_from** | **datetime**| Filter assets updated after a given date and time. | [optional] 
 **updated_to** | **datetime**| Filter assets updated before a given date and time. | [optional] 
 **custom_property_key** | **str**| Filter assets by custom property key. | [optional] 
 **custom_property_value** | **str**| Filter assets by custom property value. Must be used together with customPropertyKey. | [optional] 

### Return type

[**PaginatedClientSaasPlatform**](PaginatedClientSaasPlatform.md)

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

# **unassign_saas_platform_from_business_units**
> ClientSaasPlatformData unassign_saas_platform_from_business_units(id, business_unit_ids)

Unassign SaaS Platform from Business Units

Unassign a specific SaaS Platform asset from a list of Business Units

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_saas_platform_data import ClientSaasPlatformData
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
    api_instance = watchtowr_api_sdk.SaaSPlatformsApi(api_client)
    id = 3.4 # float | The SaaS Platform asset's ID.
    business_unit_ids = ['business_unit_ids_example'] # List[str] | List of comma-seperated business unit IDs to unassign from the asset.

    try:
        # Unassign SaaS Platform from Business Units
        api_response = api_instance.unassign_saas_platform_from_business_units(id, business_unit_ids)
        print("The response of SaaSPlatformsApi->unassign_saas_platform_from_business_units:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaaSPlatformsApi->unassign_saas_platform_from_business_units: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The SaaS Platform asset&#39;s ID. | 
 **business_unit_ids** | [**List[str]**](str.md)| List of comma-seperated business unit IDs to unassign from the asset. | 

### Return type

[**ClientSaasPlatformData**](ClientSaasPlatformData.md)

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
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_saas_platform_status**
> ClientSaasPlatformData update_asset_saas_platform_status(id, update_client_next_gen_asset_status_dto)

Update Status

Update Status of a specific SaaS Platform asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_saas_platform_data import ClientSaasPlatformData
from watchtowr_api_sdk.models.update_client_next_gen_asset_status_dto import UpdateClientNextGenAssetStatusDto
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
    api_instance = watchtowr_api_sdk.SaaSPlatformsApi(api_client)
    id = 3.4 # float | The asset ID of the SaaS Platform to update status of.
    update_client_next_gen_asset_status_dto = watchtowr_api_sdk.UpdateClientNextGenAssetStatusDto() # UpdateClientNextGenAssetStatusDto | 

    try:
        # Update Status
        api_response = api_instance.update_asset_saas_platform_status(id, update_client_next_gen_asset_status_dto)
        print("The response of SaaSPlatformsApi->update_asset_saas_platform_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaaSPlatformsApi->update_asset_saas_platform_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the SaaS Platform to update status of. | 
 **update_client_next_gen_asset_status_dto** | [**UpdateClientNextGenAssetStatusDto**](UpdateClientNextGenAssetStatusDto.md)|  | 

### Return type

[**ClientSaasPlatformData**](ClientSaasPlatformData.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_property_saas_platform**
> ClientCustomProperty update_custom_property_saas_platform(id, custom_property_id, update_client_custom_property_dto)

Update Custom Property

Update a Custom Property for a specific SaaS Platform asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_custom_property import ClientCustomProperty
from watchtowr_api_sdk.models.update_client_custom_property_dto import UpdateClientCustomPropertyDto
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
    api_instance = watchtowr_api_sdk.SaaSPlatformsApi(api_client)
    id = 3.4 # float | The asset ID of a SaaS Platform with a custom property to update.
    custom_property_id = 3.4 # float | The ID of the custom property to update.
    update_client_custom_property_dto = watchtowr_api_sdk.UpdateClientCustomPropertyDto() # UpdateClientCustomPropertyDto | 

    try:
        # Update Custom Property
        api_response = api_instance.update_custom_property_saas_platform(id, custom_property_id, update_client_custom_property_dto)
        print("The response of SaaSPlatformsApi->update_custom_property_saas_platform:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaaSPlatformsApi->update_custom_property_saas_platform: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of a SaaS Platform with a custom property to update. | 
 **custom_property_id** | **float**| The ID of the custom property to update. | 
 **update_client_custom_property_dto** | [**UpdateClientCustomPropertyDto**](UpdateClientCustomPropertyDto.md)|  | 

### Return type

[**ClientCustomProperty**](ClientCustomProperty.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_note_saas_platform**
> ClientNoteData update_note_saas_platform(id, note_id, create_client_note_dto)

Update Note

Update a Note for a specific SaaS Platform asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_note_data import ClientNoteData
from watchtowr_api_sdk.models.create_client_note_dto import CreateClientNoteDto
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
    api_instance = watchtowr_api_sdk.SaaSPlatformsApi(api_client)
    id = 3.4 # float | The asset ID of a SaaS Platform with a note to update.
    note_id = 3.4 # float | The ID of the note to update.
    create_client_note_dto = watchtowr_api_sdk.CreateClientNoteDto() # CreateClientNoteDto | 

    try:
        # Update Note
        api_response = api_instance.update_note_saas_platform(id, note_id, create_client_note_dto)
        print("The response of SaaSPlatformsApi->update_note_saas_platform:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaaSPlatformsApi->update_note_saas_platform: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of a SaaS Platform with a note to update. | 
 **note_id** | **float**| The ID of the note to update. | 
 **create_client_note_dto** | [**CreateClientNoteDto**](CreateClientNoteDto.md)|  | 

### Return type

[**ClientNoteData**](ClientNoteData.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

