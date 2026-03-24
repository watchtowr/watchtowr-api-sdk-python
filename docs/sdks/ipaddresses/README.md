# IPAddresses
(*ip_addresses*)

## Overview

### Available Operations

* [get_list_asset_ips](#get_list_asset_ips) - List IP Addresses
* [get_asset_ip_details](#get_asset_ip_details) - Get IP Address Details
* [get_asset_ip_changelog](#get_asset_ip_changelog) - Get IP Address Changelog
* [get_asset_ip_ports](#get_asset_ip_ports) - List Ports
* [get_asset_ip_port_details](#get_asset_ip_port_details) - Get Port
* [update_asset_ip_status](#update_asset_ip_status) - Update Status
* [get_asset_ip_notes](#get_asset_ip_notes) - List Notes
* [create_asset_ip_note](#create_asset_ip_note) - Create Note
* [update_asset_ip_note](#update_asset_ip_note) - Update Note
* [delete_asset_ip_note](#delete_asset_ip_note) - Delete Note
* [get_asset_ip_dns_records](#get_asset_ip_dns_records) - List DNS Records
* [get_custom_properties_ip](#get_custom_properties_ip) - List Custom Properties
* [create_custom_property_ip](#create_custom_property_ip) - Create Custom Property
* [update_custom_property_ip](#update_custom_property_ip) - Update Custom Property
* [delete_custom_property_ip](#delete_custom_property_ip) - Delete Custom Property
* [assign_ip_to_business_units](#assign_ip_to_business_units) - Assign IP to Business Units
* [unassign_ip_from_business_units](#unassign_ip_from_business_units) - Unassign IP from Business Units
* [get_asset_ip_engine_settings](#get_asset_ip_engine_settings) - Get IP Engine Settings
* [update_asset_ip_engine_settings](#update_asset_ip_engine_settings) - Update IP Engine Settings
* [set_criticality_ip](#set_criticality_ip) - Set Criticality

## get_list_asset_ips

List all discovered IP Address assets, ordered by date identified.

### Example Usage

```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation
from watchtowr_complete_watchtowr_platform_api_documentation_python.utils import parse_datetime


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.ip_addresses.get_list_asset_ips(page=1, page_size=10, asset_name="123.123.123.123", source="DNS Refresh", integration_connections="123:aws,456:azure,789:googlecloud", business_unit_ids="1,2,3", created_from=parse_datetime("2022-02-22 22:00:00"), created_to=parse_datetime("2022-02-23 22:00:00"), custom_property_key="environment", custom_property_value="production", match_type=watchtowr_complete_watchtowr_platform_api_documentation_python.MatchType.EXACT)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[float]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.                                                                                                                                                                                                                                                                                                                                                                                                                                   | 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `page_size`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | *Optional[float]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 100.                                                                                                                                                                                                                                                                                                                                                                                                                            | 10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `asset_name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Search IP address by name (full or partial).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 123.123.123.123                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `statuses`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | List[*str*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by one or more comma separated asset statuses. Valid statuses are:<br/>      * verified<br/>      * tracked<br/>      * incorrect identification<br/>      * pending<br/>      * verifiedOutOfScope<br/>      * verifiedReducedAttack<br/>      * CDN<br/>      * hanging cloud ip<br/>      * Third Party<br/>      * VerifiedHoneypot<br/>                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `source`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by the source that discovered the asset.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | DNS Refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `integration_connections`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by integration connections (comma-separated list of integrationId:integrationType pairs).<br/><br/>Valid integration types: aws, googlecloud, azure, cloudflare, alibabacloud, prismacloud, prismacloudapigee, huaweicloud, tencentcloud, wiz, servicenowcmdb, akamaiedge, fastly, markmonitor, armiscentrix, qualysvmdr, tenablevm, orcasecurity, crowdstrikefalconspotlight, taniumvm, rapid7insightvm, fastlywaf, cloudflarewaf, awswaf<br/><br/>Format: integrationId:integrationType (e.g., 123:aws)<br/>Multiple connections: separate with commas (e.g., 123:aws,456:azure,789:googlecloud) | 123:aws,456:azure,789:googlecloud                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `business_unit_ids`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by a list of comma separated business unit IDs that the asset is related to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 1,2,3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `created_from`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets created after a given date and time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 2022-02-22 22:00:00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `created_to`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets created before a given date and time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 2022-02-23 22:00:00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `custom_property_key`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by custom property key.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | environment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `custom_property_value`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by custom property value. Must be used together with customPropertyKey.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | production                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `match_type`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [Optional[models.MatchType]](../../models/matchtype.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Match assetName searches based on exact names or partial names with contains. Valid match types are:<br/>      * contains<br/>      * exact<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                             | exact                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

### Response

**[models.PaginatedClientIP](../../models/paginatedclientip.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## get_asset_ip_details

Get the details of a specific IP Address asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.ip_addresses.get_asset_ip_details(id=7467.21)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The asset ID of the IP address to retrieve.                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ClientIPData](../../models/clientipdata.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_asset_ip_changelog

Get paginated changelog for a specific IP Address asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.ip_addresses.get_asset_ip_changelog(id=4270.41, page=1, page_size=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                             | *float*                                                                                                                                                          | :heavy_check_mark:                                                                                                                                               | The asset ID of the IP Address to retrieve changelog for.                                                                                                        |                                                                                                                                                                  |
| `page`                                                                                                                                                           | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.       | 1                                                                                                                                                                |
| `page_size`                                                                                                                                                      | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | 10                                                                                                                                                               |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |                                                                                                                                                                  |

### Response

**[models.GetAssetIPChangelogResponseBody](../../models/getassetipchangelogresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_asset_ip_ports

List all discovered Ports belonging to an IP Address, ordered by date identified.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation
from watchtowr_complete_watchtowr_platform_api_documentation_python.utils import parse_datetime


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.ip_addresses.get_asset_ip_ports(id=7387.86, page=1, page_size=10, created_from=parse_datetime("2022-02-22 22:00:00"), created_to=parse_datetime("2022-02-23 22:00:00"))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                         | Type                                                                                                                                                              | Required                                                                                                                                                          | Description                                                                                                                                                       | Example                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                              | *float*                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                | The asset ID of the IP address to list associated ports of.                                                                                                       |                                                                                                                                                                   |
| `page`                                                                                                                                                            | *Optional[float]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.        | 1                                                                                                                                                                 |
| `page_size`                                                                                                                                                       | *Optional[float]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 100. | 10                                                                                                                                                                |
| `include_closed_port`                                                                                                                                             | *Optional[bool]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                | Include listings with closed ports.                                                                                                                               |                                                                                                                                                                   |
| `include_no_service`                                                                                                                                              | *Optional[bool]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                | Include listings without a service                                                                                                                                |                                                                                                                                                                   |
| `created_from`                                                                                                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                              | :heavy_minus_sign:                                                                                                                                                | Filter ports created after a given date and time.                                                                                                                 | 2022-02-22 22:00:00                                                                                                                                               |
| `created_to`                                                                                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                              | :heavy_minus_sign:                                                                                                                                                | Filter ports created before a given date and time.                                                                                                                | 2022-02-23 22:00:00                                                                                                                                               |
| `retries`                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                  | :heavy_minus_sign:                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                               |                                                                                                                                                                   |

### Response

**[models.PaginatedClientPort](../../models/paginatedclientport.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.NotFound     | 404                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## get_asset_ip_port_details

Get the details of a specific Port asset belonging to an IP Address.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.ip_addresses.get_asset_ip_port_details(ip_id="<id>", port_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `ip_id`                                                                      | *str*                                                                        | :heavy_check_mark:                                                           | The asset ID of an IP address with an associated port to get the details of. |
| `port_id`                                                                    | *str*                                                                        | :heavy_check_mark:                                                           | The ID of the Port to retrieve details of.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[models.ClientPortData](../../models/clientportdata.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## update_asset_ip_status

Update Status of a specific IP Address asset.

### Example Usage

```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.ip_addresses.update_asset_ip_status(id=3787.99, status=watchtowr_complete_watchtowr_platform_api_documentation_python.UpdateClientLegacyAssetStatusDtoStatus.VERIFIED, status_reason="Manually verified via Client API")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             | Example                                                                                                 |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                    | *float*                                                                                                 | :heavy_check_mark:                                                                                      | The asset ID of the IP address to update the status of.                                                 |                                                                                                         |
| `status`                                                                                                | [models.UpdateClientLegacyAssetStatusDtoStatus](../../models/updateclientlegacyassetstatusdtostatus.md) | :heavy_check_mark:                                                                                      | Target status to update.                                                                                | verified                                                                                                |
| `status_reason`                                                                                         | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | Reason for updating status.                                                                             | Manually verified via Client API                                                                        |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |                                                                                                         |

### Response

**[models.ClientIPData](../../models/clientipdata.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.NotFound     | 404                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## get_asset_ip_notes

List Notes of a specific IP Address asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.ip_addresses.get_asset_ip_notes(id=2433.39, page=1, page_size=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                             | *float*                                                                                                                                                          | :heavy_check_mark:                                                                                                                                               | The asset ID of the IP address to list notes of.                                                                                                                 |                                                                                                                                                                  |
| `page`                                                                                                                                                           | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.       | 1                                                                                                                                                                |
| `page_size`                                                                                                                                                      | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | 10                                                                                                                                                               |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |                                                                                                                                                                  |

### Response

**[models.ClientNoteListData](../../models/clientnotelistdata.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.NotFound     | 404                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## create_asset_ip_note

Create a Note for a specific IP Address asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.ip_addresses.create_asset_ip_note(id=8240.07, note="Passed to the engineering team. Review on 01/07/2024", title="Initial Review - 01/01/2024")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The asset ID of an IP address to create a new note for.             |                                                                     |
| `note`                                                              | *str*                                                               | :heavy_check_mark:                                                  | Content of the note.                                                | Passed to the engineering team. Review on 01/07/2024                |
| `title`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Title of the note.                                                  | Initial Review - 01/01/2024                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ClientNoteData](../../models/clientnotedata.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.NotFound     | 404                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## update_asset_ip_note

Update a Note for a specific IP Address asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.ip_addresses.update_asset_ip_note(id=7597.28, note_id=2432.86, note="Passed to the engineering team. Review on 01/07/2024", title="Initial Review - 01/01/2024")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The asset ID of an IP address with a note to update.                |                                                                     |
| `note_id`                                                           | *float*                                                             | :heavy_check_mark:                                                  | The ID of the note to update.                                       |                                                                     |
| `note`                                                              | *str*                                                               | :heavy_check_mark:                                                  | Content of the note.                                                | Passed to the engineering team. Review on 01/07/2024                |
| `title`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Title of the note.                                                  | Initial Review - 01/01/2024                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ClientNoteData](../../models/clientnotedata.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.NotFound     | 404                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## delete_asset_ip_note

Delete a Note for a specific IP Address asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.ip_addresses.delete_asset_ip_note(id=9970.66, note_id=100.21)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The asset ID of an IP address with a note to delete.                |
| `note_id`                                                           | *float*                                                             | :heavy_check_mark:                                                  | The ID of the note to delete.                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteNoteSucces](../../models/deletenotesucces.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.NotFound     | 404                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## get_asset_ip_dns_records

List DNS Records of a specific IP Address asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.ip_addresses.get_asset_ip_dns_records(id=6924.2, page=1, page_size=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                             | *float*                                                                                                                                                          | :heavy_check_mark:                                                                                                                                               | The asset ID of the IP address to list DNS records of.                                                                                                           |                                                                                                                                                                  |
| `page`                                                                                                                                                           | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.       | 1                                                                                                                                                                |
| `page_size`                                                                                                                                                      | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | 10                                                                                                                                                               |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |                                                                                                                                                                  |

### Response

**[models.ClientIPDNSRecordResponse](../../models/clientipdnsrecordresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.NotFound     | 404                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## get_custom_properties_ip

List the Custom Properties of a specific IP Address asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.ip_addresses.get_custom_properties_ip(id=7835.27, page=1, page_size=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                             | *float*                                                                                                                                                          | :heavy_check_mark:                                                                                                                                               | The asset ID of the IP address to list custom properties of.                                                                                                     |                                                                                                                                                                  |
| `page`                                                                                                                                                           | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.       | 1                                                                                                                                                                |
| `page_size`                                                                                                                                                      | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | 10                                                                                                                                                               |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |                                                                                                                                                                  |

### Response

**[models.PaginatedClientCustomProperty](../../models/paginatedclientcustomproperty.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## create_custom_property_ip

Create a Custom Property for a specific IP Address asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.ip_addresses.create_custom_property_ip(id=8002.01, key="Severity", value={}, is_preset=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                              | *float*                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                | The asset ID of the IP address to create a new custom property for.                                                                                                                                                                               |                                                                                                                                                                                                                                                   |
| `key`                                                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                | The key of the custom property. Key provided must not be empty and must be unique for the model type. If is_preset is true, key must belong to one of watchTowr's preset custom properties. Accepted preset keys include: 'Criticality'.          | Severity                                                                                                                                                                                                                                          |
| `value`                                                                                                                                                                                                                                           | [models.Value](../../models/value.md)                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                | The value of the custom property. If existing custom property's preset is true, the value supplied must belong to one of the valid watchTowr preset values. Accepted preset values are 'Low', 'Medium', 'High', 'Unknown' for key: 'Criticality'. | Low                                                                                                                                                                                                                                               |
| `is_preset`                                                                                                                                                                                                                                       | *Optional[bool]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                | Defaults to false. If true, custom property is a watchTowr preset custom property.                                                                                                                                                                | false                                                                                                                                                                                                                                             |
| `retries`                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                               |                                                                                                                                                                                                                                                   |

### Response

**[models.ClientCustomProperty](../../models/clientcustomproperty.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## update_custom_property_ip

Update a Custom Property for a specific IP Address asset

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.ip_addresses.update_custom_property_ip(id=9900.76, custom_property_id=9160.55, key="Severity", value="Low")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                              | *float*                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                | The asset ID of an IP address with a custom property to update.                                                                                                                                                                                   |                                                                                                                                                                                                                                                   |
| `custom_property_id`                                                                                                                                                                                                                              | *float*                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                | The ID of the custom property to update.                                                                                                                                                                                                          |                                                                                                                                                                                                                                                   |
| `key`                                                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                | The key of the custom property. Key provided must not be empty and must be unique for the model type. If is_preset is true, key must belong to one of watchTowr's preset custom properties. Accepted preset keys include: 'Criticality'.          | Severity                                                                                                                                                                                                                                          |
| `value`                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                | The value of the custom property. If existing custom property's preset is true, the value supplied must belong to one of the valid watchTowr preset values. Accepted preset values are 'Low', 'Medium', 'High', 'Unknown' for key: 'Criticality'. | Low                                                                                                                                                                                                                                               |
| `retries`                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                               |                                                                                                                                                                                                                                                   |

### Response

**[models.ClientCustomProperty](../../models/clientcustomproperty.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## delete_custom_property_ip

Delete a Custom Property for a specific IP Address asset

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.ip_addresses.delete_custom_property_ip(id=9074.67, custom_property_id=1283.99)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The asset ID of an IP address with a custom property to delete.     |
| `custom_property_id`                                                | *float*                                                             | :heavy_check_mark:                                                  | The ID of the custom property to delete.                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RemoveClientCustomPropertyResponseDto](../../models/removeclientcustompropertyresponsedto.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## assign_ip_to_business_units

Assign a specific IP asset to a list of Business Units

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.ip_addresses.assign_ip_to_business_units(id=970.96, business_unit_ids=[
        "1",
        "2",
        "3",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The IP asset's ID.                                                  |                                                                     |
| `business_unit_ids`                                                 | List[*str*]                                                         | :heavy_check_mark:                                                  | List of business unit IDs to assign the asset to.                   | [<br/>1,<br/>2,<br/>3<br/>]                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ClientIPData](../../models/clientipdata.md)**

### Errors

| Error Type                                                        | Status Code                                                       | Content Type                                                      |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| models.Unauthorized                                               | 401                                                               | application/json                                                  |
| models.ForbiddenResponse                                          | 403                                                               | application/json                                                  |
| models.NotFound                                                   | 404                                                               | application/json                                                  |
| models.AssetAndBusinessUnitAlreadyAssociatedConflictErrorResponse | 409                                                               | application/json                                                  |
| models.APIError                                                   | 4XX, 5XX                                                          | \*/\*                                                             |

## unassign_ip_from_business_units

Unassign a specific IP asset from a list of Business Units

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.ip_addresses.unassign_ip_from_business_units(id=6802.38, business_unit_ids=[
        "<value 1>",
        "<value 2>",
        "<value 3>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `id`                                                                  | *float*                                                               | :heavy_check_mark:                                                    | The IP asset's ID.                                                    |
| `business_unit_ids`                                                   | List[*str*]                                                           | :heavy_check_mark:                                                    | List of comma-seperated business unit IDs to unassign from the asset. |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.ClientIPData](../../models/clientipdata.md)**

### Errors

| Error Type                                                    | Status Code                                                   | Content Type                                                  |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| models.Unauthorized                                           | 401                                                           | application/json                                              |
| models.ForbiddenResponse                                      | 403                                                           | application/json                                              |
| models.NotFound                                               | 404                                                           | application/json                                              |
| models.AssetAndBusinessUnitNotAssociatedConflictErrorResponse | 409                                                           | application/json                                              |
| models.APIError                                               | 4XX, 5XX                                                      | \*/\*                                                         |

## get_asset_ip_engine_settings

Get the engine settings for a specific IP asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.ip_addresses.get_asset_ip_engine_settings(id=7494.92)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The asset ID of the IP to retrieve engine settings for.             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ClientEngineSettingsData](../../models/clientenginesettingsdata.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## update_asset_ip_engine_settings

Update the engine settings for a specific IP asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.ip_addresses.update_asset_ip_engine_settings(id=8507.82, adversary_sight_enabled=True, dns_bruteforcing_enabled=False, automated_red_teaming_enabled=True, intrusive_http_checks_enabled=True, credential_stuffing_enabled=True, rapid_reaction_enabled=True)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   | Example                                                                       |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `id`                                                                          | *float*                                                                       | :heavy_check_mark:                                                            | The asset ID of the IP to update engine settings for.                         |                                                                               |
| `adversary_sight_enabled`                                                     | *bool*                                                                        | :heavy_check_mark:                                                            | This setting manages the Adversary Sight engine coverage for the asset.       | true                                                                          |
| `dns_bruteforcing_enabled`                                                    | *bool*                                                                        | :heavy_check_mark:                                                            | This setting manages the DNS Bruteforcing engine coverage for the asset.      | false                                                                         |
| `automated_red_teaming_enabled`                                               | *bool*                                                                        | :heavy_check_mark:                                                            | This setting manages the Automated Red Teaming engine coverage for the asset. | true                                                                          |
| `intrusive_http_checks_enabled`                                               | *bool*                                                                        | :heavy_check_mark:                                                            | This setting manages Intrusive HTTP Check engine coverage for the asset.      | true                                                                          |
| `credential_stuffing_enabled`                                                 | *bool*                                                                        | :heavy_check_mark:                                                            | This setting manages the Credential Stuffing engine coverage for the asset.   | true                                                                          |
| `rapid_reaction_enabled`                                                      | *bool*                                                                        | :heavy_check_mark:                                                            | 	This setting manages the Rapid Reaction engine coverage for the asset        | true                                                                          |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |                                                                               |

### Response

**[models.ClientEngineSettingsData](../../models/clientenginesettingsdata.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## set_criticality_ip

Set or update the criticality level of a specific IP asset.

### Example Usage

```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.ip_addresses.set_criticality_ip(id=7513.65, criticality=watchtowr_complete_watchtowr_platform_api_documentation_python.Criticality.HIGH)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           | Example                                                                                               |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `id`                                                                                                  | *float*                                                                                               | :heavy_check_mark:                                                                                    | The asset ID of the IP to set criticality for.                                                        |                                                                                                       |
| `criticality`                                                                                         | [models.Criticality](../../models/criticality.md)                                                     | :heavy_check_mark:                                                                                    | The criticality level to assign to the asset. Accepted values are 'High', 'Medium', 'Low', 'Unknown'. | High                                                                                                  |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |                                                                                                       |

### Response

**[models.SetCriticalityDataResponseDto](../../models/setcriticalitydataresponsedto.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |