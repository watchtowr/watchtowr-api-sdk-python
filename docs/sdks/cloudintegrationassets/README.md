# CloudIntegrationAssets
(*cloud_integration_assets*)

## Overview

### Available Operations

* [get_list_asset_cloud_asset](#get_list_asset_cloud_asset) - List Cloud Assets
* [get_asset_cloud_asset_details](#get_asset_cloud_asset_details) - Get Cloud Asset Details
* [get_asset_cloud_asset_changelog](#get_asset_cloud_asset_changelog) - Get Cloud Asset Changelog
* [update_asset_cloud_asset_status](#update_asset_cloud_asset_status) - Update Cloud Asset Status
* [get_asset_cloud_asset_notes](#get_asset_cloud_asset_notes) - List Notes
* [add_asset_cloud_asset_note](#add_asset_cloud_asset_note) - Create Note
* [update_asset_cloud_asset_note](#update_asset_cloud_asset_note) - Update Note
* [delete_asset_cloud_asset_note](#delete_asset_cloud_asset_note) - Delete Note
* [get_custom_properties_cloud_asset](#get_custom_properties_cloud_asset) - List Custom Properties
* [create_custom_property_cloud_asset](#create_custom_property_cloud_asset) - Create Custom Property
* [update_custom_property_cloud_asset](#update_custom_property_cloud_asset) - Update Custom Property
* [delete_custom_property_cloud_asset](#delete_custom_property_cloud_asset) - Delete Custom Property
* [assign_cloud_asset_to_business_units](#assign_cloud_asset_to_business_units) - Assign Cloud Integration Asset to Business Units
* [unassign_cloud_asset_from_business_units](#unassign_cloud_asset_from_business_units) - Unassign Cloud Integration Asset from Business Units
* [set_criticality_cloud_asset](#set_criticality_cloud_asset) - Set Criticality

## get_list_asset_cloud_asset

List all discovered Cloud Integration Assets, ordered by date identified.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation
from watchtowr_complete_watchtowr_platform_api_documentation_python.utils import parse_datetime


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_integration_assets.get_list_asset_cloud_asset(page=1, page_size=10, asset_name="example-aws-cloud-asset-rds-database.example.com", source="watchtowr-cloud-integration-aws-snapshot-ebs", integration_connections="123:aws,456:azure,789:googlecloud", business_unit_ids="1,2,3", created_from=parse_datetime("2022-02-22 22:00:00"), created_to=parse_datetime("2022-02-23 22:00:00"), custom_property_key="environment", custom_property_value="production", provider="aws", super_type="database", sub_type="RDS")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[float]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.                                                                                                                                                                                                                                                                                                                                                                                                                                   | 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `page_size`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | *Optional[float]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 100.                                                                                                                                                                                                                                                                                                                                                                                                                            | 10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `asset_name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Search cloud assets by name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | example-aws-cloud-asset-rds-database.example.com                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `statuses`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | List[*str*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by one or more comma separated asset statuses. Valid statuses are:<br/>      * verified<br/>      * incorrect identification<br/>      * pending<br/>      * verifiedOutOfScope<br/>      * verifiedReducedAttack<br/>                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `source`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by the source that discovered the asset.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | watchtowr-cloud-integration-aws-snapshot-ebs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `integration_connections`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by integration connections (comma-separated list of integrationId:integrationType pairs).<br/><br/>Valid integration types: aws, googlecloud, azure, cloudflare, alibabacloud, prismacloud, prismacloudapigee, huaweicloud, tencentcloud, wiz, servicenowcmdb, akamaiedge, fastly, markmonitor, armiscentrix, qualysvmdr, tenablevm, orcasecurity, crowdstrikefalconspotlight, taniumvm, rapid7insightvm, fastlywaf, cloudflarewaf, awswaf<br/><br/>Format: integrationId:integrationType (e.g., 123:aws)<br/>Multiple connections: separate with commas (e.g., 123:aws,456:azure,789:googlecloud) | 123:aws,456:azure,789:googlecloud                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `business_unit_ids`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by a list of comma separated business unit IDs that the asset is related to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 1,2,3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `created_from`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets created after a given date and time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 2022-02-22 22:00:00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `created_to`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets created before a given date and time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 2022-02-23 22:00:00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `custom_property_key`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by custom property key.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | environment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `custom_property_value`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by custom property value. Must be used together with customPropertyKey.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | production                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `provider`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by cloud asset provider.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | aws                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `super_type`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by the cloud asset type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | database                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `sub_type`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by the cloud asset sub-type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | RDS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

### Response

**[models.PaginatedClientCloudAsset](../../models/paginatedclientcloudasset.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## get_asset_cloud_asset_details

Get the details of a specific Cloud Integration Asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_integration_assets.get_asset_cloud_asset_details(id=5722.7)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The asset ID of the Cloud Integration Asset to retrieve.            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ClientCloudAssetData](../../models/clientcloudassetdata.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_asset_cloud_asset_changelog

Get paginated changelog for a specific Cloud Integration Asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_integration_assets.get_asset_cloud_asset_changelog(id=8655.62, page=1, page_size=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                             | *float*                                                                                                                                                          | :heavy_check_mark:                                                                                                                                               | The asset ID of the Cloud Integration Asset to retrieve changelog for.                                                                                           |                                                                                                                                                                  |
| `page`                                                                                                                                                           | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.       | 1                                                                                                                                                                |
| `page_size`                                                                                                                                                      | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | 10                                                                                                                                                               |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |                                                                                                                                                                  |

### Response

**[models.GetAssetCloudAssetChangelogResponseBody](../../models/getassetcloudassetchangelogresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## update_asset_cloud_asset_status

Update the status of a specific Cloud Integration Asset.

### Example Usage

```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_integration_assets.update_asset_cloud_asset_status(id=9985.5, status=watchtowr_complete_watchtowr_platform_api_documentation_python.UpdateClientCloudAssetStatusDtoStatus.VERIFIED, status_reason="Manually verified via Client API")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           | Example                                                                                               |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `id`                                                                                                  | *float*                                                                                               | :heavy_check_mark:                                                                                    | The asset ID of the Cloud Integration Asset to update the status of.                                  |                                                                                                       |
| `status`                                                                                              | [models.UpdateClientCloudAssetStatusDtoStatus](../../models/updateclientcloudassetstatusdtostatus.md) | :heavy_check_mark:                                                                                    | Target status to update.                                                                              | verified                                                                                              |
| `status_reason`                                                                                       | *Optional[str]*                                                                                       | :heavy_minus_sign:                                                                                    | Reason for updating status.                                                                           | Manually verified via Client API                                                                      |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |                                                                                                       |

### Response

**[models.ClientCloudAssetData](../../models/clientcloudassetdata.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.NotFound     | 404                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## get_asset_cloud_asset_notes

List all notes for a specific Cloud Integration Asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_integration_assets.get_asset_cloud_asset_notes(id=1713.14, page=1, page_size=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                             | *float*                                                                                                                                                          | :heavy_check_mark:                                                                                                                                               | The asset ID of the Cloud Integration Asset to list notes of.                                                                                                    |                                                                                                                                                                  |
| `page`                                                                                                                                                           | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.       | 1                                                                                                                                                                |
| `page_size`                                                                                                                                                      | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | 10                                                                                                                                                               |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |                                                                                                                                                                  |

### Response

**[models.ClientNoteListData](../../models/clientnotelistdata.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## add_asset_cloud_asset_note

Create a Note for a specific Cloud Integration Asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_integration_assets.add_asset_cloud_asset_note(id=1371, note="Passed to the engineering team. Review on 01/07/2024", title="Initial Review - 01/01/2024")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `id`                                                                  | *float*                                                               | :heavy_check_mark:                                                    | The asset ID of the Cloud Integration Asset to create a new note for. |                                                                       |
| `note`                                                                | *str*                                                                 | :heavy_check_mark:                                                    | Content of the note.                                                  | Passed to the engineering team. Review on 01/07/2024                  |
| `title`                                                               | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Title of the note.                                                    | Initial Review - 01/01/2024                                           |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |                                                                       |

### Response

**[models.ClientNoteData](../../models/clientnotedata.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## update_asset_cloud_asset_note

Update a Note for a specific Cloud Integration Asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_integration_assets.update_asset_cloud_asset_note(id=9176.02, note_id=2801.75, note="Passed to the engineering team. Review on 01/07/2024", title="Initial Review - 01/01/2024")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The asset ID of a Cloud Integration Asset with a note to update.    |                                                                     |
| `note_id`                                                           | *float*                                                             | :heavy_check_mark:                                                  | The ID of the note to update.                                       |                                                                     |
| `note`                                                              | *str*                                                               | :heavy_check_mark:                                                  | Content of the note.                                                | Passed to the engineering team. Review on 01/07/2024                |
| `title`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Title of the note.                                                  | Initial Review - 01/01/2024                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ClientNoteData](../../models/clientnotedata.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## delete_asset_cloud_asset_note

Delete a Note from a specific Cloud Integration Asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_integration_assets.delete_asset_cloud_asset_note(id=250.46, note_id=885.01)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The asset ID of a Cloud Integration Asset with a note to delete.    |
| `note_id`                                                           | *float*                                                             | :heavy_check_mark:                                                  | The ID of the note to delete.                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteNoteSucces](../../models/deletenotesucces.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_custom_properties_cloud_asset

List the Custom Properties of a specific Cloud Integration Asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_integration_assets.get_custom_properties_cloud_asset(id=8843.52, page=1, page_size=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                             | *float*                                                                                                                                                          | :heavy_check_mark:                                                                                                                                               | The asset ID of the Cloud Integration Asset to list custom properties of.                                                                                        |                                                                                                                                                                  |
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

## create_custom_property_cloud_asset

Create Custom Property for a specific Cloud Integration Asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_integration_assets.create_custom_property_cloud_asset(id=9555.5, key="Severity", value={}, is_preset=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                              | *float*                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                | The asset ID of a Cloud Integration Asset to create a new custom property for.                                                                                                                                                                    |                                                                                                                                                                                                                                                   |
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

## update_custom_property_cloud_asset

Update a Custom Property for a specific Cloud Integration Asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_integration_assets.update_custom_property_cloud_asset(id=7760.25, custom_property_id=6123.66, key="Severity", value="Low")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                              | *float*                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                | The asset ID of a Cloud Integration Asset with a custom property to update.                                                                                                                                                                       |                                                                                                                                                                                                                                                   |
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

## delete_custom_property_cloud_asset

Delete Custom Property for a specific Cloud Integration Asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_integration_assets.delete_custom_property_cloud_asset(id=7567.02, custom_property_id=3400.6)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `id`                                                                        | *float*                                                                     | :heavy_check_mark:                                                          | The asset ID of a Cloud Integration Asset with a custom property to delete. |
| `custom_property_id`                                                        | *float*                                                                     | :heavy_check_mark:                                                          | The ID of the custom property to delete.                                    |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.RemoveClientCustomPropertyResponseDto](../../models/removeclientcustompropertyresponsedto.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## assign_cloud_asset_to_business_units

Assign a specific Cloud Integration Asset to a list of Business Units

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_integration_assets.assign_cloud_asset_to_business_units(id=596.77, business_unit_ids=[
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
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The Cloud Integration Asset's ID.                                   |                                                                     |
| `business_unit_ids`                                                 | List[*str*]                                                         | :heavy_check_mark:                                                  | List of business unit IDs to assign the asset to.                   | [<br/>1,<br/>2,<br/>3<br/>]                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ClientCloudAssetData](../../models/clientcloudassetdata.md)**

### Errors

| Error Type                                                        | Status Code                                                       | Content Type                                                      |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| models.Unauthorized                                               | 401                                                               | application/json                                                  |
| models.ForbiddenResponse                                          | 403                                                               | application/json                                                  |
| models.NotFound                                                   | 404                                                               | application/json                                                  |
| models.AssetAndBusinessUnitAlreadyAssociatedConflictErrorResponse | 409                                                               | application/json                                                  |
| models.APIError                                                   | 4XX, 5XX                                                          | \*/\*                                                             |

## unassign_cloud_asset_from_business_units

Unassign a specific Cloud Integration Asset from a list of Business Units

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_integration_assets.unassign_cloud_asset_from_business_units(id=5098.81, business_unit_ids=[
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
| `id`                                                                  | *float*                                                               | :heavy_check_mark:                                                    | The Cloud Integration Asset's ID.                                     |
| `business_unit_ids`                                                   | List[*str*]                                                           | :heavy_check_mark:                                                    | List of comma-seperated business unit IDs to unassign from the asset. |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.ClientCloudAssetData](../../models/clientcloudassetdata.md)**

### Errors

| Error Type                                                    | Status Code                                                   | Content Type                                                  |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| models.Unauthorized                                           | 401                                                           | application/json                                              |
| models.ForbiddenResponse                                      | 403                                                           | application/json                                              |
| models.NotFound                                               | 404                                                           | application/json                                              |
| models.AssetAndBusinessUnitNotAssociatedConflictErrorResponse | 409                                                           | application/json                                              |
| models.APIError                                               | 4XX, 5XX                                                      | \*/\*                                                         |

## set_criticality_cloud_asset

Set or update the criticality level of a specific Cloud Asset asset.

### Example Usage

```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_integration_assets.set_criticality_cloud_asset(id=4271.66, criticality=watchtowr_complete_watchtowr_platform_api_documentation_python.Criticality.HIGH)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           | Example                                                                                               |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `id`                                                                                                  | *float*                                                                                               | :heavy_check_mark:                                                                                    | The asset ID of the Cloud Asset to set criticality for.                                               |                                                                                                       |
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