# PlatformWhitelisting
(*platform_whitelisting*)

## Overview

### Available Operations

* [get_platform_dashboard_whitelist_ips](#get_platform_dashboard_whitelist_ips) - List Dashboard Whitelisted IPs
* [create_platform_dashboard_whitelist_ip](#create_platform_dashboard_whitelist_ip) - Add Dashboard Whitelisted IP
* [get_platform_dashboard_whitelist_status](#get_platform_dashboard_whitelist_status) - Get Dashboard Whitelisting Status
* [update_platform_dashboard_whitelist_status](#update_platform_dashboard_whitelist_status) - Update Dashboard Whitelisting Status
* [update_platform_dashboard_whitelist_ip](#update_platform_dashboard_whitelist_ip) - Update Dashboard Whitelisted IP
* [delete_platform_dashboard_whitelist_ip](#delete_platform_dashboard_whitelist_ip) - Remove Dashboard Whitelisted IP
* [get_platform_api_whitelist_ips](#get_platform_api_whitelist_ips) - List API Whitelisted IPs
* [create_platform_api_whitelist_ip](#create_platform_api_whitelist_ip) - Add API Whitelisted IP
* [get_platform_api_whitelist_status](#get_platform_api_whitelist_status) - Get API Whitelisting Status
* [update_platform_api_whitelist_status](#update_platform_api_whitelist_status) - Update API Whitelisting Status
* [update_platform_api_whitelist_ip](#update_platform_api_whitelist_ip) - Update API Whitelisted IP
* [delete_platform_api_whitelist_ip](#delete_platform_api_whitelist_ip) - Remove API Whitelisted IP

## get_platform_dashboard_whitelist_ips

Get all IP addresses whitelisted for dashboard access. Admin role required.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.platform_whitelisting.get_platform_dashboard_whitelist_ips()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WhitelistIPListData](../../models/whitelistiplistdata.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.UnauthorizedResponse | 401                         | application/json            |
| models.ForbiddenResponse    | 403                         | application/json            |
| models.APIError             | 4XX, 5XX                    | \*/\*                       |

## create_platform_dashboard_whitelist_ip

Add a new IP address to the dashboard whitelist. Admin role required.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.platform_whitelisting.create_platform_dashboard_whitelist_ip(ip="192.168.1.1", description="Office network")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ip`                                                                | *str*                                                               | :heavy_check_mark:                                                  | IP address or CIDR range to whitelist                               | 192.168.1.1                                                         |
| `description`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Description of the IP address                                       | Office network                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.WhitelistIPDataSingle](../../models/whitelistipdatasingle.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.BadRequestResponse   | 400                         | application/json            |
| models.UnauthorizedResponse | 401                         | application/json            |
| models.ForbiddenResponse    | 403                         | application/json            |
| models.APIError             | 4XX, 5XX                    | \*/\*                       |

## get_platform_dashboard_whitelist_status

Get the current status of dashboard IP whitelisting. Admin role required.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.platform_whitelisting.get_platform_dashboard_whitelist_status()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WhitelistStatusData](../../models/whiteliststatusdata.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.UnauthorizedResponse | 401                         | application/json            |
| models.ForbiddenResponse    | 403                         | application/json            |
| models.APIError             | 4XX, 5XX                    | \*/\*                       |

## update_platform_dashboard_whitelist_status

Enable or disable dashboard IP whitelisting. Admin role required.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.platform_whitelisting.update_platform_dashboard_whitelist_status(enabled=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `enabled`                                                           | *bool*                                                              | :heavy_check_mark:                                                  | Enable or disable whitelisting                                      | true                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.WhitelistStatusData](../../models/whiteliststatusdata.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.UnauthorizedResponse | 401                         | application/json            |
| models.ForbiddenResponse    | 403                         | application/json            |
| models.APIError             | 4XX, 5XX                    | \*/\*                       |

## update_platform_dashboard_whitelist_ip

Update an existing dashboard whitelisted IP address. Admin role required.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.platform_whitelisting.update_platform_dashboard_whitelist_ip(id_param=9748.85, id=1, ip="192.168.1.1", description="Office network")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id_param`                                                          | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | IP address ID                                                       | 1                                                                   |
| `ip`                                                                | *str*                                                               | :heavy_check_mark:                                                  | IP address or CIDR range to whitelist                               | 192.168.1.1                                                         |
| `description`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Description of the IP address                                       | Office network                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.WhitelistIPDataSingle](../../models/whitelistipdatasingle.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.BadRequestResponse   | 400                         | application/json            |
| models.UnauthorizedResponse | 401                         | application/json            |
| models.ForbiddenResponse    | 403                         | application/json            |
| models.NotFoundResponse     | 404                         | application/json            |
| models.APIError             | 4XX, 5XX                    | \*/\*                       |

## delete_platform_dashboard_whitelist_ip

Remove an IP address from the dashboard whitelist. Admin role required.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.platform_whitelisting.delete_platform_dashboard_whitelist_ip(id=2946.55)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteWhitelistIPData](../../models/deletewhitelistipdata.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.UnauthorizedResponse | 401                         | application/json            |
| models.ForbiddenResponse    | 403                         | application/json            |
| models.NotFoundResponse     | 404                         | application/json            |
| models.APIError             | 4XX, 5XX                    | \*/\*                       |

## get_platform_api_whitelist_ips

Get all IP addresses whitelisted for API access. Admin role required.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.platform_whitelisting.get_platform_api_whitelist_ips()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WhitelistIPListData](../../models/whitelistiplistdata.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.UnauthorizedResponse | 401                         | application/json            |
| models.ForbiddenResponse    | 403                         | application/json            |
| models.APIError             | 4XX, 5XX                    | \*/\*                       |

## create_platform_api_whitelist_ip

Add a new IP address to the API whitelist. Admin role required.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.platform_whitelisting.create_platform_api_whitelist_ip(ip="192.168.1.1", description="Office network")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `ip`                                                                | *str*                                                               | :heavy_check_mark:                                                  | IP address or CIDR range to whitelist                               | 192.168.1.1                                                         |
| `description`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Description of the IP address                                       | Office network                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.WhitelistIPDataSingle](../../models/whitelistipdatasingle.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.BadRequestResponse   | 400                         | application/json            |
| models.UnauthorizedResponse | 401                         | application/json            |
| models.ForbiddenResponse    | 403                         | application/json            |
| models.APIError             | 4XX, 5XX                    | \*/\*                       |

## get_platform_api_whitelist_status

Get the current status of API IP whitelisting. Admin role required.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.platform_whitelisting.get_platform_api_whitelist_status()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.WhitelistStatusData](../../models/whiteliststatusdata.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.UnauthorizedResponse | 401                         | application/json            |
| models.ForbiddenResponse    | 403                         | application/json            |
| models.APIError             | 4XX, 5XX                    | \*/\*                       |

## update_platform_api_whitelist_status

Enable or disable API IP whitelisting. Admin role required.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.platform_whitelisting.update_platform_api_whitelist_status(enabled=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `enabled`                                                           | *bool*                                                              | :heavy_check_mark:                                                  | Enable or disable whitelisting                                      | true                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.WhitelistStatusData](../../models/whiteliststatusdata.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.UnauthorizedResponse | 401                         | application/json            |
| models.ForbiddenResponse    | 403                         | application/json            |
| models.APIError             | 4XX, 5XX                    | \*/\*                       |

## update_platform_api_whitelist_ip

Update an existing API whitelisted IP address. Admin role required.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.platform_whitelisting.update_platform_api_whitelist_ip(id_param=8772.98, id=1, ip="192.168.1.1", description="Office network")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id_param`                                                          | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | IP address ID                                                       | 1                                                                   |
| `ip`                                                                | *str*                                                               | :heavy_check_mark:                                                  | IP address or CIDR range to whitelist                               | 192.168.1.1                                                         |
| `description`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | Description of the IP address                                       | Office network                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.WhitelistIPDataSingle](../../models/whitelistipdatasingle.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.BadRequestResponse   | 400                         | application/json            |
| models.UnauthorizedResponse | 401                         | application/json            |
| models.ForbiddenResponse    | 403                         | application/json            |
| models.NotFoundResponse     | 404                         | application/json            |
| models.APIError             | 4XX, 5XX                    | \*/\*                       |

## delete_platform_api_whitelist_ip

Remove an IP address from the API whitelist. Admin role required.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.platform_whitelisting.delete_platform_api_whitelist_ip(id=2913.28)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteWhitelistIPData](../../models/deletewhitelistipdata.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.UnauthorizedResponse | 401                         | application/json            |
| models.ForbiddenResponse    | 403                         | application/json            |
| models.NotFoundResponse     | 404                         | application/json            |
| models.APIError             | 4XX, 5XX                    | \*/\*                       |