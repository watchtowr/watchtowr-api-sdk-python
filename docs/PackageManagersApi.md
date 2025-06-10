# openapi_client.PackageManagersApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_asset_package_manager_note**](PackageManagersApi.md#add_asset_package_manager_note) | **POST** /api/client/assets/packageManager/show/{id}/note | Create Note
[**assign_package_manager_to_business_units**](PackageManagersApi.md#assign_package_manager_to_business_units) | **POST** /api/client/assets/packageManager/show/{id}/business-units | Assign Package Manager to Business Units
[**create_custom_property_package_manager**](PackageManagersApi.md#create_custom_property_package_manager) | **POST** /api/client/assets/packageManager/show/{id}/custom-property | Create Custom Property
[**delete_asset_package_manager_note**](PackageManagersApi.md#delete_asset_package_manager_note) | **DELETE** /api/client/assets/packageManager/show/{id}/note/{noteId} | Delete Note
[**delete_custom_property_by_id**](PackageManagersApi.md#delete_custom_property_by_id) | **DELETE** /api/client/assets/packageManager/show/{id}/custom-property/{customPropertyId} | Delete Custom Property
[**get_asset_package_manager_details**](PackageManagersApi.md#get_asset_package_manager_details) | **GET** /api/client/assets/packageManager/show/{id} | Get Package Manager
[**get_asset_package_manager_notes**](PackageManagersApi.md#get_asset_package_manager_notes) | **GET** /api/client/assets/packageManager/show/{id}/notes | List Notes
[**get_custom_properties_package_manager**](PackageManagersApi.md#get_custom_properties_package_manager) | **GET** /api/client/assets/packageManager/show/{id}/custom-properties | List Custom Properties
[**get_list_asset_package_managers**](PackageManagersApi.md#get_list_asset_package_managers) | **GET** /api/client/assets/packageManager/list | List Package Managers
[**unassign_package_manager_from_business_units**](PackageManagersApi.md#unassign_package_manager_from_business_units) | **DELETE** /api/client/assets/packageManager/show/{id}/business-units | Unassign Package Manager from Business Units
[**update_asset_package_manager_note**](PackageManagersApi.md#update_asset_package_manager_note) | **PUT** /api/client/assets/packageManager/show/{id}/note/{noteId} | Update Note
[**update_asset_package_manager_status**](PackageManagersApi.md#update_asset_package_manager_status) | **PUT** /api/client/assets/packageManager/update-status/{id} | Update Status
[**update_custom_property_package_manager**](PackageManagersApi.md#update_custom_property_package_manager) | **PUT** /api/client/assets/packageManager/show/{id}/custom-property/{customPropertyId} | Update Custom Property


# **add_asset_package_manager_note**
> ClientNoteData add_asset_package_manager_note(id, create_client_note_dto)

Create Note

Create a Note for a specific Package Manager asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.client_note_data import ClientNoteData
from openapi_client.models.create_client_note_dto import CreateClientNoteDto
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
    api_instance = openapi_client.PackageManagersApi(api_client)
    id = 3.4 # float | The asset ID of the Package Manager asset to create a new note for.
    create_client_note_dto = openapi_client.CreateClientNoteDto() # CreateClientNoteDto | 

    try:
        # Create Note
        api_response = api_instance.add_asset_package_manager_note(id, create_client_note_dto)
        print("The response of PackageManagersApi->add_asset_package_manager_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageManagersApi->add_asset_package_manager_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the Package Manager asset to create a new note for. | 
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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_package_manager_to_business_units**
> ClientPackageManagerData assign_package_manager_to_business_units(id, asset_business_unit_ids_dto)

Assign Package Manager to Business Units

Assign a specific Package Manager asset to a list of Business Units

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.asset_business_unit_ids_dto import AssetBusinessUnitIdsDTO
from openapi_client.models.client_package_manager_data import ClientPackageManagerData
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
    api_instance = openapi_client.PackageManagersApi(api_client)
    id = 3.4 # float | The Package Manager asset's ID.
    asset_business_unit_ids_dto = openapi_client.AssetBusinessUnitIdsDTO() # AssetBusinessUnitIdsDTO | 

    try:
        # Assign Package Manager to Business Units
        api_response = api_instance.assign_package_manager_to_business_units(id, asset_business_unit_ids_dto)
        print("The response of PackageManagersApi->assign_package_manager_to_business_units:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageManagersApi->assign_package_manager_to_business_units: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The Package Manager asset&#39;s ID. | 
 **asset_business_unit_ids_dto** | [**AssetBusinessUnitIdsDTO**](AssetBusinessUnitIdsDTO.md)|  | 

### Return type

[**ClientPackageManagerData**](ClientPackageManagerData.md)

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

# **create_custom_property_package_manager**
> ClientCustomProperty create_custom_property_package_manager(id, create_client_custom_property_dto)

Create Custom Property

Create a Custom Property for a specific Package Manager asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.client_custom_property import ClientCustomProperty
from openapi_client.models.create_client_custom_property_dto import CreateClientCustomPropertyDto
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
    api_instance = openapi_client.PackageManagersApi(api_client)
    id = 3.4 # float | The asset ID of the Package Manager asset to create a new custom property for.
    create_client_custom_property_dto = openapi_client.CreateClientCustomPropertyDto() # CreateClientCustomPropertyDto | 

    try:
        # Create Custom Property
        api_response = api_instance.create_custom_property_package_manager(id, create_client_custom_property_dto)
        print("The response of PackageManagersApi->create_custom_property_package_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageManagersApi->create_custom_property_package_manager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the Package Manager asset to create a new custom property for. | 
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

# **delete_asset_package_manager_note**
> DeleteNoteSucces delete_asset_package_manager_note(id, note_id)

Delete Note

Delete a Note of a specific Package Manager asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.delete_note_succes import DeleteNoteSucces
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
    api_instance = openapi_client.PackageManagersApi(api_client)
    id = 3.4 # float | The asset ID of a Package Manager asset with a note to delete.
    note_id = 3.4 # float | The ID of the note to delete.

    try:
        # Delete Note
        api_response = api_instance.delete_asset_package_manager_note(id, note_id)
        print("The response of PackageManagersApi->delete_asset_package_manager_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageManagersApi->delete_asset_package_manager_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of a Package Manager asset with a note to delete. | 
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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_property_by_id**
> RemoveClientCustomPropertyResponseDto delete_custom_property_by_id(id, custom_property_id)

Delete Custom Property

Delete a Custom Property for a specific Package Manager asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.remove_client_custom_property_response_dto import RemoveClientCustomPropertyResponseDto
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
    api_instance = openapi_client.PackageManagersApi(api_client)
    id = 3.4 # float | The asset ID of a Package Manager asset with a custom property to delete.
    custom_property_id = 3.4 # float | The ID of the custom property to delete.

    try:
        # Delete Custom Property
        api_response = api_instance.delete_custom_property_by_id(id, custom_property_id)
        print("The response of PackageManagersApi->delete_custom_property_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageManagersApi->delete_custom_property_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of a Package Manager asset with a custom property to delete. | 
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

# **get_asset_package_manager_details**
> ClientPackageManagerData get_asset_package_manager_details(id)

Get Package Manager

Get the details of a specific Package Manager.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.client_package_manager_data import ClientPackageManagerData
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
    api_instance = openapi_client.PackageManagersApi(api_client)
    id = 3.4 # float | The asset ID of the Package Manager asset to get.

    try:
        # Get Package Manager
        api_response = api_instance.get_asset_package_manager_details(id)
        print("The response of PackageManagersApi->get_asset_package_manager_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageManagersApi->get_asset_package_manager_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the Package Manager asset to get. | 

### Return type

[**ClientPackageManagerData**](ClientPackageManagerData.md)

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

# **get_asset_package_manager_notes**
> ClientNoteListData get_asset_package_manager_notes(id, page=page, page_size=page_size)

List Notes

List the Notes of a specific Package Manager asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.client_note_list_data import ClientNoteListData
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
    api_instance = openapi_client.PackageManagersApi(api_client)
    id = 3.4 # float | The asset ID of the Package Manager asset to list notes for.
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)

    try:
        # List Notes
        api_response = api_instance.get_asset_package_manager_notes(id, page=page, page_size=page_size)
        print("The response of PackageManagersApi->get_asset_package_manager_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageManagersApi->get_asset_package_manager_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the Package Manager asset to list notes for. | 
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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_properties_package_manager**
> PaginatedClientCustomProperty get_custom_properties_package_manager(id, page=page, page_size=page_size)

List Custom Properties

List the Custom Properties of a specific Package Manager asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.paginated_client_custom_property import PaginatedClientCustomProperty
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
    api_instance = openapi_client.PackageManagersApi(api_client)
    id = 3.4 # float | The asset ID of the Package Manager asset to list custom properties of.
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)

    try:
        # List Custom Properties
        api_response = api_instance.get_custom_properties_package_manager(id, page=page, page_size=page_size)
        print("The response of PackageManagersApi->get_custom_properties_package_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageManagersApi->get_custom_properties_package_manager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the Package Manager asset to list custom properties of. | 
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

# **get_list_asset_package_managers**
> PaginatedClientPackageManager get_list_asset_package_managers(page=page, page_size=page_size, asset_name=asset_name, statuses=statuses, source=source, business_unit_ids=business_unit_ids, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to)

List Package Managers

List all discovered Package Managers, ordered by date identified.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.paginated_client_package_manager import PaginatedClientPackageManager
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
    api_instance = openapi_client.PackageManagersApi(api_client)
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)
    asset_name = 'watchTowr/devel_repo' # str | Search package managers by asset name. (optional)
    statuses = ['verified,Tracked'] # List[str] | Filter assets by one or more comma separated asset statuses. Valid statuses are:       * verified       * tracked       * incorrect identification       * pending       * verifiedOutOfScope  (optional)
    source = 'module-adversarysight-yarn-project-discovery' # str | Filter assets by the source that discovered the asset. (optional)
    business_unit_ids = '1,2,3' # str | Filter assets by a list of comma separated business unit IDs that the asset is related to. (optional)
    created_from = '2022-02-22 22:00:00' # datetime | Filter assets created after a given date and time. (optional)
    created_to = '2022-02-23 22:00:00' # datetime | Filter assets created before a given date and time. (optional)
    updated_from = '2022-02-22 22:00:00' # datetime | Filter assets updated after a given date and time. (optional)
    updated_to = '2022-02-23 22:00:00' # datetime | Filter assets updated before a given date and time. (optional)

    try:
        # List Package Managers
        api_response = api_instance.get_list_asset_package_managers(page=page, page_size=page_size, asset_name=asset_name, statuses=statuses, source=source, business_unit_ids=business_unit_ids, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to)
        print("The response of PackageManagersApi->get_list_asset_package_managers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageManagersApi->get_list_asset_package_managers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | [optional] 
 **asset_name** | **str**| Search package managers by asset name. | [optional] 
 **statuses** | [**List[str]**](str.md)| Filter assets by one or more comma separated asset statuses. Valid statuses are:       * verified       * tracked       * incorrect identification       * pending       * verifiedOutOfScope  | [optional] 
 **source** | **str**| Filter assets by the source that discovered the asset. | [optional] 
 **business_unit_ids** | **str**| Filter assets by a list of comma separated business unit IDs that the asset is related to. | [optional] 
 **created_from** | **datetime**| Filter assets created after a given date and time. | [optional] 
 **created_to** | **datetime**| Filter assets created before a given date and time. | [optional] 
 **updated_from** | **datetime**| Filter assets updated after a given date and time. | [optional] 
 **updated_to** | **datetime**| Filter assets updated before a given date and time. | [optional] 

### Return type

[**PaginatedClientPackageManager**](PaginatedClientPackageManager.md)

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

# **unassign_package_manager_from_business_units**
> ClientPackageManagerData unassign_package_manager_from_business_units(id, business_unit_ids)

Unassign Package Manager from Business Units

Unassign a specific Package Manager asset from a list of Business Units

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.client_package_manager_data import ClientPackageManagerData
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
    api_instance = openapi_client.PackageManagersApi(api_client)
    id = 3.4 # float | The Package Manager asset's ID.
    business_unit_ids = ['1,2,3'] # List[str] | List of comma-seperated business unit IDs to unassign from the asset.

    try:
        # Unassign Package Manager from Business Units
        api_response = api_instance.unassign_package_manager_from_business_units(id, business_unit_ids)
        print("The response of PackageManagersApi->unassign_package_manager_from_business_units:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageManagersApi->unassign_package_manager_from_business_units: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The Package Manager asset&#39;s ID. | 
 **business_unit_ids** | [**List[str]**](str.md)| List of comma-seperated business unit IDs to unassign from the asset. | 

### Return type

[**ClientPackageManagerData**](ClientPackageManagerData.md)

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

# **update_asset_package_manager_note**
> ClientNoteData update_asset_package_manager_note(id, note_id, create_client_note_dto)

Update Note

Update a Note of a specific Package Manager asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.client_note_data import ClientNoteData
from openapi_client.models.create_client_note_dto import CreateClientNoteDto
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
    api_instance = openapi_client.PackageManagersApi(api_client)
    id = 3.4 # float | The asset ID of a Package Manager asset with a note to update.
    note_id = 3.4 # float | The ID of the note to update.
    create_client_note_dto = openapi_client.CreateClientNoteDto() # CreateClientNoteDto | 

    try:
        # Update Note
        api_response = api_instance.update_asset_package_manager_note(id, note_id, create_client_note_dto)
        print("The response of PackageManagersApi->update_asset_package_manager_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageManagersApi->update_asset_package_manager_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of a Package Manager asset with a note to update. | 
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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_package_manager_status**
> ClientPackageManagerData update_asset_package_manager_status(id, update_client_next_gen_asset_status_dto)

Update Status

Update Status of a specific Package Manager asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.client_package_manager_data import ClientPackageManagerData
from openapi_client.models.update_client_next_gen_asset_status_dto import UpdateClientNextGenAssetStatusDto
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
    api_instance = openapi_client.PackageManagersApi(api_client)
    id = 3.4 # float | The asset ID of the Package Manager asset to update the status of.
    update_client_next_gen_asset_status_dto = openapi_client.UpdateClientNextGenAssetStatusDto() # UpdateClientNextGenAssetStatusDto | 

    try:
        # Update Status
        api_response = api_instance.update_asset_package_manager_status(id, update_client_next_gen_asset_status_dto)
        print("The response of PackageManagersApi->update_asset_package_manager_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageManagersApi->update_asset_package_manager_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the Package Manager asset to update the status of. | 
 **update_client_next_gen_asset_status_dto** | [**UpdateClientNextGenAssetStatusDto**](UpdateClientNextGenAssetStatusDto.md)|  | 

### Return type

[**ClientPackageManagerData**](ClientPackageManagerData.md)

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

# **update_custom_property_package_manager**
> ClientCustomProperty update_custom_property_package_manager(id, custom_property_id, update_client_custom_property_dto)

Update Custom Property

Update a Custom Property for a specific Package Manager asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.client_custom_property import ClientCustomProperty
from openapi_client.models.update_client_custom_property_dto import UpdateClientCustomPropertyDto
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
    api_instance = openapi_client.PackageManagersApi(api_client)
    id = 3.4 # float | The asset ID of a Package Manager asset with a custom property to update.
    custom_property_id = 3.4 # float | The ID of the custom property to update.
    update_client_custom_property_dto = openapi_client.UpdateClientCustomPropertyDto() # UpdateClientCustomPropertyDto | 

    try:
        # Update Custom Property
        api_response = api_instance.update_custom_property_package_manager(id, custom_property_id, update_client_custom_property_dto)
        print("The response of PackageManagersApi->update_custom_property_package_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PackageManagersApi->update_custom_property_package_manager: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of a Package Manager asset with a custom property to update. | 
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

