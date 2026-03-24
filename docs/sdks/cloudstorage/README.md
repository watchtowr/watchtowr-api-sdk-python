# CloudStorage
(*cloud_storage*)

## Overview

### Available Operations

* [get_list_asset_cloud_storages](#get_list_asset_cloud_storages) - List Cloud Storage
* [get_asset_cloud_storage_details](#get_asset_cloud_storage_details) - Get Cloud Storage
* [get_asset_cloud_storage_changelog](#get_asset_cloud_storage_changelog) - Get Cloud Storage Changelog
* [update_asset_cloud_storage_status](#update_asset_cloud_storage_status) - Update Status
* [get_asset_cloud_storage_notes](#get_asset_cloud_storage_notes) - List Notes
* [add_asset_cloud_storage_note](#add_asset_cloud_storage_note) - Create Note
* [update_asset_cloud_storage_note](#update_asset_cloud_storage_note) - Update Note
* [delete_asset_cloud_storage_note](#delete_asset_cloud_storage_note) - Delete Note
* [get_custom_properties_cloud_storage](#get_custom_properties_cloud_storage) - List Custom Properties
* [create_custom_property_cloud_storage](#create_custom_property_cloud_storage) - Create Custom Property
* [update_custom_property_cloud_storage](#update_custom_property_cloud_storage) - Update Custom Property
* [delete_custom_property_cloud_storage](#delete_custom_property_cloud_storage) - Delete Custom Property
* [assign_cloud_storage_to_business_units](#assign_cloud_storage_to_business_units) - Assign Cloud Storage to Business Units
* [unassign_cloud_storage_from_business_units](#unassign_cloud_storage_from_business_units) - Unassign Cloud Storage from Business Units
* [set_criticality_cloud_storage](#set_criticality_cloud_storage) - Set Criticality

## get_list_asset_cloud_storages

List all discovered Cloud Storage assets, ordered by date identified.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation
from watchtowr_complete_watchtowr_platform_api_documentation_python.utils import parse_datetime


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_storage.get_list_asset_cloud_storages(page=1, page_size=10, asset_name="watchTowr-aws-bucket", source="module-adversarysight-cloud-integration-aws-s3-buckets", integration_connections="123:aws,456:azure,789:googlecloud", business_unit_ids="1,2,3", created_from=parse_datetime("2022-02-22 22:00:00"), created_to=parse_datetime("2022-02-23 22:00:00"), custom_property_key="environment", custom_property_value="production")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[float]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.                                                                                                                                                                                                                                                                                                                                                                                                                                   | 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `page_size`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | *Optional[float]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 100.                                                                                                                                                                                                                                                                                                                                                                                                                            | 10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `asset_name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Search cloud storage assets by asset name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | watchTowr-aws-bucket                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `statuses`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | List[*str*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by one or more comma separated asset statuses. Valid statuses are:<br/>      * verified<br/>      * tracked<br/>      * incorrect identification<br/>      * pending<br/>      * verifiedOutOfScope                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `source`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by the source that discovered the asset.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | module-adversarysight-cloud-integration-aws-s3-buckets                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `integration_connections`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by integration connections (comma-separated list of integrationId:integrationType pairs).<br/><br/>Valid integration types: aws, googlecloud, azure, cloudflare, alibabacloud, prismacloud, prismacloudapigee, huaweicloud, tencentcloud, wiz, servicenowcmdb, akamaiedge, fastly, markmonitor, armiscentrix, qualysvmdr, tenablevm, orcasecurity, crowdstrikefalconspotlight, taniumvm, rapid7insightvm, fastlywaf, cloudflarewaf, awswaf<br/><br/>Format: integrationId:integrationType (e.g., 123:aws)<br/>Multiple connections: separate with commas (e.g., 123:aws,456:azure,789:googlecloud) | 123:aws,456:azure,789:googlecloud                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `business_unit_ids`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by a list of comma separated business unit IDs that the asset is related to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 1,2,3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `created_from`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets created after a given date and time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 2022-02-22 22:00:00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `created_to`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets created before a given date and time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 2022-02-23 22:00:00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `custom_property_key`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by custom property key.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | environment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `custom_property_value`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by custom property value. Must be used together with customPropertyKey.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | production                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

### Response

**[models.PaginatedClientCloudStorage](../../models/paginatedclientcloudstorage.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## get_asset_cloud_storage_details

Get the details of a specific Cloud Storage asset by asset id.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_storage.get_asset_cloud_storage_details(id=687.49)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The asset ID of the Cloud Storage asset to get.                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ClientCloudStorageData](../../models/clientcloudstoragedata.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_asset_cloud_storage_changelog

Get paginated changelog for a specific Cloud Storage asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_storage.get_asset_cloud_storage_changelog(id=2007.85, page=1, page_size=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                             | *float*                                                                                                                                                          | :heavy_check_mark:                                                                                                                                               | The asset ID of the Cloud Storage to retrieve changelog for.                                                                                                     |                                                                                                                                                                  |
| `page`                                                                                                                                                           | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.       | 1                                                                                                                                                                |
| `page_size`                                                                                                                                                      | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | 10                                                                                                                                                               |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |                                                                                                                                                                  |

### Response

**[models.GetAssetCloudStorageChangelogResponseBody](../../models/getassetcloudstoragechangelogresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## update_asset_cloud_storage_status

Update the Status of a specific Cloud Storage asset.

### Example Usage

```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_storage.update_asset_cloud_storage_status(id=5902.94, status=watchtowr_complete_watchtowr_platform_api_documentation_python.UpdateClientNextGenAssetStatusDtoStatus.VERIFIED, status_reason="Manually verified via Client API")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               | Example                                                                                                   |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                      | *float*                                                                                                   | :heavy_check_mark:                                                                                        | The asset ID of the Cloud Storage asset to update.                                                        |                                                                                                           |
| `status`                                                                                                  | [models.UpdateClientNextGenAssetStatusDtoStatus](../../models/updateclientnextgenassetstatusdtostatus.md) | :heavy_check_mark:                                                                                        | Target status to update.                                                                                  | verified                                                                                                  |
| `status_reason`                                                                                           | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Reason for updating status.                                                                               | Manually verified via Client API                                                                          |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |                                                                                                           |

### Response

**[models.ClientCloudStorageData](../../models/clientcloudstoragedata.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.NotFound     | 404                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## get_asset_cloud_storage_notes

List the Notes of a specific Cloud Storage asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_storage.get_asset_cloud_storage_notes(id=235.51, page=1, page_size=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                             | *float*                                                                                                                                                          | :heavy_check_mark:                                                                                                                                               | The asset ID of the Cloud Storage asset to list notes for.                                                                                                       |                                                                                                                                                                  |
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

## add_asset_cloud_storage_note

Create a Note for a specific Cloud Storage asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_storage.add_asset_cloud_storage_note(id=1780.48, note="Passed to the engineering team. Review on 01/07/2024", title="Initial Review - 01/01/2024")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The asset ID of the Cloud Storage asset to create a new note for.   |                                                                     |
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

## update_asset_cloud_storage_note

Update a Note of a specific Cloud Storage asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_storage.update_asset_cloud_storage_note(id=2445.21, note_id=9434.72, note="Passed to the engineering team. Review on 01/07/2024", title="Initial Review - 01/01/2024")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The asset ID of the Cloud Storage asset with a note to update.      |                                                                     |
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

## delete_asset_cloud_storage_note

Delete a Note of a specific Cloud Storage asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_storage.delete_asset_cloud_storage_note(id=6799.1, note_id=13.87)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The asset ID of the Cloud Storage asset with a note to delete.      |
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

## get_custom_properties_cloud_storage

List the Custom Properties of a specific Cloud Storage.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_storage.get_custom_properties_cloud_storage(id=6528.53, page=1, page_size=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                             | *float*                                                                                                                                                          | :heavy_check_mark:                                                                                                                                               | The asset ID of a Cloud Storage asset to list custom properties of.                                                                                              |                                                                                                                                                                  |
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
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## create_custom_property_cloud_storage

Create a Custom Property for a specific Cloud Storage.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_storage.create_custom_property_cloud_storage(id=1426.62, key="Severity", value={}, is_preset=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                              | *float*                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                | The asset ID of a Cloud Storage asset to create a custom property for.                                                                                                                                                                            |                                                                                                                                                                                                                                                   |
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

## update_custom_property_cloud_storage

Update a Custom Property for a specific Cloud Storage.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_storage.update_custom_property_cloud_storage(id=8083.48, custom_property_id=1400.91, key="Severity", value="Low")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                              | *float*                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                | The asset ID of a Cloud Storage asset with a custom property to update.                                                                                                                                                                           |                                                                                                                                                                                                                                                   |
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

## delete_custom_property_cloud_storage

Delete a Custom Property for a specific Cloud Storage.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_storage.delete_custom_property_cloud_storage(id=3277.87, custom_property_id=7087.69)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `id`                                                                    | *float*                                                                 | :heavy_check_mark:                                                      | The asset ID of a Cloud Storage asset with a custom property to delete. |
| `custom_property_id`                                                    | *float*                                                                 | :heavy_check_mark:                                                      | The ID of the custom property to delete.                                |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.RemoveClientCustomPropertyResponseDto](../../models/removeclientcustompropertyresponsedto.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## assign_cloud_storage_to_business_units

Assign a specific Cloud Storage asset to a list of Business Units

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_storage.assign_cloud_storage_to_business_units(id=6556.77, business_unit_ids=[
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
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The Cloud Storage asset's ID.                                       |                                                                     |
| `business_unit_ids`                                                 | List[*str*]                                                         | :heavy_check_mark:                                                  | List of business unit IDs to assign the asset to.                   | [<br/>1,<br/>2,<br/>3<br/>]                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ClientCloudStorageData](../../models/clientcloudstoragedata.md)**

### Errors

| Error Type                                                        | Status Code                                                       | Content Type                                                      |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| models.Unauthorized                                               | 401                                                               | application/json                                                  |
| models.ForbiddenResponse                                          | 403                                                               | application/json                                                  |
| models.NotFound                                                   | 404                                                               | application/json                                                  |
| models.AssetAndBusinessUnitAlreadyAssociatedConflictErrorResponse | 409                                                               | application/json                                                  |
| models.APIError                                                   | 4XX, 5XX                                                          | \*/\*                                                             |

## unassign_cloud_storage_from_business_units

Unassign a specific Cloud Storage asset from a list of Business Units

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_storage.unassign_cloud_storage_from_business_units(id=7002.56, business_unit_ids=[
        "<value 1>",
        "<value 2>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `id`                                                                  | *float*                                                               | :heavy_check_mark:                                                    | The Cloud Storage asset's ID.                                         |
| `business_unit_ids`                                                   | List[*str*]                                                           | :heavy_check_mark:                                                    | List of comma-seperated business unit IDs to unassign from the asset. |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.ClientCloudStorageData](../../models/clientcloudstoragedata.md)**

### Errors

| Error Type                                                    | Status Code                                                   | Content Type                                                  |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| models.Unauthorized                                           | 401                                                           | application/json                                              |
| models.ForbiddenResponse                                      | 403                                                           | application/json                                              |
| models.NotFound                                               | 404                                                           | application/json                                              |
| models.AssetAndBusinessUnitNotAssociatedConflictErrorResponse | 409                                                           | application/json                                              |
| models.APIError                                               | 4XX, 5XX                                                      | \*/\*                                                         |

## set_criticality_cloud_storage

Set or update the criticality level of a specific Cloud Storage asset.

### Example Usage

```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.cloud_storage.set_criticality_cloud_storage(id=4888.65, criticality=watchtowr_complete_watchtowr_platform_api_documentation_python.Criticality.HIGH)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           | Example                                                                                               |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `id`                                                                                                  | *float*                                                                                               | :heavy_check_mark:                                                                                    | The asset ID of the Cloud Storage to set criticality for.                                             |                                                                                                       |
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