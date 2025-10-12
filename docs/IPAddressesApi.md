# watchtowr_api_sdk.IPAddressesApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_ip_to_business_units**](IPAddressesApi.md#assign_ip_to_business_units) | **POST** /api/client/assets/ip/show/{id}/business-units | Assign IP to Business Units
[**create_asset_ip_note**](IPAddressesApi.md#create_asset_ip_note) | **POST** /api/client/assets/ip/show/{id}/note | Create Note
[**create_custom_property_ip**](IPAddressesApi.md#create_custom_property_ip) | **POST** /api/client/assets/ip/show/{id}/custom-property | Create Custom Property
[**delete_asset_ip_note**](IPAddressesApi.md#delete_asset_ip_note) | **DELETE** /api/client/assets/ip/show/{id}/note/{noteId} | Delete Note
[**delete_custom_property_ip**](IPAddressesApi.md#delete_custom_property_ip) | **DELETE** /api/client/assets/ip/show/{id}/custom-property/{customPropertyId} | Delete Custom Property
[**get_asset_ip_details**](IPAddressesApi.md#get_asset_ip_details) | **GET** /api/client/assets/ip/show/{id} | Get IP Address Details
[**get_asset_ip_dns_records**](IPAddressesApi.md#get_asset_ip_dns_records) | **GET** /api/client/assets/ip/show/{id}/dns-records | List DNS Records
[**get_asset_ip_notes**](IPAddressesApi.md#get_asset_ip_notes) | **GET** /api/client/assets/ip/show/{id}/notes | List Notes
[**get_asset_ip_port_details**](IPAddressesApi.md#get_asset_ip_port_details) | **GET** /api/client/assets/ip/show/{ipId}/port/show/{portId} | Get Port
[**get_asset_ip_ports**](IPAddressesApi.md#get_asset_ip_ports) | **GET** /api/client/assets/ip/show/{id}/port/list | List Ports
[**get_custom_properties_ip**](IPAddressesApi.md#get_custom_properties_ip) | **GET** /api/client/assets/ip/show/{id}/custom-properties | List Custom Properties
[**get_list_asset_ips**](IPAddressesApi.md#get_list_asset_ips) | **GET** /api/client/assets/ip/list | List IP Addresses
[**unassign_ip_from_business_units**](IPAddressesApi.md#unassign_ip_from_business_units) | **DELETE** /api/client/assets/ip/show/{id}/business-units | Unassign IP from Business Units
[**update_asset_ip_note**](IPAddressesApi.md#update_asset_ip_note) | **PUT** /api/client/assets/ip/show/{id}/note/{noteId} | Update Note
[**update_asset_ip_status**](IPAddressesApi.md#update_asset_ip_status) | **PUT** /api/client/assets/ip/update-status/{id} | Update Status
[**update_custom_property_ip**](IPAddressesApi.md#update_custom_property_ip) | **PUT** /api/client/assets/ip/show/{id}/custom-property/{customPropertyId} | Update Custom Property


# **assign_ip_to_business_units**
> ClientIpData assign_ip_to_business_units(id, asset_business_unit_ids_dto)

Assign IP to Business Units

Assign a specific IP asset to a list of Business Units

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.asset_business_unit_ids_dto import AssetBusinessUnitIdsDTO
from watchtowr_api_sdk.models.client_ip_data import ClientIpData
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
    api_instance = watchtowr_api_sdk.IPAddressesApi(api_client)
    id = 3.4 # float | The IP asset's ID.
    asset_business_unit_ids_dto = watchtowr_api_sdk.AssetBusinessUnitIdsDTO() # AssetBusinessUnitIdsDTO | 

    try:
        # Assign IP to Business Units
        api_response = api_instance.assign_ip_to_business_units(id, asset_business_unit_ids_dto)
        print("The response of IPAddressesApi->assign_ip_to_business_units:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPAddressesApi->assign_ip_to_business_units: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The IP asset&#39;s ID. | 
 **asset_business_unit_ids_dto** | [**AssetBusinessUnitIdsDTO**](AssetBusinessUnitIdsDTO.md)|  | 

### Return type

[**ClientIpData**](ClientIpData.md)

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

# **create_asset_ip_note**
> ClientNoteData create_asset_ip_note(id, create_client_note_dto)

Create Note

Create a Note for a specific IP Address asset.

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
    api_instance = watchtowr_api_sdk.IPAddressesApi(api_client)
    id = 3.4 # float | The asset ID of an IP address to create a new note for.
    create_client_note_dto = watchtowr_api_sdk.CreateClientNoteDto() # CreateClientNoteDto | 

    try:
        # Create Note
        api_response = api_instance.create_asset_ip_note(id, create_client_note_dto)
        print("The response of IPAddressesApi->create_asset_ip_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPAddressesApi->create_asset_ip_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of an IP address to create a new note for. | 
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

# **create_custom_property_ip**
> ClientCustomProperty create_custom_property_ip(id, create_client_custom_property_dto)

Create Custom Property

Create a Custom Property for a specific IP Address asset.

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
    api_instance = watchtowr_api_sdk.IPAddressesApi(api_client)
    id = 3.4 # float | The asset ID of the IP address to create a new custom property for.
    create_client_custom_property_dto = watchtowr_api_sdk.CreateClientCustomPropertyDto() # CreateClientCustomPropertyDto | 

    try:
        # Create Custom Property
        api_response = api_instance.create_custom_property_ip(id, create_client_custom_property_dto)
        print("The response of IPAddressesApi->create_custom_property_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPAddressesApi->create_custom_property_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the IP address to create a new custom property for. | 
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

# **delete_asset_ip_note**
> DeleteNoteSucces delete_asset_ip_note(id, note_id)

Delete Note

Delete a Note for a specific IP Address asset.

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
    api_instance = watchtowr_api_sdk.IPAddressesApi(api_client)
    id = 3.4 # float | The asset ID of an IP address with a note to delete.
    note_id = 3.4 # float | The ID of the note to delete.

    try:
        # Delete Note
        api_response = api_instance.delete_asset_ip_note(id, note_id)
        print("The response of IPAddressesApi->delete_asset_ip_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPAddressesApi->delete_asset_ip_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of an IP address with a note to delete. | 
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

# **delete_custom_property_ip**
> RemoveClientCustomPropertyResponseDto delete_custom_property_ip(id, custom_property_id)

Delete Custom Property

Delete a Custom Property for a specific IP Address asset

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
    api_instance = watchtowr_api_sdk.IPAddressesApi(api_client)
    id = 3.4 # float | The asset ID of an IP address with a custom property to delete.
    custom_property_id = 3.4 # float | The ID of the custom property to delete.

    try:
        # Delete Custom Property
        api_response = api_instance.delete_custom_property_ip(id, custom_property_id)
        print("The response of IPAddressesApi->delete_custom_property_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPAddressesApi->delete_custom_property_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of an IP address with a custom property to delete. | 
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

# **get_asset_ip_details**
> ClientIpData get_asset_ip_details(id)

Get IP Address Details

Get the details of a specific IP address asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_ip_data import ClientIpData
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
    api_instance = watchtowr_api_sdk.IPAddressesApi(api_client)
    id = 3.4 # float | The asset ID of the IP address to retrieve.

    try:
        # Get IP Address Details
        api_response = api_instance.get_asset_ip_details(id)
        print("The response of IPAddressesApi->get_asset_ip_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPAddressesApi->get_asset_ip_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the IP address to retrieve. | 

### Return type

[**ClientIpData**](ClientIpData.md)

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

# **get_asset_ip_dns_records**
> ClientIpDnsRecordResponse get_asset_ip_dns_records(id, page=page, page_size=page_size)

List DNS Records

List DNS Records of a specific IP Address asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_ip_dns_record_response import ClientIpDnsRecordResponse
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
    api_instance = watchtowr_api_sdk.IPAddressesApi(api_client)
    id = 3.4 # float | The asset ID of the IP address to list DNS records of.
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)

    try:
        # List DNS Records
        api_response = api_instance.get_asset_ip_dns_records(id, page=page, page_size=page_size)
        print("The response of IPAddressesApi->get_asset_ip_dns_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPAddressesApi->get_asset_ip_dns_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the IP address to list DNS records of. | 
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | [optional] 

### Return type

[**ClientIpDnsRecordResponse**](ClientIpDnsRecordResponse.md)

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

# **get_asset_ip_notes**
> ClientNoteListData get_asset_ip_notes(id, page=page, page_size=page_size)

List Notes

List Notes of a specific IP Address asset.

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
    api_instance = watchtowr_api_sdk.IPAddressesApi(api_client)
    id = 3.4 # float | The asset ID of the IP address to list notes of.
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)

    try:
        # List Notes
        api_response = api_instance.get_asset_ip_notes(id, page=page, page_size=page_size)
        print("The response of IPAddressesApi->get_asset_ip_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPAddressesApi->get_asset_ip_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the IP address to list notes of. | 
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

# **get_asset_ip_port_details**
> ClientPortData get_asset_ip_port_details(ip_id, port_id)

Get Port

Get the details of a specific Port asset belonging to an IP Address.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_port_data import ClientPortData
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
    api_instance = watchtowr_api_sdk.IPAddressesApi(api_client)
    ip_id = 'ip_id_example' # str | The asset ID of an IP address with an associated port to get the details of.
    port_id = 'port_id_example' # str | The ID of the Port to retrieve details of.

    try:
        # Get Port
        api_response = api_instance.get_asset_ip_port_details(ip_id, port_id)
        print("The response of IPAddressesApi->get_asset_ip_port_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPAddressesApi->get_asset_ip_port_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_id** | **str**| The asset ID of an IP address with an associated port to get the details of. | 
 **port_id** | **str**| The ID of the Port to retrieve details of. | 

### Return type

[**ClientPortData**](ClientPortData.md)

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

# **get_asset_ip_ports**
> PaginatedClientPort get_asset_ip_ports(id, page=page, page_size=page_size, include_closed_port=include_closed_port, include_no_service=include_no_service, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to)

List Ports

List all discovered Ports belonging to an IP Address, ordered by date identified.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.paginated_client_port import PaginatedClientPort
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
    api_instance = watchtowr_api_sdk.IPAddressesApi(api_client)
    id = 3.4 # float | The asset ID of the IP address to list associated ports of.
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)
    include_closed_port = True # bool | Include listings with closed ports. (optional)
    include_no_service = True # bool | Include listings without a service (optional)
    created_from = '2013-10-20T19:20:30+01:00' # datetime | Filter ports created after a given date and time. (optional)
    created_to = '2013-10-20T19:20:30+01:00' # datetime | Filter ports created before a given date and time. (optional)
    updated_from = '2013-10-20T19:20:30+01:00' # datetime | Filter ports updated after a given date and time. (optional)
    updated_to = '2013-10-20T19:20:30+01:00' # datetime | Filter ports updated before a given date and time. (optional)

    try:
        # List Ports
        api_response = api_instance.get_asset_ip_ports(id, page=page, page_size=page_size, include_closed_port=include_closed_port, include_no_service=include_no_service, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to)
        print("The response of IPAddressesApi->get_asset_ip_ports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPAddressesApi->get_asset_ip_ports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the IP address to list associated ports of. | 
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | [optional] 
 **include_closed_port** | **bool**| Include listings with closed ports. | [optional] 
 **include_no_service** | **bool**| Include listings without a service | [optional] 
 **created_from** | **datetime**| Filter ports created after a given date and time. | [optional] 
 **created_to** | **datetime**| Filter ports created before a given date and time. | [optional] 
 **updated_from** | **datetime**| Filter ports updated after a given date and time. | [optional] 
 **updated_to** | **datetime**| Filter ports updated before a given date and time. | [optional] 

### Return type

[**PaginatedClientPort**](PaginatedClientPort.md)

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

# **get_custom_properties_ip**
> PaginatedClientCustomProperty get_custom_properties_ip(id, page=page, page_size=page_size)

List Custom Properties

List the Custom Properties of a specific IP Address asset.

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
    api_instance = watchtowr_api_sdk.IPAddressesApi(api_client)
    id = 3.4 # float | The asset ID of the IP address to list custom properties of.
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)

    try:
        # List Custom Properties
        api_response = api_instance.get_custom_properties_ip(id, page=page, page_size=page_size)
        print("The response of IPAddressesApi->get_custom_properties_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPAddressesApi->get_custom_properties_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the IP address to list custom properties of. | 
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

# **get_list_asset_ips**
> PaginatedClientIp get_list_asset_ips(page=page, page_size=page_size, asset_name=asset_name, statuses=statuses, source=source, integration_connections=integration_connections, business_unit_ids=business_unit_ids, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, custom_property_key=custom_property_key, custom_property_value=custom_property_value, match_type=match_type)

List IP Addresses

List all discovered IP address assets, ordered by date identified.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.paginated_client_ip import PaginatedClientIp
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
    api_instance = watchtowr_api_sdk.IPAddressesApi(api_client)
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)
    asset_name = '123.123.123.123' # str | Search IP address by name (full or partial). (optional)
    statuses = ['statuses_example'] # List[str] | Filter assets by one or more comma separated asset statuses. Valid statuses are:       * verified       * tracked       * incorrect identification       * pending       * verifiedOutOfScope       * verifiedReducedAttack       * CDN       * hanging cloud ip       * Third Party       * VerifiedHoneypot  (optional)
    source = 'DNS Refresh' # str | Filter assets by the source that discovered the asset. (optional)
    integration_connections = '123:aws,456:azure,789:googlecloud' # str | Filter assets by integration connections (comma-separated list of integrationId:integrationType pairs).      Valid integration types: aws, googlecloud, azure, cloudflare, alibabacloud, prismacloud, prismacloudapigee, huaweicloud, tencentcloud, wiz, servicenowcmdb, akamaiedge, armiscentrix, qualysvmdr  Format: integrationId:integrationType (e.g., 123:aws) Multiple connections: separate with commas (e.g., 123:aws,456:azure,789:googlecloud) (optional)
    business_unit_ids = '1,2,3' # str | Filter assets by a list of comma separated business unit IDs that the asset is related to. (optional)
    created_from = '2013-10-20T19:20:30+01:00' # datetime | Filter assets created after a given date and time. (optional)
    created_to = '2013-10-20T19:20:30+01:00' # datetime | Filter assets created before a given date and time. (optional)
    updated_from = '2013-10-20T19:20:30+01:00' # datetime | Filter assets updated after a given date and time. (optional)
    updated_to = '2013-10-20T19:20:30+01:00' # datetime | Filter assets updated before a given date and time. (optional)
    custom_property_key = 'environment' # str | Filter assets by custom property key. (optional)
    custom_property_value = 'production' # str | Filter assets by custom property value. Must be used together with customPropertyKey. (optional)
    match_type = contains # str | Match assetName searches based on exact names or partial names with contains. Valid match types are:       * contains       * exact  (optional) (default to contains)

    try:
        # List IP Addresses
        api_response = api_instance.get_list_asset_ips(page=page, page_size=page_size, asset_name=asset_name, statuses=statuses, source=source, integration_connections=integration_connections, business_unit_ids=business_unit_ids, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, custom_property_key=custom_property_key, custom_property_value=custom_property_value, match_type=match_type)
        print("The response of IPAddressesApi->get_list_asset_ips:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPAddressesApi->get_list_asset_ips: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | [optional] 
 **asset_name** | **str**| Search IP address by name (full or partial). | [optional] 
 **statuses** | [**List[str]**](str.md)| Filter assets by one or more comma separated asset statuses. Valid statuses are:       * verified       * tracked       * incorrect identification       * pending       * verifiedOutOfScope       * verifiedReducedAttack       * CDN       * hanging cloud ip       * Third Party       * VerifiedHoneypot  | [optional] 
 **source** | **str**| Filter assets by the source that discovered the asset. | [optional] 
 **integration_connections** | **str**| Filter assets by integration connections (comma-separated list of integrationId:integrationType pairs).      Valid integration types: aws, googlecloud, azure, cloudflare, alibabacloud, prismacloud, prismacloudapigee, huaweicloud, tencentcloud, wiz, servicenowcmdb, akamaiedge, armiscentrix, qualysvmdr  Format: integrationId:integrationType (e.g., 123:aws) Multiple connections: separate with commas (e.g., 123:aws,456:azure,789:googlecloud) | [optional] 
 **business_unit_ids** | **str**| Filter assets by a list of comma separated business unit IDs that the asset is related to. | [optional] 
 **created_from** | **datetime**| Filter assets created after a given date and time. | [optional] 
 **created_to** | **datetime**| Filter assets created before a given date and time. | [optional] 
 **updated_from** | **datetime**| Filter assets updated after a given date and time. | [optional] 
 **updated_to** | **datetime**| Filter assets updated before a given date and time. | [optional] 
 **custom_property_key** | **str**| Filter assets by custom property key. | [optional] 
 **custom_property_value** | **str**| Filter assets by custom property value. Must be used together with customPropertyKey. | [optional] 
 **match_type** | **str**| Match assetName searches based on exact names or partial names with contains. Valid match types are:       * contains       * exact  | [optional] [default to contains]

### Return type

[**PaginatedClientIp**](PaginatedClientIp.md)

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

# **unassign_ip_from_business_units**
> ClientIpData unassign_ip_from_business_units(id, business_unit_ids)

Unassign IP from Business Units

Unassign a specific IP asset from a list of Business Units

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_ip_data import ClientIpData
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
    api_instance = watchtowr_api_sdk.IPAddressesApi(api_client)
    id = 3.4 # float | The IP asset's ID.
    business_unit_ids = ['business_unit_ids_example'] # List[str] | List of comma-seperated business unit IDs to unassign from the asset.

    try:
        # Unassign IP from Business Units
        api_response = api_instance.unassign_ip_from_business_units(id, business_unit_ids)
        print("The response of IPAddressesApi->unassign_ip_from_business_units:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPAddressesApi->unassign_ip_from_business_units: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The IP asset&#39;s ID. | 
 **business_unit_ids** | [**List[str]**](str.md)| List of comma-seperated business unit IDs to unassign from the asset. | 

### Return type

[**ClientIpData**](ClientIpData.md)

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

# **update_asset_ip_note**
> ClientNoteData update_asset_ip_note(id, note_id, create_client_note_dto)

Update Note

Update a Note for a specific IP Address asset.

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
    api_instance = watchtowr_api_sdk.IPAddressesApi(api_client)
    id = 3.4 # float | The asset ID of an IP address with a note to update.
    note_id = 3.4 # float | The ID of the note to update.
    create_client_note_dto = watchtowr_api_sdk.CreateClientNoteDto() # CreateClientNoteDto | 

    try:
        # Update Note
        api_response = api_instance.update_asset_ip_note(id, note_id, create_client_note_dto)
        print("The response of IPAddressesApi->update_asset_ip_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPAddressesApi->update_asset_ip_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of an IP address with a note to update. | 
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

# **update_asset_ip_status**
> ClientIpData update_asset_ip_status(id, update_client_legacy_asset_status_dto)

Update Status

Update Status of a specific IP Address asset.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_ip_data import ClientIpData
from watchtowr_api_sdk.models.update_client_legacy_asset_status_dto import UpdateClientLegacyAssetStatusDto
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
    api_instance = watchtowr_api_sdk.IPAddressesApi(api_client)
    id = 3.4 # float | The asset ID of the IP address to update the status of.
    update_client_legacy_asset_status_dto = watchtowr_api_sdk.UpdateClientLegacyAssetStatusDto() # UpdateClientLegacyAssetStatusDto | 

    try:
        # Update Status
        api_response = api_instance.update_asset_ip_status(id, update_client_legacy_asset_status_dto)
        print("The response of IPAddressesApi->update_asset_ip_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPAddressesApi->update_asset_ip_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the IP address to update the status of. | 
 **update_client_legacy_asset_status_dto** | [**UpdateClientLegacyAssetStatusDto**](UpdateClientLegacyAssetStatusDto.md)|  | 

### Return type

[**ClientIpData**](ClientIpData.md)

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

# **update_custom_property_ip**
> ClientCustomProperty update_custom_property_ip(id, custom_property_id, update_client_custom_property_dto)

Update Custom Property

Update a Custom Property for a specific IP Address asset

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
    api_instance = watchtowr_api_sdk.IPAddressesApi(api_client)
    id = 3.4 # float | The asset ID of an IP address with a custom property to update.
    custom_property_id = 3.4 # float | The ID of the custom property to update.
    update_client_custom_property_dto = watchtowr_api_sdk.UpdateClientCustomPropertyDto() # UpdateClientCustomPropertyDto | 

    try:
        # Update Custom Property
        api_response = api_instance.update_custom_property_ip(id, custom_property_id, update_client_custom_property_dto)
        print("The response of IPAddressesApi->update_custom_property_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPAddressesApi->update_custom_property_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of an IP address with a custom property to update. | 
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

