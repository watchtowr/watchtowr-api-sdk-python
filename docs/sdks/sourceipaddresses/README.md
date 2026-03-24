# SourceIPAddresses
(*source_ip_addresses*)

## Overview

### Available Operations

* [get_list_source_ip_addresses](#get_list_source_ip_addresses) - List Testing Infrastructure

## get_list_source_ip_addresses

List IP addresses and hostnames used by watchTowr for all outbound platform traffic.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.source_ip_addresses.get_list_source_ip_addresses()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `whitelist`                                                         | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Filter by whitelist status (true for whitelisted items only)        |
| `region`                                                            | [Optional[models.Region]](../../models/region.md)                   | :heavy_minus_sign:                                                  | Filter by region                                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ClientSourceIpsAddresses](../../models/clientsourceipsaddresses.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |