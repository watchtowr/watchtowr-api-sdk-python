# MobileApplications
(*mobile_applications*)

## Overview

### Available Operations

* [get_list_asset_mobile_apps](#get_list_asset_mobile_apps) - List Mobile Applications
* [get_asset_mobile_app_details](#get_asset_mobile_app_details) - Get Mobile Application
* [get_asset_mobile_app_changelog](#get_asset_mobile_app_changelog) - Get Mobile Application Changelog
* [update_asset_mobile_app_status](#update_asset_mobile_app_status) - Update Status
* [get_asset_mobile_app_notes](#get_asset_mobile_app_notes) - List Notes
* [create_note_mobile_app](#create_note_mobile_app) - Create Note
* [update_note_mobile_app](#update_note_mobile_app) - Update Note
* [delete_note_mobile_app](#delete_note_mobile_app) - Delete Note
* [get_custom_properties_mobile_app](#get_custom_properties_mobile_app) - List Custom Properties
* [create_custom_property_mobile_app](#create_custom_property_mobile_app) - Create Custom Property
* [update_custom_property_mobile_app](#update_custom_property_mobile_app) - Update Custom Property
* [delete_custom_property_mobile_app](#delete_custom_property_mobile_app) - Delete Custom Property
* [assign_mobile_app_to_business_units](#assign_mobile_app_to_business_units) - Assign Mobile App to Business Units
* [unassign_mobile_app_from_business_units](#unassign_mobile_app_from_business_units) - Unassign Mobile App from Business Units
* [set_criticality_mobile_app](#set_criticality_mobile_app) - Set Criticality

## get_list_asset_mobile_apps

List all discovered Mobile Applications, ordered by date identified.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation
from watchtowr_complete_watchtowr_platform_api_documentation_python.utils import parse_datetime


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.mobile_applications.get_list_asset_mobile_apps(page=1, page_size=10, asset_name="watchTowr-Android", source="module-adversarysight-playstore-mobileapp-discovery", integration_connections="123:aws,456:azure,789:googlecloud", business_unit_ids="1,2,3", created_from=parse_datetime("2022-02-22 22:00:00"), created_to=parse_datetime("2022-02-23 22:00:00"), custom_property_key="environment", custom_property_value="production")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | *Optional[float]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.                                                                                                                                                                                                                                                                                                                                                                                                                                   | 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `page_size`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | *Optional[float]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 100.                                                                                                                                                                                                                                                                                                                                                                                                                            | 10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `asset_name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Search Mobile Applications by assets by name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | watchTowr-Android                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `statuses`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | List[*str*]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by one or more comma separated asset statuses. Valid statuses are:<br/>      * verified<br/>      * tracked<br/>      * incorrect identification<br/>      * pending<br/>      * verifiedOutOfScope<br/>                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `source`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by the source that discovered the asset.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | module-adversarysight-playstore-mobileapp-discovery                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `integration_connections`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by integration connections (comma-separated list of integrationId:integrationType pairs).<br/><br/>Valid integration types: aws, googlecloud, azure, cloudflare, alibabacloud, prismacloud, prismacloudapigee, huaweicloud, tencentcloud, wiz, servicenowcmdb, akamaiedge, fastly, markmonitor, armiscentrix, qualysvmdr, tenablevm, orcasecurity, crowdstrikefalconspotlight, taniumvm, rapid7insightvm, fastlywaf, cloudflarewaf, awswaf<br/><br/>Format: integrationId:integrationType (e.g., 123:aws)<br/>Multiple connections: separate with commas (e.g., 123:aws,456:azure,789:googlecloud) | 123:aws,456:azure,789:googlecloud                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `business_unit_ids`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by a list of comma separated business unit IDs that the asset is related to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 1,2,3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `created_from`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets created after a given date and time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 2022-02-22 22:00:00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `created_to`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets created before a given date and time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 2022-02-23 22:00:00                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `custom_property_key`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by custom property key.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | environment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `custom_property_value`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Filter assets by custom property value. Must be used together with customPropertyKey.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | production                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

### Response

**[models.PaginatedClientMobileApp](../../models/paginatedclientmobileapp.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## get_asset_mobile_app_details

Get the details of a specific Mobile Application.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.mobile_applications.get_asset_mobile_app_details(id=3573.01)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The asset ID of the Mobile Application to get.                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ClientMobileAppData](../../models/clientmobileappdata.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_asset_mobile_app_changelog

Get paginated changelog for a specific Mobile Application.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.mobile_applications.get_asset_mobile_app_changelog(id=6404.02, page=1, page_size=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                             | *float*                                                                                                                                                          | :heavy_check_mark:                                                                                                                                               | The asset ID of the Mobile Application to retrieve changelog for.                                                                                                |                                                                                                                                                                  |
| `page`                                                                                                                                                           | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.       | 1                                                                                                                                                                |
| `page_size`                                                                                                                                                      | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | 10                                                                                                                                                               |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |                                                                                                                                                                  |

### Response

**[models.GetAssetMobileAppChangelogResponseBody](../../models/getassetmobileappchangelogresponsebody.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## update_asset_mobile_app_status

Update Status of a specific Mobile Application asset.

### Example Usage

```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.mobile_applications.update_asset_mobile_app_status(id=7305.94, status=watchtowr_complete_watchtowr_platform_api_documentation_python.UpdateClientNextGenAssetStatusDtoStatus.VERIFIED, status_reason="Manually verified via Client API")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               | Example                                                                                                   |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                      | *float*                                                                                                   | :heavy_check_mark:                                                                                        | The asset ID of the Mobile Application to update status of.                                               |                                                                                                           |
| `status`                                                                                                  | [models.UpdateClientNextGenAssetStatusDtoStatus](../../models/updateclientnextgenassetstatusdtostatus.md) | :heavy_check_mark:                                                                                        | Target status to update.                                                                                  | verified                                                                                                  |
| `status_reason`                                                                                           | *Optional[str]*                                                                                           | :heavy_minus_sign:                                                                                        | Reason for updating status.                                                                               | Manually verified via Client API                                                                          |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |                                                                                                           |

### Response

**[models.ClientMobileAppData](../../models/clientmobileappdata.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.NotFound     | 404                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## get_asset_mobile_app_notes

List the Notes of a specific Mobile Application asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.mobile_applications.get_asset_mobile_app_notes(id=369.99, page=1, page_size=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                             | *float*                                                                                                                                                          | :heavy_check_mark:                                                                                                                                               | The asset ID of the Mobile Application to list notes of.                                                                                                         |                                                                                                                                                                  |
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

## create_note_mobile_app

Create a Note for a specific Mobile Application asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.mobile_applications.create_note_mobile_app(id=6974.85, note="Passed to the engineering team. Review on 01/07/2024", title="Initial Review - 01/01/2024")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The asset ID of the Mobile Application to create a new note for.    |                                                                     |
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

## update_note_mobile_app

Update a Note for a specific Mobile Application asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.mobile_applications.update_note_mobile_app(id=6183.34, note_id=5533.5, note="Passed to the engineering team. Review on 01/07/2024", title="Initial Review - 01/01/2024")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The asset ID of a Mobile Application with a note to update.         |                                                                     |
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

## delete_note_mobile_app

Delete a Note for a specific Mobile Application asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.mobile_applications.delete_note_mobile_app(id=5606.24, note_id=7915.99)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The asset ID of a Mobile Application with a note to delete.         |
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

## get_custom_properties_mobile_app

List the Custom Properties of a specific Mobile Application asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.mobile_applications.get_custom_properties_mobile_app(id=6206.97, page=1, page_size=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                             | *float*                                                                                                                                                          | :heavy_check_mark:                                                                                                                                               | The asset ID of the Mobile Application to list custom properties of.                                                                                             |                                                                                                                                                                  |
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

## create_custom_property_mobile_app

Create a Custom Property for a specific Mobile Application asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.mobile_applications.create_custom_property_mobile_app(id=3935.7, key="Severity", value={}, is_preset=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                              | *float*                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                | The asset ID of the Mobile Application to create a new custom property for.                                                                                                                                                                       |                                                                                                                                                                                                                                                   |
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

## update_custom_property_mobile_app

Update a Custom Property for a specific Mobile Application asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.mobile_applications.update_custom_property_mobile_app(id=6298.24, custom_property_id=7250.3, key="Severity", value="Low")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                              | *float*                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                | The asset ID of a Mobile Application with a custom property to update.                                                                                                                                                                            |                                                                                                                                                                                                                                                   |
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

## delete_custom_property_mobile_app

Delete a Custom Property for a specific Mobile Application asset.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.mobile_applications.delete_custom_property_mobile_app(id=8660.78, custom_property_id=7129.52)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *float*                                                                | :heavy_check_mark:                                                     | The asset ID of a Mobile Application with a custom property to delete. |
| `custom_property_id`                                                   | *float*                                                                | :heavy_check_mark:                                                     | The ID of the custom property to delete.                               |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[models.RemoveClientCustomPropertyResponseDto](../../models/removeclientcustompropertyresponsedto.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## assign_mobile_app_to_business_units

Assign a specific Mobile App asset to a list of Business Units

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.mobile_applications.assign_mobile_app_to_business_units(id=8964.59, business_unit_ids=[
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
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The Mobile App asset's ID.                                          |                                                                     |
| `business_unit_ids`                                                 | List[*str*]                                                         | :heavy_check_mark:                                                  | List of business unit IDs to assign the asset to.                   | [<br/>1,<br/>2,<br/>3<br/>]                                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ClientMobileAppData](../../models/clientmobileappdata.md)**

### Errors

| Error Type                                                        | Status Code                                                       | Content Type                                                      |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| models.Unauthorized                                               | 401                                                               | application/json                                                  |
| models.ForbiddenResponse                                          | 403                                                               | application/json                                                  |
| models.NotFound                                                   | 404                                                               | application/json                                                  |
| models.AssetAndBusinessUnitAlreadyAssociatedConflictErrorResponse | 409                                                               | application/json                                                  |
| models.APIError                                                   | 4XX, 5XX                                                          | \*/\*                                                             |

## unassign_mobile_app_from_business_units

Unassign a specific Mobile App asset from a list of Business Units

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.mobile_applications.unassign_mobile_app_from_business_units(id=9779.35, business_unit_ids=[
        "<value 1>",
        "<value 2>",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `id`                                                                  | *float*                                                               | :heavy_check_mark:                                                    | The Mobile App asset's ID.                                            |
| `business_unit_ids`                                                   | List[*str*]                                                           | :heavy_check_mark:                                                    | List of comma-seperated business unit IDs to unassign from the asset. |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.ClientMobileAppData](../../models/clientmobileappdata.md)**

### Errors

| Error Type                                                    | Status Code                                                   | Content Type                                                  |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| models.Unauthorized                                           | 401                                                           | application/json                                              |
| models.ForbiddenResponse                                      | 403                                                           | application/json                                              |
| models.NotFound                                               | 404                                                           | application/json                                              |
| models.AssetAndBusinessUnitNotAssociatedConflictErrorResponse | 409                                                           | application/json                                              |
| models.APIError                                               | 4XX, 5XX                                                      | \*/\*                                                         |

## set_criticality_mobile_app

Set or update the criticality level of a specific Mobile App asset.

### Example Usage

```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.mobile_applications.set_criticality_mobile_app(id=9489.86, criticality=watchtowr_complete_watchtowr_platform_api_documentation_python.Criticality.HIGH)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           | Example                                                                                               |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `id`                                                                                                  | *float*                                                                                               | :heavy_check_mark:                                                                                    | The asset ID of the Mobile App to set criticality for.                                                |                                                                                                       |
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