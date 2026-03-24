# PendingDomains
(*pending_domains*)

## Overview

### Available Operations

* [get_list_pending_domains](#get_list_pending_domains) - List Pending Domains

## get_list_pending_domains

List all pending domain assets with filtering and pagination support.

### Example Usage

```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation
from watchtowr_complete_watchtowr_platform_api_documentation_python.utils import parse_datetime


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.pending_domains.get_list_pending_domains(page=1, page_size=10, name="example.com", source="example-source", start_date=parse_datetime("2022-02-23 22:00:00"), end_date=parse_datetime("2022-02-23 22:00:00"), sort_by=watchtowr_complete_watchtowr_platform_api_documentation_python.GetListPendingDomainsQueryParamSortBy.CREATED_AT, sort_order=watchtowr_complete_watchtowr_platform_api_documentation_python.GetListPendingDomainsQueryParamSortOrder.DESC)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                         | Type                                                                                                                                                              | Required                                                                                                                                                          | Description                                                                                                                                                       | Example                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page`                                                                                                                                                            | *Optional[float]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.        | 1                                                                                                                                                                 |
| `page_size`                                                                                                                                                       | *Optional[float]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 100. | 10                                                                                                                                                                |
| `name`                                                                                                                                                            | *Optional[str]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | Filter by domain name                                                                                                                                             | example.com                                                                                                                                                       |
| `source`                                                                                                                                                          | *Optional[str]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | Filter by source that discovered the domain                                                                                                                       | example-source                                                                                                                                                    |
| `start_date`                                                                                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                              | :heavy_minus_sign:                                                                                                                                                | Filter by start date                                                                                                                                              | 2022-02-23 22:00:00                                                                                                                                               |
| `end_date`                                                                                                                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                              | :heavy_minus_sign:                                                                                                                                                | Filter by end date                                                                                                                                                | 2022-02-23 22:00:00                                                                                                                                               |
| `sort_by`                                                                                                                                                         | [Optional[models.GetListPendingDomainsQueryParamSortBy]](../../models/getlistpendingdomainsqueryparamsortby.md)                                                   | :heavy_minus_sign:                                                                                                                                                | Sort by field                                                                                                                                                     |                                                                                                                                                                   |
| `sort_order`                                                                                                                                                      | [Optional[models.GetListPendingDomainsQueryParamSortOrder]](../../models/getlistpendingdomainsqueryparamsortorder.md)                                             | :heavy_minus_sign:                                                                                                                                                | Sort order                                                                                                                                                        |                                                                                                                                                                   |
| `retries`                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                  | :heavy_minus_sign:                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                               |                                                                                                                                                                   |

### Response

**[models.PaginatedClientPendingDomain](../../models/paginatedclientpendingdomain.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |