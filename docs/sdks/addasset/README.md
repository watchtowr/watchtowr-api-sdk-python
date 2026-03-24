# AddAsset
(*add_asset*)

## Overview

### Available Operations

* [submit_asset](#submit_asset) - Submit Seed Data
* [list_submitted_assets](#list_submitted_assets) - List Submitted Assets

## submit_asset

Submit one or more seed data assets to your attack surface for review.

### Example Usage

```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.add_asset.submit_asset(data=[
        {
            "title": "Main Website",
            "type": watchtowr_complete_watchtowr_platform_api_documentation_python.Type.SUBDOMAIN,
            "value": "www.watchTowr.com",
        },
        {
            "title": "Labs Blog IP",
            "type": watchtowr_complete_watchtowr_platform_api_documentation_python.Type.IP,
            "value": "123.123.123.123",
        },
        {
            "title": "IP Range",
            "type": watchtowr_complete_watchtowr_platform_api_documentation_python.Type.IP_RANGE,
            "value": "www.watchTowr.com",
            "values": {
                "cidr": "192.168.1.0/24",
                "asn": "AS16509",
            },
        },
    ], business_units=[
        {
            "id": -1,
            "type": watchtowr_complete_watchtowr_platform_api_documentation_python.FilterByBusinessUnitInputType.UNASSIGNED,
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                     | Example                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `data`                                                                                                                                                                                                                                                          | List[[models.ClientSeedData](../../models/clientseeddata.md)]                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                                                                              | JSON array listing seed data assets to submit for review.                                                                                                                                                                                                       | [<br/>{<br/>"title": "Main Website",<br/>"type": "subdomain",<br/>"value": "www.watchTowr.com"<br/>},<br/>{<br/>"title": "Labs Blog IP",<br/>"type": "ip",<br/>"value": "123.123.123.123"<br/>},<br/>{<br/>"title": "IP Range",<br/>"type": "ipRange",<br/>"values": {<br/>"cidr": "192.168.1.0/24",<br/>"asn": "AS16509"<br/>}<br/>}<br/>] |
| `business_units`                                                                                                                                                                                                                                                | List[[models.FilterByBusinessUnitInput](../../models/filterbybusinessunitinput.md)]                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                              | List of business units to allocate new assets to. -1 indicates UNASSIGNED business unit                                                                                                                                                                         | [<br/>{<br/>"id": -1,<br/>"type": "UNASSIGNED"<br/>}<br/>]                                                                                                                                                                                                      |
| `retries`                                                                                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                                                                                             |                                                                                                                                                                                                                                                                 |

### Response

**[models.ClientSeedDataData](../../models/clientseeddatadata.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## list_submitted_assets

List all submitted seed data assets with pagination and filtering support.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.add_asset.list_submitted_assets(page=1, page_size=20, business_unit_ids="1,2,3")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                         | Type                                                                                                                                                              | Required                                                                                                                                                          | Description                                                                                                                                                       | Example                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page`                                                                                                                                                            | *Optional[float]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.        | 1                                                                                                                                                                 |
| `page_size`                                                                                                                                                       | *Optional[float]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 20. The maximum for pageSize is 100. | 20                                                                                                                                                                |
| `business_unit_ids`                                                                                                                                               | *Optional[str]*                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                | Filter by a list of comma separated business unit IDs that the seed data is related to.                                                                           | 1,2,3                                                                                                                                                             |
| `retries`                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                  | :heavy_minus_sign:                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                               |                                                                                                                                                                   |

### Response

**[models.PaginatedClientSeedData](../../models/paginatedclientseeddata.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |