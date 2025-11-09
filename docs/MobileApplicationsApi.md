# watchtowr_api_sdk.MobileApplicationsApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_mobile_app_to_business_units**](MobileApplicationsApi.md#assign_mobile_app_to_business_units) | **POST** /api/client/assets/mobileApp/show/{id}/business-units | Assign Mobile App to Business Units
[**create_custom_property_mobile_app**](MobileApplicationsApi.md#create_custom_property_mobile_app) | **POST** /api/client/assets/mobileApp/show/{id}/custom-property | Create Custom Property
[**create_note_mobile_app**](MobileApplicationsApi.md#create_note_mobile_app) | **POST** /api/client/assets/mobileApp/show/{id}/note | Create Note
[**delete_custom_property_mobile_app**](MobileApplicationsApi.md#delete_custom_property_mobile_app) | **DELETE** /api/client/assets/mobileApp/show/{id}/custom-property/{customPropertyId} | Delete Custom Property
[**delete_note_mobile_app**](MobileApplicationsApi.md#delete_note_mobile_app) | **DELETE** /api/client/assets/mobileApp/show/{id}/note/{noteId} | Delete Note
[**get_asset_mobile_app_details**](MobileApplicationsApi.md#get_asset_mobile_app_details) | **GET** /api/client/assets/mobileApp/show/{id} | Get Mobile Application
[**get_asset_mobile_app_notes**](MobileApplicationsApi.md#get_asset_mobile_app_notes) | **GET** /api/client/assets/mobileApp/show/{id}/notes | List Notes
[**get_custom_properties_mobile_app**](MobileApplicationsApi.md#get_custom_properties_mobile_app) | **GET** /api/client/assets/mobileApp/show/{id}/custom-properties | List Custom Properties
[**get_list_asset_mobile_apps**](MobileApplicationsApi.md#get_list_asset_mobile_apps) | **GET** /api/client/assets/mobileApp/list | List Mobile Applications
[**unassign_mobile_app_from_business_units**](MobileApplicationsApi.md#unassign_mobile_app_from_business_units) | **DELETE** /api/client/assets/mobileApp/show/{id}/business-units | Unassign Mobile App from Business Units
[**update_asset_mobile_app_status**](MobileApplicationsApi.md#update_asset_mobile_app_status) | **PUT** /api/client/assets/mobileApp/update-status/{id} | Update Status
[**update_custom_property_mobile_app**](MobileApplicationsApi.md#update_custom_property_mobile_app) | **PUT** /api/client/assets/mobileApp/show/{id}/custom-property/{customPropertyId} | Update Custom Property
[**update_note_mobile_app**](MobileApplicationsApi.md#update_note_mobile_app) | **PUT** /api/client/assets/mobileApp/show/{id}/note/{noteId} | Update Note


# **assign_mobile_app_to_business_units**
> ClientMobileAppData assign_mobile_app_to_business_units(id, asset_business_unit_ids_dto)

Assign Mobile App to Business Units

Assign a specific Mobile App asset to a list of Business Units

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.asset_business_unit_ids_dto import AssetBusinessUnitIdsDTO
from watchtowr_api_sdk.models.client_mobile_app_data import ClientMobileAppData
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
    api_instance = watchtowr_api_sdk.MobileApplicationsApi(api_client)
    id = 3.4 # float | The Mobile App asset's ID.
    asset_business_unit_ids_dto = watchtowr_api_sdk.AssetBusinessUnitIdsDTO() # AssetBusinessUnitIdsDTO | 

    try:
        # Assign Mobile App to Business Units
        api_response = api_instance.assign_mobile_app_to_business_units(id, asset_business_unit_ids_dto)
        print("The response of MobileApplicationsApi->assign_mobile_app_to_business_units:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileApplicationsApi->assign_mobile_app_to_business_units: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The Mobile App asset&#39;s ID. | 
 **asset_business_unit_ids_dto** | [**AssetBusinessUnitIdsDTO**](AssetBusinessUnitIdsDTO.md)|  | 

### Return type

[**ClientMobileAppData**](ClientMobileAppData.md)

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

# **create_custom_property_mobile_app**
> ClientCustomProperty create_custom_property_mobile_app(id, create_client_custom_property_dto)

Create Custom Property

Create a Custom Property for a specific Mobile Application asset.

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
    api_instance = watchtowr_api_sdk.MobileApplicationsApi(api_client)
    id = 3.4 # float | The asset ID of the mobile application to create a new custom property for.
    create_client_custom_property_dto = watchtowr_api_sdk.CreateClientCustomPropertyDto() # CreateClientCustomPropertyDto | 

    try:
        # Create Custom Property
        api_response = api_instance.create_custom_property_mobile_app(id, create_client_custom_property_dto)
        print("The response of MobileApplicationsApi->create_custom_property_mobile_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileApplicationsApi->create_custom_property_mobile_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the mobile application to create a new custom property for. | 
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

# **create_note_mobile_app**
> ClientNoteData create_note_mobile_app(id, create_client_note_dto)

Create Note

Create a Note for a specific Mobile Application asset.

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
    api_instance = watchtowr_api_sdk.MobileApplicationsApi(api_client)
    id = 3.4 # float | The asset ID of the mobile application to create a new note for.
    create_client_note_dto = watchtowr_api_sdk.CreateClientNoteDto() # CreateClientNoteDto | 

    try:
        # Create Note
        api_response = api_instance.create_note_mobile_app(id, create_client_note_dto)
        print("The response of MobileApplicationsApi->create_note_mobile_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileApplicationsApi->create_note_mobile_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the mobile application to create a new note for. | 
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

# **delete_custom_property_mobile_app**
> RemoveClientCustomPropertyResponseDto delete_custom_property_mobile_app(id, custom_property_id)

Delete Custom Property

Delete a Custom Property for a specific Mobile Application asset.

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
    api_instance = watchtowr_api_sdk.MobileApplicationsApi(api_client)
    id = 3.4 # float | The asset ID of a mobile application with a custom property to delete.
    custom_property_id = 3.4 # float | The ID of the custom property to delete.

    try:
        # Delete Custom Property
        api_response = api_instance.delete_custom_property_mobile_app(id, custom_property_id)
        print("The response of MobileApplicationsApi->delete_custom_property_mobile_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileApplicationsApi->delete_custom_property_mobile_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of a mobile application with a custom property to delete. | 
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

# **delete_note_mobile_app**
> DeleteNoteSucces delete_note_mobile_app(id, note_id)

Delete Note

Delete a Note for a specific Mobile Application asset.

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
    api_instance = watchtowr_api_sdk.MobileApplicationsApi(api_client)
    id = 3.4 # float | The asset ID of a mobile application with a note to delete.
    note_id = 3.4 # float | The ID of the note to delete.

    try:
        # Delete Note
        api_response = api_instance.delete_note_mobile_app(id, note_id)
        print("The response of MobileApplicationsApi->delete_note_mobile_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileApplicationsApi->delete_note_mobile_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of a mobile application with a note to delete. | 
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

# **get_asset_mobile_app_details**
> ClientMobileAppData get_asset_mobile_app_details(id)

Get Mobile Application

Get the details of a specific Mobile Application.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_mobile_app_data import ClientMobileAppData
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
    api_instance = watchtowr_api_sdk.MobileApplicationsApi(api_client)
    id = 3.4 # float | The asset ID of the mobile application to get.

    try:
        # Get Mobile Application
        api_response = api_instance.get_asset_mobile_app_details(id)
        print("The response of MobileApplicationsApi->get_asset_mobile_app_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileApplicationsApi->get_asset_mobile_app_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the mobile application to get. | 

### Return type

[**ClientMobileAppData**](ClientMobileAppData.md)

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

# **get_asset_mobile_app_notes**
> ClientNoteListData get_asset_mobile_app_notes(id, page=page, page_size=page_size)

List Notes

List the Notes of a specific Mobile Application asset.

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
    api_instance = watchtowr_api_sdk.MobileApplicationsApi(api_client)
    id = 3.4 # float | The asset ID of the mobile application to list notes of.
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)

    try:
        # List Notes
        api_response = api_instance.get_asset_mobile_app_notes(id, page=page, page_size=page_size)
        print("The response of MobileApplicationsApi->get_asset_mobile_app_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileApplicationsApi->get_asset_mobile_app_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the mobile application to list notes of. | 
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

# **get_custom_properties_mobile_app**
> PaginatedClientCustomProperty get_custom_properties_mobile_app(id, page=page, page_size=page_size)

List Custom Properties

List the Custom Properties of a specific Mobile Application asset.

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
    api_instance = watchtowr_api_sdk.MobileApplicationsApi(api_client)
    id = 3.4 # float | The asset ID of the mobile application to list custom properties of.
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)

    try:
        # List Custom Properties
        api_response = api_instance.get_custom_properties_mobile_app(id, page=page, page_size=page_size)
        print("The response of MobileApplicationsApi->get_custom_properties_mobile_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileApplicationsApi->get_custom_properties_mobile_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the mobile application to list custom properties of. | 
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

# **get_list_asset_mobile_apps**
> PaginatedClientMobileApp get_list_asset_mobile_apps(page=page, page_size=page_size, asset_name=asset_name, statuses=statuses, source=source, integration_connections=integration_connections, business_unit_ids=business_unit_ids, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, custom_property_key=custom_property_key, custom_property_value=custom_property_value)

List Mobile Applications

List all discovered Mobile Applications, ordered by date identified.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.paginated_client_mobile_app import PaginatedClientMobileApp
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
    api_instance = watchtowr_api_sdk.MobileApplicationsApi(api_client)
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)
    asset_name = 'watchTowr-Android' # str | Search Mobile Applications by assets by name. (optional)
    statuses = ['statuses_example'] # List[str] | Filter assets by one or more comma separated asset statuses. Valid statuses are:       * verified       * tracked       * incorrect identification       * pending       * verifiedOutOfScope  (optional)
    source = 'module-adversarysight-playstore-mobileapp-discovery' # str | Filter assets by the source that discovered the asset. (optional)
    integration_connections = '123:aws,456:azure,789:googlecloud' # str | Filter assets by integration connections (comma-separated list of integrationId:integrationType pairs).  Valid integration types: aws, googlecloud, azure, cloudflare, alibabacloud, prismacloud, prismacloudapigee, huaweicloud, tencentcloud, wiz, servicenowcmdb, akamaiedge, armiscentrix, qualysvmdr, tenable  Format: integrationId:integrationType (e.g., 123:aws) Multiple connections: separate with commas (e.g., 123:aws,456:azure,789:googlecloud) (optional)
    business_unit_ids = '1,2,3' # str | Filter assets by a list of comma separated business unit IDs that the asset is related to. (optional)
    created_from = '2013-10-20T19:20:30+01:00' # datetime | Filter assets created after a given date and time. (optional)
    created_to = '2013-10-20T19:20:30+01:00' # datetime | Filter assets created before a given date and time. (optional)
    updated_from = '2013-10-20T19:20:30+01:00' # datetime | Filter assets updated after a given date and time. (optional)
    updated_to = '2013-10-20T19:20:30+01:00' # datetime | Filter assets updated before a given date and time. (optional)
    custom_property_key = 'environment' # str | Filter assets by custom property key. (optional)
    custom_property_value = 'production' # str | Filter assets by custom property value. Must be used together with customPropertyKey. (optional)

    try:
        # List Mobile Applications
        api_response = api_instance.get_list_asset_mobile_apps(page=page, page_size=page_size, asset_name=asset_name, statuses=statuses, source=source, integration_connections=integration_connections, business_unit_ids=business_unit_ids, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, custom_property_key=custom_property_key, custom_property_value=custom_property_value)
        print("The response of MobileApplicationsApi->get_list_asset_mobile_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileApplicationsApi->get_list_asset_mobile_apps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | [optional] 
 **asset_name** | **str**| Search Mobile Applications by assets by name. | [optional] 
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

[**PaginatedClientMobileApp**](PaginatedClientMobileApp.md)

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

# **unassign_mobile_app_from_business_units**
> ClientMobileAppData unassign_mobile_app_from_business_units(id, business_unit_ids)

Unassign Mobile App from Business Units

Unassign a specific Mobile App asset from a list of Business Units

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_mobile_app_data import ClientMobileAppData
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
    api_instance = watchtowr_api_sdk.MobileApplicationsApi(api_client)
    id = 3.4 # float | The Mobile App asset's ID.
    business_unit_ids = ['business_unit_ids_example'] # List[str] | List of comma-seperated business unit IDs to unassign from the asset.

    try:
        # Unassign Mobile App from Business Units
        api_response = api_instance.unassign_mobile_app_from_business_units(id, business_unit_ids)
        print("The response of MobileApplicationsApi->unassign_mobile_app_from_business_units:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileApplicationsApi->unassign_mobile_app_from_business_units: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The Mobile App asset&#39;s ID. | 
 **business_unit_ids** | [**List[str]**](str.md)| List of comma-seperated business unit IDs to unassign from the asset. | 

### Return type

[**ClientMobileAppData**](ClientMobileAppData.md)

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

# **update_asset_mobile_app_status**
> ClientMobileAppData update_asset_mobile_app_status(id, update_client_next_gen_asset_status_dto)

Update Status

Update Status of a specific Mobile Application asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_mobile_app_data import ClientMobileAppData
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
    api_instance = watchtowr_api_sdk.MobileApplicationsApi(api_client)
    id = 3.4 # float | The asset ID of the mobile application to update status of.
    update_client_next_gen_asset_status_dto = watchtowr_api_sdk.UpdateClientNextGenAssetStatusDto() # UpdateClientNextGenAssetStatusDto | 

    try:
        # Update Status
        api_response = api_instance.update_asset_mobile_app_status(id, update_client_next_gen_asset_status_dto)
        print("The response of MobileApplicationsApi->update_asset_mobile_app_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileApplicationsApi->update_asset_mobile_app_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the mobile application to update status of. | 
 **update_client_next_gen_asset_status_dto** | [**UpdateClientNextGenAssetStatusDto**](UpdateClientNextGenAssetStatusDto.md)|  | 

### Return type

[**ClientMobileAppData**](ClientMobileAppData.md)

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

# **update_custom_property_mobile_app**
> ClientCustomProperty update_custom_property_mobile_app(id, custom_property_id, update_client_custom_property_dto)

Update Custom Property

Update a Custom Property for a specific Mobile Application asset.

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
    api_instance = watchtowr_api_sdk.MobileApplicationsApi(api_client)
    id = 3.4 # float | The asset ID of a mobile application with a custom property to update.
    custom_property_id = 3.4 # float | The ID of the custom property to update.
    update_client_custom_property_dto = watchtowr_api_sdk.UpdateClientCustomPropertyDto() # UpdateClientCustomPropertyDto | 

    try:
        # Update Custom Property
        api_response = api_instance.update_custom_property_mobile_app(id, custom_property_id, update_client_custom_property_dto)
        print("The response of MobileApplicationsApi->update_custom_property_mobile_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileApplicationsApi->update_custom_property_mobile_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of a mobile application with a custom property to update. | 
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

# **update_note_mobile_app**
> ClientNoteData update_note_mobile_app(id, note_id, create_client_note_dto)

Update Note

Update a Note for a specific Mobile Application asset.

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
    api_instance = watchtowr_api_sdk.MobileApplicationsApi(api_client)
    id = 3.4 # float | The asset ID of a mobile application with a note to update.
    note_id = 3.4 # float | The ID of the note to update.
    create_client_note_dto = watchtowr_api_sdk.CreateClientNoteDto() # CreateClientNoteDto | 

    try:
        # Update Note
        api_response = api_instance.update_note_mobile_app(id, note_id, create_client_note_dto)
        print("The response of MobileApplicationsApi->update_note_mobile_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MobileApplicationsApi->update_note_mobile_app: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of a mobile application with a note to update. | 
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

