# PointsOfInterestSDK
(*points_of_interest*)

## Overview

### Available Operations

* [get_list_points_of_interest](#get_list_points_of_interest) - List Points of Interest
* [convert_poi_to_finding](#convert_poi_to_finding) - Convert Point of Interest to Finding

## get_list_points_of_interest

List all discovered Points of Interest assets, ordered by discovery date.

### Example Usage

```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation
from watchtowr_complete_watchtowr_platform_api_documentation_python.utils import parse_datetime


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.points_of_interest.get_list_points_of_interest(page=1, page_size=10, created_from=parse_datetime("2022-02-22 22:00:00"), created_to=parse_datetime("2022-02-23 22:00:00"), updated_from=parse_datetime("2022-02-22 22:00:00"), updated_to=parse_datetime("2022-02-23 22:00:00"), discovered_date_order=watchtowr_complete_watchtowr_platform_api_documentation_python.DiscoveredDateOrder.DESC, search="Apache%20Airflow%20Admin%20Login", types="admin-panel,open-directory", has_finding=False, start_date=parse_datetime("2022-02-23 22:00:00"), end_date=parse_datetime("2022-02-23 22:00:00"), asset_statuses="verified,Unregistered,Parked,Incorrect Identification,pending,VerifiedOutOfScope,VerifiedReducedAttack,Tracked,CDN,Hanging Cloud IP,VerifiedHoneypot,Third Party", business_unit_ids="1,2,3", suppression_filter=watchtowr_complete_watchtowr_platform_api_documentation_python.QueryParamSuppressionFilter.NON_SUPPRESSED)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page`                                                                                                                                                           | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.       | 1                                                                                                                                                                |
| `page_size`                                                                                                                                                      | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | 10                                                                                                                                                               |
| `created_from`                                                                                                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                             | :heavy_minus_sign:                                                                                                                                               | Filter points of interest created after a given date and time.                                                                                                   | 2022-02-22 22:00:00                                                                                                                                              |
| `created_to`                                                                                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                             | :heavy_minus_sign:                                                                                                                                               | Filter points of interest created before a given date and time.                                                                                                  | 2022-02-23 22:00:00                                                                                                                                              |
| `updated_from`                                                                                                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                             | :heavy_minus_sign:                                                                                                                                               | Filter points of interest updated after a given date and time.                                                                                                   | 2022-02-22 22:00:00                                                                                                                                              |
| `updated_to`                                                                                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                             | :heavy_minus_sign:                                                                                                                                               | Filter points of interest updated before a given date and time.                                                                                                  | 2022-02-23 22:00:00                                                                                                                                              |
| `discovered_date_order`                                                                                                                                          | [Optional[models.DiscoveredDateOrder]](../../models/discovereddateorder.md)                                                                                      | :heavy_minus_sign:                                                                                                                                               | Order points of interest by their discovery date.                                                                                                                | DESC                                                                                                                                                             |
| `search`                                                                                                                                                         | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Search Points of Interest by name or URL.                                                                                                                        | Apache%20Airflow%20Admin%20Login                                                                                                                                 |
| `types`                                                                                                                                                          | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Filter by a comma separated list of types.                                                                                                                       | admin-panel,open-directory                                                                                                                                       |
| `has_finding`                                                                                                                                                    | *Optional[bool]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Filter points of interest that have findings.                                                                                                                    | false                                                                                                                                                            |
| `start_date`                                                                                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                             | :heavy_minus_sign:                                                                                                                                               | Filter points of interest by start date.                                                                                                                         | 2022-02-23 22:00:00                                                                                                                                              |
| `end_date`                                                                                                                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                             | :heavy_minus_sign:                                                                                                                                               | Filter points of interest by end date.                                                                                                                           | 2022-02-23 22:00:00                                                                                                                                              |
| `asset_statuses`                                                                                                                                                 | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Filter points of interest by a comma separated list of asset statuses.                                                                                           | verified,Unregistered,Parked,Incorrect Identification,pending,VerifiedOutOfScope,VerifiedReducedAttack,Tracked,CDN,Hanging Cloud IP,VerifiedHoneypot,Third Party |
| `business_unit_ids`                                                                                                                                              | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Filter points of interest by a comma separated list of business unit IDs.                                                                                        | 1,2,3                                                                                                                                                            |
| `suppression_filter`                                                                                                                                             | [Optional[models.QueryParamSuppressionFilter]](../../models/queryparamsuppressionfilter.md)                                                                      | :heavy_minus_sign:                                                                                                                                               | Filter points of interest by suppression status.                                                                                                                 | non-suppressed                                                                                                                                                   |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |                                                                                                                                                                  |

### Response

**[models.PaginatedPointOfInterest](../../models/paginatedpointofinterest.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## convert_poi_to_finding

Convert a Point of Interest to a finding. The POI must exist and not already have a finding associated with it.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.points_of_interest.convert_poi_to_finding(id=6980.65)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The ID of the Point of Interest to convert to a finding.            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PointsOfInterestData](../../models/pointsofinterestdata.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |