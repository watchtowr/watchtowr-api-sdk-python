# SuspiciousDomains
(*suspicious_domains*)

## Overview

### Available Operations

* [get_list_suspicious_domain](#get_list_suspicious_domain) - List Suspicious Domains
* [get_suspicious_domain_details](#get_suspicious_domain_details) - Get Suspicious Domain Details

## get_list_suspicious_domain

List all discovered suspicious domain assets, ordered by discovery date.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation
from watchtowr_complete_watchtowr_platform_api_documentation_python.utils import parse_datetime


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.suspicious_domains.get_list_suspicious_domain(page=1, page_size=10, created_from=parse_datetime("2022-02-22 22:00:00"), created_to=parse_datetime("2022-02-23 22:00:00"), updated_from=parse_datetime("2022-02-22 22:00:00"), updated_to=parse_datetime("2022-02-23 22:00:00"), search="watchtowr.com", discovery_reason="suspicious-words", whois_search="Name%20Server:%20malicious.ns.com", statuses="pending,malicious,legitimate,benign")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page`                                                                                                                                                           | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.       | 1                                                                                                                                                                |
| `page_size`                                                                                                                                                      | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | 10                                                                                                                                                               |
| `created_from`                                                                                                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                             | :heavy_minus_sign:                                                                                                                                               | Filter suspicious domains created after a given date and time.                                                                                                   | 2022-02-22 22:00:00                                                                                                                                              |
| `created_to`                                                                                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                             | :heavy_minus_sign:                                                                                                                                               | Filter suspicious domains created before a given date and time.                                                                                                  | 2022-02-23 22:00:00                                                                                                                                              |
| `updated_from`                                                                                                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                             | :heavy_minus_sign:                                                                                                                                               | Filter suspicious domains updated after a given date and time.                                                                                                   | 2022-02-22 22:00:00                                                                                                                                              |
| `updated_to`                                                                                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                             | :heavy_minus_sign:                                                                                                                                               | Filter suspicious domains updated before a given date and time.                                                                                                  | 2022-02-23 22:00:00                                                                                                                                              |
| `search`                                                                                                                                                         | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Search suspicious domains by text within the domain.                                                                                                             | watchtowr.com                                                                                                                                                    |
| `discovery_reason`                                                                                                                                               | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Search suspicious domains by discovery reason.                                                                                                                   | suspicious-words                                                                                                                                                 |
| `whois_search`                                                                                                                                                   | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Search suspicious domains by contents of Whois data.                                                                                                             | Name%20Server:%20malicious.ns.com                                                                                                                                |
| `statuses`                                                                                                                                                       | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Filter suspicious domains by a list of comma separated statuses that asset is tagged with.                                                                       | pending,malicious,legitimate,benign                                                                                                                              |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |                                                                                                                                                                  |

### Response

**[models.PaginatedSuspiciousDomain](../../models/paginatedsuspiciousdomain.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## get_suspicious_domain_details

Get the details of a specific suspicious domain.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.suspicious_domains.get_suspicious_domain_details(id=8648.02)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The ID of the suspicious domain to retrieve.                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ClientSuspiciousDomainData](../../models/clientsuspiciousdomaindata.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |