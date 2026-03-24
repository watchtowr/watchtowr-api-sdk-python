# Ports
(*ports*)

## Overview

### Available Operations

* [get_list_asset_ports](#get_list_asset_ports) - List Ports
* [get_asset_port_details](#get_asset_port_details) - Get Port

## get_list_asset_ports

List all discovered Ports for all IP Addresses, ordered by date identified.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation
from watchtowr_complete_watchtowr_platform_api_documentation_python.utils import parse_datetime


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.ports.get_list_asset_ports(page=1, page_size=10, created_from=parse_datetime("2022-02-22 22:00:00"), created_to=parse_datetime("2022-02-23 22:00:00"), asset_name="80", business_unit_ids="1,2,3", custom_property_key="environment", custom_property_value="production")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                         | Type                                                                                                                                                              | Required                                                                                                                                                          | Description                                                                                                                                                       | Example                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page`                                                                                                                                                            | *Optional[float]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.        | 1                                                                                                                                                                 |
| `page_size`                                                                                                                                                       | *Optional[float]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 100. | 10                                                                                                                                                                |
| `include_closed_port`                                                                                                                                             | *Optional[bool]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                | Include listings with closed ports.                                                                                                                               |                                                                                                                                                                   |
| `include_no_service`                                                                                                                                              | *Optional[bool]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                | Include listings without a service                                                                                                                                |                                                                                                                                                                   |
| `created_from`                                                                                                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                              | :heavy_minus_sign:                                                                                                                                                | Filter ports created after a given date and time.                                                                                                                 | 2022-02-22 22:00:00                                                                                                                                               |
| `created_to`                                                                                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                              | :heavy_minus_sign:                                                                                                                                                | Filter ports created before a given date and time.                                                                                                                | 2022-02-23 22:00:00                                                                                                                                               |
| `asset_name`                                                                                                                                                      | *Optional[str]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | Search ports by port number.                                                                                                                                      | 80                                                                                                                                                                |
| `business_unit_ids`                                                                                                                                               | *Optional[str]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | Filter assets by a list of comma separated business unit IDs that the asset is related to.                                                                        | 1,2,3                                                                                                                                                             |
| `custom_property_key`                                                                                                                                             | *Optional[str]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | Filter assets by custom property key.                                                                                                                             | environment                                                                                                                                                       |
| `custom_property_value`                                                                                                                                           | *Optional[str]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | Filter assets by custom property value. Must be used together with customPropertyKey.                                                                             | production                                                                                                                                                        |
| `retries`                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                  | :heavy_minus_sign:                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                               |                                                                                                                                                                   |

### Response

**[models.PaginatedClientPort](../../models/paginatedclientport.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## get_asset_port_details

Get the details of a specific Port asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.ports.get_asset_port_details(id=2113.83)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The asset ID of a Port to get.                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ClientPortData](../../models/clientportdata.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |