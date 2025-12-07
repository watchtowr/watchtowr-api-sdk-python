# watchtowr_api_sdk.FindingsApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_property_finding**](FindingsApi.md#create_custom_property_finding) | **POST** /api/client/findings/show/{id}/custom-property | Create Custom Property
[**create_finding_note**](FindingsApi.md#create_finding_note) | **POST** /api/client/findings/show/{id}/note | Create Finding Note
[**delete_custom_property_finding**](FindingsApi.md#delete_custom_property_finding) | **DELETE** /api/client/findings/show/{id}/custom-property/{customPropertyId} | Delete Custom Property
[**delete_finding_note**](FindingsApi.md#delete_finding_note) | **DELETE** /api/client/findings/show/{id}/note/{noteId} | Delete Finding Note
[**export_pdf_for_finding**](FindingsApi.md#export_pdf_for_finding) | **GET** /api/client/findings/export/{id} | Export Finding PDF
[**get_available_finding_statuses**](FindingsApi.md#get_available_finding_statuses) | **GET** /api/client/findings/statuses | List Finding Statuses
[**get_custom_properties_finding**](FindingsApi.md#get_custom_properties_finding) | **GET** /api/client/findings/show/{id}/custom-properties | List Custom Properties
[**get_finding_details**](FindingsApi.md#get_finding_details) | **GET** /api/client/findings/show/{id} | Get Finding Details
[**get_finding_notes**](FindingsApi.md#get_finding_notes) | **GET** /api/client/findings/show/{id}/notes | List Finding Notes
[**get_list_findings**](FindingsApi.md#get_list_findings) | **GET** /api/client/findings/list | List Findings
[**start_specific_finding_retest**](FindingsApi.md#start_specific_finding_retest) | **POST** /api/client/findings/retest/{finding_id} | Retest Finding
[**update_custom_property_finding**](FindingsApi.md#update_custom_property_finding) | **PUT** /api/client/findings/show/{id}/custom-property/{customPropertyId} | Update Custom Property
[**update_finding_note**](FindingsApi.md#update_finding_note) | **PUT** /api/client/findings/show/{id}/note/{noteId} | Update Finding Note
[**update_finding_state**](FindingsApi.md#update_finding_state) | **POST** /api/client/findings/state/{id} | Update Finding State
[**update_finding_status**](FindingsApi.md#update_finding_status) | **POST** /api/client/findings/status/{id} | Update Finding Status


# **create_custom_property_finding**
> ClientCustomProperty create_custom_property_finding(id, create_client_custom_property_dto)

Create Custom Property

Create a Custom Property for a specific Finding.

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
    api_instance = watchtowr_api_sdk.FindingsApi(api_client)
    id = 3.4 # float | The ID of the finding to create a new custom property for.
    create_client_custom_property_dto = watchtowr_api_sdk.CreateClientCustomPropertyDto() # CreateClientCustomPropertyDto | 

    try:
        # Create Custom Property
        api_response = api_instance.create_custom_property_finding(id, create_client_custom_property_dto)
        print("The response of FindingsApi->create_custom_property_finding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->create_custom_property_finding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The ID of the finding to create a new custom property for. | 
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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_finding_note**
> ClientNoteData create_finding_note(id, create_client_note_dto)

Create Finding Note

Create a new note for a specific finding.

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
    api_instance = watchtowr_api_sdk.FindingsApi(api_client)
    id = 3.4 # float | The ID of the finding to create a note for.
    create_client_note_dto = watchtowr_api_sdk.CreateClientNoteDto() # CreateClientNoteDto | 

    try:
        # Create Finding Note
        api_response = api_instance.create_finding_note(id, create_client_note_dto)
        print("The response of FindingsApi->create_finding_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->create_finding_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The ID of the finding to create a note for. | 
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

# **delete_custom_property_finding**
> RemoveClientCustomPropertyResponseDto delete_custom_property_finding(id, custom_property_id)

Delete Custom Property

Delete a Custom Property for a specific Finding.

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
    api_instance = watchtowr_api_sdk.FindingsApi(api_client)
    id = 3.4 # float | The ID of the finding to delete a custom property of.
    custom_property_id = 3.4 # float | The ID of the custom property to delete.

    try:
        # Delete Custom Property
        api_response = api_instance.delete_custom_property_finding(id, custom_property_id)
        print("The response of FindingsApi->delete_custom_property_finding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->delete_custom_property_finding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The ID of the finding to delete a custom property of. | 
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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_finding_note**
> DeleteNoteSucces delete_finding_note(id, note_id)

Delete Finding Note

Delete a specific note from a finding.

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
    api_instance = watchtowr_api_sdk.FindingsApi(api_client)
    id = 3.4 # float | The ID of the finding that contains the note.
    note_id = 3.4 # float | The ID of the note to delete.

    try:
        # Delete Finding Note
        api_response = api_instance.delete_finding_note(id, note_id)
        print("The response of FindingsApi->delete_finding_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->delete_finding_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The ID of the finding that contains the note. | 
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

# **export_pdf_for_finding**
> export_pdf_for_finding(id)

Export Finding PDF

Export a PDF report for a specific finding.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
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
    api_instance = watchtowr_api_sdk.FindingsApi(api_client)
    id = 3.4 # float | The ID of the finding to export.

    try:
        # Export Finding PDF
        api_instance.export_pdf_for_finding(id)
    except Exception as e:
        print("Exception when calling FindingsApi->export_pdf_for_finding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The ID of the finding to export. | 

### Return type

void (empty response body)

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

# **get_available_finding_statuses**
> get_available_finding_statuses()

List Finding Statuses

List all available statuses for findings.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
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
    api_instance = watchtowr_api_sdk.FindingsApi(api_client)

    try:
        # List Finding Statuses
        api_instance.get_available_finding_statuses()
    except Exception as e:
        print("Exception when calling FindingsApi->get_available_finding_statuses: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_properties_finding**
> PaginatedClientCustomProperty get_custom_properties_finding(id, page=page, page_size=page_size)

List Custom Properties

List the Custom Properties of a specific Finding.

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
    api_instance = watchtowr_api_sdk.FindingsApi(api_client)
    id = 3.4 # float | The ID of the finding to list custom properties of.
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)

    try:
        # List Custom Properties
        api_response = api_instance.get_custom_properties_finding(id, page=page, page_size=page_size)
        print("The response of FindingsApi->get_custom_properties_finding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->get_custom_properties_finding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The ID of the finding to list custom properties of. | 
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

# **get_finding_details**
> ClientFindingData get_finding_details(id)

Get Finding Details

Get the details of a specific finding.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_finding_data import ClientFindingData
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
    api_instance = watchtowr_api_sdk.FindingsApi(api_client)
    id = 3.4 # float | The ID of the finding to retrieve.

    try:
        # Get Finding Details
        api_response = api_instance.get_finding_details(id)
        print("The response of FindingsApi->get_finding_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->get_finding_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The ID of the finding to retrieve. | 

### Return type

[**ClientFindingData**](ClientFindingData.md)

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

# **get_finding_notes**
> ClientNoteListData get_finding_notes(id, page=page, page_size=page_size)

List Finding Notes

List all notes for a specific finding.

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
    api_instance = watchtowr_api_sdk.FindingsApi(api_client)
    id = 3.4 # float | The ID of the finding to list notes for.
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)

    try:
        # List Finding Notes
        api_response = api_instance.get_finding_notes(id, page=page, page_size=page_size)
        print("The response of FindingsApi->get_finding_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->get_finding_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The ID of the finding to list notes for. | 
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

# **get_list_findings**
> PaginatedClientFindings get_list_findings(page=page, page_size=page_size, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, statuses=statuses, business_unit_ids=business_unit_ids, finding_impact_threshold=finding_impact_threshold, finding_title=finding_title, severities=severities, asset_title=asset_title, asset_types=asset_types, assignee=assignee, tags=tags, only_validated_exploitable=only_validated_exploitable, only_unacknowledged=only_unacknowledged, exploitation_risk_level=exploitation_risk_level)

List Findings

List all discovered findings, ordered by date identified.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.paginated_client_findings import PaginatedClientFindings
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
    api_instance = watchtowr_api_sdk.FindingsApi(api_client)
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)
    created_from = '2013-10-20T19:20:30+01:00' # datetime | Filter findings created after a given date and time. (optional)
    created_to = '2013-10-20T19:20:30+01:00' # datetime | Filter findings created before a given date and time. (optional)
    updated_from = '2013-10-20T19:20:30+01:00' # datetime | Filter findings updated after a given date and time. (optional)
    updated_to = '2013-10-20T19:20:30+01:00' # datetime | Filter findings updated before a given date and time. (optional)
    statuses = 'confirmed,unconfirmed,remediated,risk-accepted,closed,asset-no-longer-tracked' # str | Filter findings by a list of comma separated statuses they're tagged with. (optional)
    business_unit_ids = '1,2,3' # str | Filter findings by a list of comma separated business unit IDs that they're related to. (optional)
    finding_impact_threshold = 'finding_impact_threshold_example' # str | Impact Setting: * High - Prioritised Findings (vulnerabilities, misconfigurations and weaknesses) that could have an immediate, direct impact on your organisation's security posture. * All - All Findings, a broader range of findings that may not directly impact your organisation's security posture, but may represent deviations from best practices. (optional)
    finding_title = 'Valid%20Credentials%20Discovered' # str | Search findings by title contents. (optional)
    severities = 'critical,high,medium,low,info' # str | Filter findings by a list of comma separated severities they're tagged with. (optional)
    asset_title = 'www.watchTowr.com' # str | Search by findings by affected asset. (optional)
    asset_types = 'domain,subdomain,ip' # str | Filter findings by a comma separated list of affected asset types. (optional)
    assignee = 'John Smith' # str | Filter findings by assignee. To filter findings that don't have an assignee, please use assignee=No Assignee. (optional)
    tags = 'CISA-KEV,Defacement,Credentials' # str | Filter findings by a comma separated list of tags. (optional)
    only_validated_exploitable = true # bool | Filter to only show findings validated as exploitable. (optional)
    only_unacknowledged = true # bool | Filter to only show unacknowledged findings. (optional)
    exploitation_risk_level = 'Unknown,Moderate,High' # str | Filter findings by a comma separated list of exploitation risk levels. (optional)

    try:
        # List Findings
        api_response = api_instance.get_list_findings(page=page, page_size=page_size, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, statuses=statuses, business_unit_ids=business_unit_ids, finding_impact_threshold=finding_impact_threshold, finding_title=finding_title, severities=severities, asset_title=asset_title, asset_types=asset_types, assignee=assignee, tags=tags, only_validated_exploitable=only_validated_exploitable, only_unacknowledged=only_unacknowledged, exploitation_risk_level=exploitation_risk_level)
        print("The response of FindingsApi->get_list_findings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->get_list_findings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | [optional] 
 **created_from** | **datetime**| Filter findings created after a given date and time. | [optional] 
 **created_to** | **datetime**| Filter findings created before a given date and time. | [optional] 
 **updated_from** | **datetime**| Filter findings updated after a given date and time. | [optional] 
 **updated_to** | **datetime**| Filter findings updated before a given date and time. | [optional] 
 **statuses** | **str**| Filter findings by a list of comma separated statuses they&#39;re tagged with. | [optional] 
 **business_unit_ids** | **str**| Filter findings by a list of comma separated business unit IDs that they&#39;re related to. | [optional] 
 **finding_impact_threshold** | **str**| Impact Setting: * High - Prioritised Findings (vulnerabilities, misconfigurations and weaknesses) that could have an immediate, direct impact on your organisation&#39;s security posture. * All - All Findings, a broader range of findings that may not directly impact your organisation&#39;s security posture, but may represent deviations from best practices. | [optional] 
 **finding_title** | **str**| Search findings by title contents. | [optional] 
 **severities** | **str**| Filter findings by a list of comma separated severities they&#39;re tagged with. | [optional] 
 **asset_title** | **str**| Search by findings by affected asset. | [optional] 
 **asset_types** | **str**| Filter findings by a comma separated list of affected asset types. | [optional] 
 **assignee** | **str**| Filter findings by assignee. To filter findings that don&#39;t have an assignee, please use assignee&#x3D;No Assignee. | [optional] 
 **tags** | **str**| Filter findings by a comma separated list of tags. | [optional] 
 **only_validated_exploitable** | **bool**| Filter to only show findings validated as exploitable. | [optional] 
 **only_unacknowledged** | **bool**| Filter to only show unacknowledged findings. | [optional] 
 **exploitation_risk_level** | **str**| Filter findings by a comma separated list of exploitation risk levels. | [optional] 

### Return type

[**PaginatedClientFindings**](PaginatedClientFindings.md)

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

# **start_specific_finding_retest**
> ClientFinding start_specific_finding_retest(finding_id, include_dns_connected=include_dns_connected)

Retest Finding

Initiate a retest for a specific finding.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_finding import ClientFinding
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
    api_instance = watchtowr_api_sdk.FindingsApi(api_client)
    finding_id = 3.4 # float | The ID of the finding to retest.
    include_dns_connected = true # bool | Include DNS-connected findings with the same vulnerability type in the retest. When enabled, the system will identify all findings with the same KB entry on assets connected via DNS A records (up to 10 findings total) and retest them together. (optional)

    try:
        # Retest Finding
        api_response = api_instance.start_specific_finding_retest(finding_id, include_dns_connected=include_dns_connected)
        print("The response of FindingsApi->start_specific_finding_retest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->start_specific_finding_retest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finding_id** | **float**| The ID of the finding to retest. | 
 **include_dns_connected** | **bool**| Include DNS-connected findings with the same vulnerability type in the retest. When enabled, the system will identify all findings with the same KB entry on assets connected via DNS A records (up to 10 findings total) and retest them together. | [optional] 

### Return type

[**ClientFinding**](ClientFinding.md)

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
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_property_finding**
> ClientCustomProperty update_custom_property_finding(id, custom_property_id, update_client_custom_property_dto)

Update Custom Property

Update a Custom Property for a specific Finding

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
    api_instance = watchtowr_api_sdk.FindingsApi(api_client)
    id = 3.4 # float | The ID of the finding to update a custom property of.
    custom_property_id = 3.4 # float | The ID of the custom property to update.
    update_client_custom_property_dto = watchtowr_api_sdk.UpdateClientCustomPropertyDto() # UpdateClientCustomPropertyDto | 

    try:
        # Update Custom Property
        api_response = api_instance.update_custom_property_finding(id, custom_property_id, update_client_custom_property_dto)
        print("The response of FindingsApi->update_custom_property_finding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->update_custom_property_finding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The ID of the finding to update a custom property of. | 
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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_finding_note**
> ClientNoteData update_finding_note(id, note_id, create_client_note_dto)

Update Finding Note

Update an existing note for a specific finding.

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
    api_instance = watchtowr_api_sdk.FindingsApi(api_client)
    id = 3.4 # float | The ID of the finding that contains the note.
    note_id = 3.4 # float | The ID of the note to update.
    create_client_note_dto = watchtowr_api_sdk.CreateClientNoteDto() # CreateClientNoteDto | 

    try:
        # Update Finding Note
        api_response = api_instance.update_finding_note(id, note_id, create_client_note_dto)
        print("The response of FindingsApi->update_finding_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->update_finding_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The ID of the finding that contains the note. | 
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

# **update_finding_state**
> ClientFindingData update_finding_state(id, update_client_finding_state_request_body)

Update Finding State

Update the state of a specific finding.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_finding_data import ClientFindingData
from watchtowr_api_sdk.models.update_client_finding_state_request_body import UpdateClientFindingStateRequestBody
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
    api_instance = watchtowr_api_sdk.FindingsApi(api_client)
    id = 3.4 # float | The ID of the finding to update.
    update_client_finding_state_request_body = watchtowr_api_sdk.UpdateClientFindingStateRequestBody() # UpdateClientFindingStateRequestBody | 

    try:
        # Update Finding State
        api_response = api_instance.update_finding_state(id, update_client_finding_state_request_body)
        print("The response of FindingsApi->update_finding_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->update_finding_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The ID of the finding to update. | 
 **update_client_finding_state_request_body** | [**UpdateClientFindingStateRequestBody**](UpdateClientFindingStateRequestBody.md)|  | 

### Return type

[**ClientFindingData**](ClientFindingData.md)

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

# **update_finding_status**
> ClientFindingData update_finding_status(id, update_client_finding_status_request_body)

Update Finding Status

Update the status of a specific finding.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_finding_data import ClientFindingData
from watchtowr_api_sdk.models.update_client_finding_status_request_body import UpdateClientFindingStatusRequestBody
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
    api_instance = watchtowr_api_sdk.FindingsApi(api_client)
    id = 3.4 # float | The ID of the finding to update.
    update_client_finding_status_request_body = watchtowr_api_sdk.UpdateClientFindingStatusRequestBody() # UpdateClientFindingStatusRequestBody | 

    try:
        # Update Finding Status
        api_response = api_instance.update_finding_status(id, update_client_finding_status_request_body)
        print("The response of FindingsApi->update_finding_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FindingsApi->update_finding_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The ID of the finding to update. | 
 **update_client_finding_status_request_body** | [**UpdateClientFindingStatusRequestBody**](UpdateClientFindingStatusRequestBody.md)|  | 

### Return type

[**ClientFindingData**](ClientFindingData.md)

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

