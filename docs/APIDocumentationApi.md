# watchtowr_api_sdk.APIDocumentationApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_asset_api_documentation_note**](APIDocumentationApi.md#add_asset_api_documentation_note) | **POST** /api/client/assets/apiDocumentation/show/{id}/note | Create Note
[**assign_api_documentation_to_business_units**](APIDocumentationApi.md#assign_api_documentation_to_business_units) | **POST** /api/client/assets/apiDocumentation/show/{id}/business-units | Assign API Documentation to Business Units
[**create_custom_property_api_documentation**](APIDocumentationApi.md#create_custom_property_api_documentation) | **POST** /api/client/assets/apiDocumentation/show/{id}/custom-property | Create Custom Property
[**delete_asset_api_documentation_note**](APIDocumentationApi.md#delete_asset_api_documentation_note) | **DELETE** /api/client/assets/apiDocumentation/show/{id}/note/{noteId} | Delete Note
[**delete_custom_property_api_documentation**](APIDocumentationApi.md#delete_custom_property_api_documentation) | **DELETE** /api/client/assets/apiDocumentation/show/{id}/custom-property/{customPropertyId} | Delete Custom Property
[**get_asset_api_documentation_details**](APIDocumentationApi.md#get_asset_api_documentation_details) | **GET** /api/client/assets/apiDocumentation/show/{id} | Get API Documentation Details
[**get_asset_api_documentation_notes**](APIDocumentationApi.md#get_asset_api_documentation_notes) | **GET** /api/client/assets/apiDocumentation/show/{id}/notes | List API Documentation Notes
[**get_custom_properties_api_documentation**](APIDocumentationApi.md#get_custom_properties_api_documentation) | **GET** /api/client/assets/apiDocumentation/show/{id}/custom-properties | List Custom Properties
[**get_list_asset_api_documentation**](APIDocumentationApi.md#get_list_asset_api_documentation) | **GET** /api/client/assets/apiDocumentation/list | List API Documentation
[**unassign_api_documentation_from_business_units**](APIDocumentationApi.md#unassign_api_documentation_from_business_units) | **DELETE** /api/client/assets/apiDocumentation/show/{id}/business-units | Unassign API Documentation from Business Units
[**update_asset_api_documentation_note**](APIDocumentationApi.md#update_asset_api_documentation_note) | **PUT** /api/client/assets/apiDocumentation/show/{id}/note/{noteId} | Update Note
[**update_asset_api_documentation_status**](APIDocumentationApi.md#update_asset_api_documentation_status) | **PUT** /api/client/assets/apiDocumentation/update-status/{id} | Update API Documentation Status
[**update_custom_property_api_documentation**](APIDocumentationApi.md#update_custom_property_api_documentation) | **PUT** /api/client/assets/apiDocumentation/show/{id}/custom-property/{customPropertyId} | Update Custom Property


# **add_asset_api_documentation_note**
> ClientNoteData add_asset_api_documentation_note(id, create_client_note_dto)

Create Note

Create a Note for a specific API Documentation asset.

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
    api_instance = watchtowr_api_sdk.APIDocumentationApi(api_client)
    id = 3.4 # float | The asset ID of the API Documentation asset to create a new note for.
    create_client_note_dto = watchtowr_api_sdk.CreateClientNoteDto() # CreateClientNoteDto | 

    try:
        # Create Note
        api_response = api_instance.add_asset_api_documentation_note(id, create_client_note_dto)
        print("The response of APIDocumentationApi->add_asset_api_documentation_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDocumentationApi->add_asset_api_documentation_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the API Documentation asset to create a new note for. | 
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

# **assign_api_documentation_to_business_units**
> ClientApiDocumentation assign_api_documentation_to_business_units(id, asset_business_unit_ids_dto)

Assign API Documentation to Business Units

Assign a specific API Documentation asset to a list of Business Units

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.asset_business_unit_ids_dto import AssetBusinessUnitIdsDTO
from watchtowr_api_sdk.models.client_api_documentation import ClientApiDocumentation
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
    api_instance = watchtowr_api_sdk.APIDocumentationApi(api_client)
    id = 3.4 # float | The API Documentation asset's ID.
    asset_business_unit_ids_dto = watchtowr_api_sdk.AssetBusinessUnitIdsDTO() # AssetBusinessUnitIdsDTO | 

    try:
        # Assign API Documentation to Business Units
        api_response = api_instance.assign_api_documentation_to_business_units(id, asset_business_unit_ids_dto)
        print("The response of APIDocumentationApi->assign_api_documentation_to_business_units:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDocumentationApi->assign_api_documentation_to_business_units: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The API Documentation asset&#39;s ID. | 
 **asset_business_unit_ids_dto** | [**AssetBusinessUnitIdsDTO**](AssetBusinessUnitIdsDTO.md)|  | 

### Return type

[**ClientApiDocumentation**](ClientApiDocumentation.md)

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

# **create_custom_property_api_documentation**
> ClientCustomProperty create_custom_property_api_documentation(id, create_client_custom_property_dto)

Create Custom Property

Create Custom Property for a specific API Documentation asset.

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
    api_instance = watchtowr_api_sdk.APIDocumentationApi(api_client)
    id = 3.4 # float | The asset ID of the API Documentation asset to create a new custom property for.
    create_client_custom_property_dto = watchtowr_api_sdk.CreateClientCustomPropertyDto() # CreateClientCustomPropertyDto | 

    try:
        # Create Custom Property
        api_response = api_instance.create_custom_property_api_documentation(id, create_client_custom_property_dto)
        print("The response of APIDocumentationApi->create_custom_property_api_documentation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDocumentationApi->create_custom_property_api_documentation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the API Documentation asset to create a new custom property for. | 
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

# **delete_asset_api_documentation_note**
> DeleteNoteSucces delete_asset_api_documentation_note(id, note_id)

Delete Note

Delete a Note of a specific API Documentation asset.

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
    api_instance = watchtowr_api_sdk.APIDocumentationApi(api_client)
    id = 3.4 # float | The asset ID of an API Documentation asset with a note to delete.
    note_id = 3.4 # float | The ID of the note to delete.

    try:
        # Delete Note
        api_response = api_instance.delete_asset_api_documentation_note(id, note_id)
        print("The response of APIDocumentationApi->delete_asset_api_documentation_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDocumentationApi->delete_asset_api_documentation_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of an API Documentation asset with a note to delete. | 
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

# **delete_custom_property_api_documentation**
> RemoveClientCustomPropertyResponseDto delete_custom_property_api_documentation(id, custom_property_id)

Delete Custom Property

Delete Custom Property specific API Documentation asset.

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
    api_instance = watchtowr_api_sdk.APIDocumentationApi(api_client)
    id = 3.4 # float | The asset ID of an API Documentation asset with a custom property to delete. 
    custom_property_id = 3.4 # float | The ID of the custom property to delete.

    try:
        # Delete Custom Property
        api_response = api_instance.delete_custom_property_api_documentation(id, custom_property_id)
        print("The response of APIDocumentationApi->delete_custom_property_api_documentation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDocumentationApi->delete_custom_property_api_documentation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of an API Documentation asset with a custom property to delete.  | 
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

# **get_asset_api_documentation_details**
> ClientApiDocumentation get_asset_api_documentation_details(id)

Get API Documentation Details

Get the details of a specific API documentation asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_api_documentation import ClientApiDocumentation
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
    api_instance = watchtowr_api_sdk.APIDocumentationApi(api_client)
    id = 3.4 # float | The asset ID of the API documentation asset to retrieve.

    try:
        # Get API Documentation Details
        api_response = api_instance.get_asset_api_documentation_details(id)
        print("The response of APIDocumentationApi->get_asset_api_documentation_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDocumentationApi->get_asset_api_documentation_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the API documentation asset to retrieve. | 

### Return type

[**ClientApiDocumentation**](ClientApiDocumentation.md)

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

# **get_asset_api_documentation_notes**
> ClientNoteListData get_asset_api_documentation_notes(id, page=page, page_size=page_size)

List API Documentation Notes

List all notes for a specific API documentation asset.

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
    api_instance = watchtowr_api_sdk.APIDocumentationApi(api_client)
    id = 3.4 # float | The asset ID of the API documentation asset to list notes for.
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)

    try:
        # List API Documentation Notes
        api_response = api_instance.get_asset_api_documentation_notes(id, page=page, page_size=page_size)
        print("The response of APIDocumentationApi->get_asset_api_documentation_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDocumentationApi->get_asset_api_documentation_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the API documentation asset to list notes for. | 
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

# **get_custom_properties_api_documentation**
> PaginatedClientCustomProperty get_custom_properties_api_documentation(id, page=page, page_size=page_size)

List Custom Properties

List the Custom Properties of a specific API Documentation asset.

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
    api_instance = watchtowr_api_sdk.APIDocumentationApi(api_client)
    id = 3.4 # float | The asset ID of the API Documentation asset to list custom properties of.
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)

    try:
        # List Custom Properties
        api_response = api_instance.get_custom_properties_api_documentation(id, page=page, page_size=page_size)
        print("The response of APIDocumentationApi->get_custom_properties_api_documentation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDocumentationApi->get_custom_properties_api_documentation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the API Documentation asset to list custom properties of. | 
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

# **get_list_asset_api_documentation**
> PaginatedApiDocumentation get_list_asset_api_documentation(page=page, page_size=page_size, asset_name=asset_name, statuses=statuses, source=source, integration_connections=integration_connections, business_unit_ids=business_unit_ids, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, custom_property_key=custom_property_key, custom_property_value=custom_property_value)

List API Documentation

List all discovered API documentation assets, ordered by date identified.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.paginated_api_documentation import PaginatedApiDocumentation
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
    api_instance = watchtowr_api_sdk.APIDocumentationApi(api_client)
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)
    asset_name = 'watchtowr_docs/watchtowr-swagger-hub' # str | Search API documentation by asset name. (optional)
    statuses = ['statuses_example'] # List[str] | Filter assets by one or more comma separated asset statuses. Valid statuses are:       * verified       * tracked       * incorrect identification       * pending       * verifiedOutOfScope  (optional)
    source = 'module-adversarysight-api-discovery' # str | Filter assets by the source that discovered the asset. (optional)
    integration_connections = '123:aws,456:azure,789:googlecloud' # str | Filter assets by integration connections (comma-separated list of integrationId:integrationType pairs).  Valid integration types: aws, googlecloud, azure, cloudflare, alibabacloud, prismacloud, prismacloudapigee, huaweicloud, tencentcloud, wiz, servicenowcmdb, akamaiedge, armiscentrix, qualysvmdr  Format: integrationId:integrationType (e.g., 123:aws) Multiple connections: separate with commas (e.g., 123:aws,456:azure,789:googlecloud) (optional)
    business_unit_ids = '1,2,3' # str | Filter assets by a list of comma separated business unit IDs that the asset is related to. (optional)
    created_from = '2013-10-20T19:20:30+01:00' # datetime | Filter assets created after a given date and time. (optional)
    created_to = '2013-10-20T19:20:30+01:00' # datetime | Filter assets created before a given date and time. (optional)
    updated_from = '2013-10-20T19:20:30+01:00' # datetime | Filter assets updated after a given date and time. (optional)
    updated_to = '2013-10-20T19:20:30+01:00' # datetime | Filter assets updated before a given date and time. (optional)
    custom_property_key = 'environment' # str | Filter assets by custom property key. (optional)
    custom_property_value = 'production' # str | Filter assets by custom property value. Must be used together with customPropertyKey. (optional)

    try:
        # List API Documentation
        api_response = api_instance.get_list_asset_api_documentation(page=page, page_size=page_size, asset_name=asset_name, statuses=statuses, source=source, integration_connections=integration_connections, business_unit_ids=business_unit_ids, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, custom_property_key=custom_property_key, custom_property_value=custom_property_value)
        print("The response of APIDocumentationApi->get_list_asset_api_documentation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDocumentationApi->get_list_asset_api_documentation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | [optional] 
 **asset_name** | **str**| Search API documentation by asset name. | [optional] 
 **statuses** | [**List[str]**](str.md)| Filter assets by one or more comma separated asset statuses. Valid statuses are:       * verified       * tracked       * incorrect identification       * pending       * verifiedOutOfScope  | [optional] 
 **source** | **str**| Filter assets by the source that discovered the asset. | [optional] 
 **integration_connections** | **str**| Filter assets by integration connections (comma-separated list of integrationId:integrationType pairs).  Valid integration types: aws, googlecloud, azure, cloudflare, alibabacloud, prismacloud, prismacloudapigee, huaweicloud, tencentcloud, wiz, servicenowcmdb, akamaiedge, armiscentrix, qualysvmdr  Format: integrationId:integrationType (e.g., 123:aws) Multiple connections: separate with commas (e.g., 123:aws,456:azure,789:googlecloud) | [optional] 
 **business_unit_ids** | **str**| Filter assets by a list of comma separated business unit IDs that the asset is related to. | [optional] 
 **created_from** | **datetime**| Filter assets created after a given date and time. | [optional] 
 **created_to** | **datetime**| Filter assets created before a given date and time. | [optional] 
 **updated_from** | **datetime**| Filter assets updated after a given date and time. | [optional] 
 **updated_to** | **datetime**| Filter assets updated before a given date and time. | [optional] 
 **custom_property_key** | **str**| Filter assets by custom property key. | [optional] 
 **custom_property_value** | **str**| Filter assets by custom property value. Must be used together with customPropertyKey. | [optional] 

### Return type

[**PaginatedApiDocumentation**](PaginatedApiDocumentation.md)

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

# **unassign_api_documentation_from_business_units**
> ClientApiDocumentation unassign_api_documentation_from_business_units(id, business_unit_ids)

Unassign API Documentation from Business Units

Unassign a specific API Documentation asset from a list of Business Units

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_api_documentation import ClientApiDocumentation
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
    api_instance = watchtowr_api_sdk.APIDocumentationApi(api_client)
    id = 3.4 # float | The API Documentation asset's ID.
    business_unit_ids = ['business_unit_ids_example'] # List[str] | List of comma-seperated business unit IDs to unassign from the asset.

    try:
        # Unassign API Documentation from Business Units
        api_response = api_instance.unassign_api_documentation_from_business_units(id, business_unit_ids)
        print("The response of APIDocumentationApi->unassign_api_documentation_from_business_units:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDocumentationApi->unassign_api_documentation_from_business_units: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The API Documentation asset&#39;s ID. | 
 **business_unit_ids** | [**List[str]**](str.md)| List of comma-seperated business unit IDs to unassign from the asset. | 

### Return type

[**ClientApiDocumentation**](ClientApiDocumentation.md)

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

# **update_asset_api_documentation_note**
> ClientNoteData update_asset_api_documentation_note(id, note_id, create_client_note_dto)

Update Note

Update a Note of a specific API Documentation asset.

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
    api_instance = watchtowr_api_sdk.APIDocumentationApi(api_client)
    id = 3.4 # float | The asset ID of an API Documentation asset with a note to update.
    note_id = 3.4 # float | The ID of the note to update.
    create_client_note_dto = watchtowr_api_sdk.CreateClientNoteDto() # CreateClientNoteDto | 

    try:
        # Update Note
        api_response = api_instance.update_asset_api_documentation_note(id, note_id, create_client_note_dto)
        print("The response of APIDocumentationApi->update_asset_api_documentation_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDocumentationApi->update_asset_api_documentation_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of an API Documentation asset with a note to update. | 
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

# **update_asset_api_documentation_status**
> ClientApiDocumentation update_asset_api_documentation_status(id, update_api_documentation_status_dto)

Update API Documentation Status

Update the status of a specific API documentation asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_api_documentation import ClientApiDocumentation
from watchtowr_api_sdk.models.update_api_documentation_status_dto import UpdateApiDocumentationStatusDto
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
    api_instance = watchtowr_api_sdk.APIDocumentationApi(api_client)
    id = 3.4 # float | The asset ID of the API documentation asset to update.
    update_api_documentation_status_dto = watchtowr_api_sdk.UpdateApiDocumentationStatusDto() # UpdateApiDocumentationStatusDto | 

    try:
        # Update API Documentation Status
        api_response = api_instance.update_asset_api_documentation_status(id, update_api_documentation_status_dto)
        print("The response of APIDocumentationApi->update_asset_api_documentation_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDocumentationApi->update_asset_api_documentation_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the API documentation asset to update. | 
 **update_api_documentation_status_dto** | [**UpdateApiDocumentationStatusDto**](UpdateApiDocumentationStatusDto.md)|  | 

### Return type

[**ClientApiDocumentation**](ClientApiDocumentation.md)

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

# **update_custom_property_api_documentation**
> ClientCustomProperty update_custom_property_api_documentation(id, custom_property_id, update_client_custom_property_dto)

Update Custom Property

Update a Custom Property for a specific API Documentation asset.

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
    api_instance = watchtowr_api_sdk.APIDocumentationApi(api_client)
    id = 3.4 # float | The asset ID of an API Documentation asset with a custom property to update.
    custom_property_id = 3.4 # float | The ID of the custom property to update.
    update_client_custom_property_dto = watchtowr_api_sdk.UpdateClientCustomPropertyDto() # UpdateClientCustomPropertyDto | 

    try:
        # Update Custom Property
        api_response = api_instance.update_custom_property_api_documentation(id, custom_property_id, update_client_custom_property_dto)
        print("The response of APIDocumentationApi->update_custom_property_api_documentation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIDocumentationApi->update_custom_property_api_documentation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of an API Documentation asset with a custom property to update. | 
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

