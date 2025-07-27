# watchtowr_api_sdk.DNSRecordAnalysisApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_dns_records**](DNSRecordAnalysisApi.md#get_list_dns_records) | **GET** /api/client/dns-records/list | List DNS Records


# **get_list_dns_records**
> PaginatedClientDnsRecord get_list_dns_records(page=page, page_size=page_size, business_unit_ids=business_unit_ids, sort_by=sort_by, sort_order=sort_order, asset_name=asset_name, record_name=record_name, record_value=record_value, record_types=record_types, start_date=start_date, end_date=end_date)

List DNS Records

List all DNS records with filtering and pagination support.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.paginated_client_dns_record import PaginatedClientDnsRecord
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
    api_instance = watchtowr_api_sdk.DNSRecordAnalysisApi(api_client)
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 20 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 20. The maximum for pageSize is 100. (optional)
    business_unit_ids = '1,2,3' # str | Filter assets by a list of comma separated business unit IDs that the asset is related to. (optional)
    sort_by = createdAt # str | Sort by field (optional) (default to createdAt)
    sort_order = DESC # str | Sort order (optional) (default to DESC)
    asset_name = 'example.com' # str | Filter by asset name (optional)
    record_name = 'example.com' # str | Filter by record name (optional)
    record_value = '192.168.1.1' # str | Filter by record value (optional)
    record_types = 'A,AAAA,CNAME' # str | Filter by record types (comma separated) (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Filter by start date (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Filter by end date (optional)

    try:
        # List DNS Records
        api_response = api_instance.get_list_dns_records(page=page, page_size=page_size, business_unit_ids=business_unit_ids, sort_by=sort_by, sort_order=sort_order, asset_name=asset_name, record_name=record_name, record_value=record_value, record_types=record_types, start_date=start_date, end_date=end_date)
        print("The response of DNSRecordAnalysisApi->get_list_dns_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSRecordAnalysisApi->get_list_dns_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 20. The maximum for pageSize is 100. | [optional] 
 **business_unit_ids** | **str**| Filter assets by a list of comma separated business unit IDs that the asset is related to. | [optional] 
 **sort_by** | **str**| Sort by field | [optional] [default to createdAt]
 **sort_order** | **str**| Sort order | [optional] [default to DESC]
 **asset_name** | **str**| Filter by asset name | [optional] 
 **record_name** | **str**| Filter by record name | [optional] 
 **record_value** | **str**| Filter by record value | [optional] 
 **record_types** | **str**| Filter by record types (comma separated) | [optional] 
 **start_date** | **datetime**| Filter by start date | [optional] 
 **end_date** | **datetime**| Filter by end date | [optional] 

### Return type

[**PaginatedClientDnsRecord**](PaginatedClientDnsRecord.md)

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

