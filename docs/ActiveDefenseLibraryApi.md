# watchtowr_api_sdk.ActiveDefenseLibraryApi

All URIs are relative to *https://your-tenant-id.sg.client.watchtowr.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_active_defense_library_rule_details**](ActiveDefenseLibraryApi.md#get_active_defense_library_rule_details) | **GET** /api/client/active-defense-library/show/{ruleId} | Get Active Defense Rule Details
[**get_active_defense_library_rule_provider_template**](ActiveDefenseLibraryApi.md#get_active_defense_library_rule_provider_template) | **GET** /api/client/active-defense-library/show/{ruleId}/provider/show/{provider} | Get Active Defense Rule Provider Template
[**get_list_active_defense_library_rules**](ActiveDefenseLibraryApi.md#get_list_active_defense_library_rules) | **GET** /api/client/active-defense-library/list | List Active Defense Rules


# **get_active_defense_library_rule_details**
> ClientActiveDefenseRuleData get_active_defense_library_rule_details(rule_id)

Get Active Defense Rule Details

Get the details of a specific Active Defense Library rule by rule ID. The `findingsCount` and `affectedKbEntryIds` are scoped to the requesting user’s business units and the organization’s finding impact threshold.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_active_defense_rule_data import ClientActiveDefenseRuleData
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
    api_instance = watchtowr_api_sdk.ActiveDefenseLibraryApi(api_client)
    rule_id = 3.4 # float | The numeric rule ID of the Active Defense Library rule to retrieve.

    try:
        # Get Active Defense Rule Details
        api_response = api_instance.get_active_defense_library_rule_details(rule_id)
        print("The response of ActiveDefenseLibraryApi->get_active_defense_library_rule_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActiveDefenseLibraryApi->get_active_defense_library_rule_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **float**| The numeric rule ID of the Active Defense Library rule to retrieve. | 

### Return type

[**ClientActiveDefenseRuleData**](ClientActiveDefenseRuleData.md)

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
**404** | Rule not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_defense_library_rule_provider_template**
> ClientActiveDefenseRuleProviderData get_active_defense_library_rule_provider_template(rule_id, provider)

Get Active Defense Rule Provider Template

Get the provider-specific rule template (e.g. Cloudflare expression, AWS WAF CFN, Fastly VCL) for a single Active Defense Library rule.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.client_active_defense_rule_provider_data import ClientActiveDefenseRuleProviderData
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
    api_instance = watchtowr_api_sdk.ActiveDefenseLibraryApi(api_client)
    rule_id = 3.4 # float | The numeric rule ID of the Active Defense Library rule.
    provider = 'provider_example' # str | The WAF provider whose rule template should be returned.

    try:
        # Get Active Defense Rule Provider Template
        api_response = api_instance.get_active_defense_library_rule_provider_template(rule_id, provider)
        print("The response of ActiveDefenseLibraryApi->get_active_defense_library_rule_provider_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActiveDefenseLibraryApi->get_active_defense_library_rule_provider_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **float**| The numeric rule ID of the Active Defense Library rule. | 
 **provider** | **str**| The WAF provider whose rule template should be returned. | 

### Return type

[**ClientActiveDefenseRuleProviderData**](ClientActiveDefenseRuleProviderData.md)

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

# **get_list_active_defense_library_rules**
> PaginatedActiveDefenseRules get_list_active_defense_library_rules(page=page, page_size=page_size, search=search)

List Active Defense Rules

List Active Defense Library rules. Rule visibility, ordering and any affected-vulnerability prioritisation are scoped to the requesting user’s business units and the organization’s finding impact threshold.

### Example

* Bearer (API_TOKEN) Authentication (bearer):

```python
import watchtowr_api_sdk
from watchtowr_api_sdk.models.paginated_active_defense_rules import PaginatedActiveDefenseRules
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
    api_instance = watchtowr_api_sdk.ActiveDefenseLibraryApi(api_client)
    page = 1 # float | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. (optional)
    page_size = 10 # float | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. (optional)
    search = 'CVE-2023-34362' # str | Search rules by rule name, CVE ID, or watchTowr vulnerability ID. (optional)

    try:
        # List Active Defense Rules
        api_response = api_instance.get_list_active_defense_library_rules(page=page, page_size=page_size, search=search)
        print("The response of ActiveDefenseLibraryApi->get_list_active_defense_library_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActiveDefenseLibraryApi->get_list_active_defense_library_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**| The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results. | [optional] 
 **page_size** | **float**| The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | [optional] 
 **search** | **str**| Search rules by rule name, CVE ID, or watchTowr vulnerability ID. | [optional] 

### Return type

[**PaginatedActiveDefenseRules**](PaginatedActiveDefenseRules.md)

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

