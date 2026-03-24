# FindingRetestHistory
(*finding_retest_history*)

## Overview

### Available Operations

* [get_list_finding_retest_history](#get_list_finding_retest_history) - List Finding Retest History

## get_list_finding_retest_history

List all finding retest history entries, ordered by creation date.

### Example Usage

```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.finding_retest_history.get_list_finding_retest_history(page=1, page_size=10, business_unit_ids="1,2,3", sort_by=watchtowr_complete_watchtowr_platform_api_documentation_python.QueryParamSortBy.CREATED_AT, sort_order=watchtowr_complete_watchtowr_platform_api_documentation_python.SortOrder.DESC)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page`                                                                                                                                                           | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.       | 1                                                                                                                                                                |
| `page_size`                                                                                                                                                      | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | 10                                                                                                                                                               |
| `business_unit_ids`                                                                                                                                              | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Filter assets by a list of comma separated business unit IDs that the asset is related to.                                                                       | 1,2,3                                                                                                                                                            |
| `sort_by`                                                                                                                                                        | [Optional[models.QueryParamSortBy]](../../models/queryparamsortby.md)                                                                                            | :heavy_minus_sign:                                                                                                                                               | Sort by field                                                                                                                                                    |                                                                                                                                                                  |
| `sort_order`                                                                                                                                                     | [Optional[models.SortOrder]](../../models/sortorder.md)                                                                                                          | :heavy_minus_sign:                                                                                                                                               | Sort order                                                                                                                                                       |                                                                                                                                                                  |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |                                                                                                                                                                  |

### Response

**[models.PaginatedClientFindingRetestHistory](../../models/paginatedclientfindingretesthistory.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |