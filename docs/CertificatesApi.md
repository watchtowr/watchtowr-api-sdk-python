# openapi_client.CertificatesApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_certificate_details**](CertificatesApi.md#get_certificate_details) | **GET** /api/client/certificates/show/{id} | Get Certificate Details
[**get_list_certificates**](CertificatesApi.md#get_list_certificates) | **GET** /api/client/certificates/list | List Certificates


# **get_certificate_details**
> ClientServiceInformationResponseData get_certificate_details(id)

Get Certificate Details

Get the details of a specific TLS/SSL certificate.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.client_service_information_response_data import ClientServiceInformationResponseData
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
    api_instance = openapi_client.CertificatesApi(api_client)
    id = 3.4 # float | The asset ID of the certificate to retrieve.

    try:
        # Get Certificate Details
        api_response = api_instance.get_certificate_details(id)
        print("The response of CertificatesApi->get_certificate_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->get_certificate_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**| The asset ID of the certificate to retrieve. | 

### Return type

[**ClientServiceInformationResponseData**](ClientServiceInformationResponseData.md)

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

# **get_list_certificates**
> PaginatedServiceInformationResponse get_list_certificates(page=page, page_size=page_size, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, not_after_from=not_after_from, not_after_to=not_after_to, subject_common_name_search=subject_common_name_search, subject_alt_name_search=subject_alt_name_search, subject_organisation_search=subject_organisation_search, subject_countries=subject_countries, asset_name_search=asset_name_search, statuses=statuses, business_unit_ids=business_unit_ids)

List Certificates

List all discovered TLS/SSL certificate assets, ordered by discovery date.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import openapi_client
from openapi_client.models.paginated_service_information_response import PaginatedServiceInformationResponse
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
    api_instance = openapi_client.CertificatesApi(api_client)
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)
    created_from = '2013-10-20T19:20:30+01:00' # datetime | Filter certificates created after a given date and time. (optional)
    created_to = '2013-10-20T19:20:30+01:00' # datetime | Filter certificates created before a given date and time. (optional)
    updated_from = '2013-10-20T19:20:30+01:00' # datetime | Filter certificates updated after a given date and time. (optional)
    updated_to = '2013-10-20T19:20:30+01:00' # datetime | Filter certificates updated before a given date and time. (optional)
    not_after_from = '2013-10-20T19:20:30+01:00' # datetime | Filter certificates that do not expire after a given date and time. (optional)
    not_after_to = '2013-10-20T19:20:30+01:00' # datetime | Filter certificates that do not expire before a given date and time. (optional)
    subject_common_name_search = 'example.com' # str | Search certificates by Subject Common Name. (optional)
    subject_alt_name_search = 'example.com' # str | Search certificates by Subject Alt Name. (optional)
    subject_organisation_search = 'example' # str | Search by subject organization. (optional)
    subject_countries = ['subject_countries_example'] # List[str] | Filter certificates by a list of comma separated subject countries that they're related to. (optional)
    asset_name_search = 'example.watchTowr.com' # str | Search Certificates by the name of the associated asset. (optional)
    statuses = 'Expired,Expiring Within 30 Days,Valid' # str | Filter certificates by a list of comma separated statuses that they're tagged with. (optional)
    business_unit_ids = '1,2,3' # str | Filter certificates by a list of comma separated business unit IDs they're related to. (optional)

    try:
        # List Certificates
        api_response = api_instance.get_list_certificates(page=page, page_size=page_size, created_from=created_from, created_to=created_to, updated_from=updated_from, updated_to=updated_to, not_after_from=not_after_from, not_after_to=not_after_to, subject_common_name_search=subject_common_name_search, subject_alt_name_search=subject_alt_name_search, subject_organisation_search=subject_organisation_search, subject_countries=subject_countries, asset_name_search=asset_name_search, statuses=statuses, business_unit_ids=business_unit_ids)
        print("The response of CertificatesApi->get_list_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->get_list_certificates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | [optional] 
 **created_from** | **datetime**| Filter certificates created after a given date and time. | [optional] 
 **created_to** | **datetime**| Filter certificates created before a given date and time. | [optional] 
 **updated_from** | **datetime**| Filter certificates updated after a given date and time. | [optional] 
 **updated_to** | **datetime**| Filter certificates updated before a given date and time. | [optional] 
 **not_after_from** | **datetime**| Filter certificates that do not expire after a given date and time. | [optional] 
 **not_after_to** | **datetime**| Filter certificates that do not expire before a given date and time. | [optional] 
 **subject_common_name_search** | **str**| Search certificates by Subject Common Name. | [optional] 
 **subject_alt_name_search** | **str**| Search certificates by Subject Alt Name. | [optional] 
 **subject_organisation_search** | **str**| Search by subject organization. | [optional] 
 **subject_countries** | [**List[str]**](str.md)| Filter certificates by a list of comma separated subject countries that they&#39;re related to. | [optional] 
 **asset_name_search** | **str**| Search Certificates by the name of the associated asset. | [optional] 
 **statuses** | **str**| Filter certificates by a list of comma separated statuses that they&#39;re tagged with. | [optional] 
 **business_unit_ids** | **str**| Filter certificates by a list of comma separated business unit IDs they&#39;re related to. | [optional] 

### Return type

[**PaginatedServiceInformationResponse**](PaginatedServiceInformationResponse.md)

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

