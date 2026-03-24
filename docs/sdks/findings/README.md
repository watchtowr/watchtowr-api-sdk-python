# Findings
(*findings*)

## Overview

### Available Operations

* [get_list_findings](#get_list_findings) - List Findings
* [get_finding_details](#get_finding_details) - Get Finding Details
* [export_pdf_for_finding](#export_pdf_for_finding) - Export Finding PDF
* [get_available_finding_statuses](#get_available_finding_statuses) - List Finding Statuses
* [update_finding_status](#update_finding_status) - Update Finding Status
* [update_finding_state](#update_finding_state) - Update Finding State
* [start_specific_finding_retest](#start_specific_finding_retest) - Retest Finding
* [get_finding_notes](#get_finding_notes) - List Finding Notes
* [create_finding_note](#create_finding_note) - Create Finding Note
* [create_finding_manual_ticket](#create_finding_manual_ticket) - Create Finding Manual Ticket
* [update_finding_note](#update_finding_note) - Update Finding Note
* [delete_finding_note](#delete_finding_note) - Delete Finding Note
* [get_custom_properties_finding](#get_custom_properties_finding) - List Custom Properties
* [create_custom_property_finding](#create_custom_property_finding) - Create Custom Property
* [update_custom_property_finding](#update_custom_property_finding) - Update Custom Property
* [delete_custom_property_finding](#delete_custom_property_finding) - Delete Custom Property

## get_list_findings

List all discovered findings, ordered by date identified.

### Example Usage

```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation
from watchtowr_complete_watchtowr_platform_api_documentation_python.utils import parse_datetime


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.findings.get_list_findings(page=1, page_size=10, created_from=parse_datetime("2022-02-22 22:00:00"), created_to=parse_datetime("2022-02-23 22:00:00"), updated_from=parse_datetime("2022-02-22 22:00:00"), updated_to=parse_datetime("2022-02-23 22:00:00"), statuses="confirmed,unconfirmed,remediated,risk-accepted,closed,asset-no-longer-tracked", business_unit_ids="1,2,3", finding_title="Valid%20Credentials%20Discovered", severities=watchtowr_complete_watchtowr_platform_api_documentation_python.Severities.MEDIUM, asset_title="www.watchTowr.com", asset_types=watchtowr_complete_watchtowr_platform_api_documentation_python.AssetTypes.PORT, tags="CISA-KEV,Defacement,Credentials", only_validated_exploitable=False, only_unacknowledged=False, exploitation_risk_level=watchtowr_complete_watchtowr_platform_api_documentation_python.ExploitationRiskLevel.HIGH)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                     | Type                                                                                                                                                                                                                                                                                                                                                          | Required                                                                                                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                   | Example                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page`                                                                                                                                                                                                                                                                                                                                                        | *Optional[float]*                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.                                                                                                                                                                                                    | 1                                                                                                                                                                                                                                                                                                                                                             |
| `page_size`                                                                                                                                                                                                                                                                                                                                                   | *Optional[float]*                                                                                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30.                                                                                                                                                                                              | 10                                                                                                                                                                                                                                                                                                                                                            |
| `created_from`                                                                                                                                                                                                                                                                                                                                                | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | Filter findings created after a given date and time.                                                                                                                                                                                                                                                                                                          | 2022-02-22 22:00:00                                                                                                                                                                                                                                                                                                                                           |
| `created_to`                                                                                                                                                                                                                                                                                                                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | Filter findings created before a given date and time.                                                                                                                                                                                                                                                                                                         | 2022-02-23 22:00:00                                                                                                                                                                                                                                                                                                                                           |
| `updated_from`                                                                                                                                                                                                                                                                                                                                                | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | Filter findings updated after a given date and time.                                                                                                                                                                                                                                                                                                          | 2022-02-22 22:00:00                                                                                                                                                                                                                                                                                                                                           |
| `updated_to`                                                                                                                                                                                                                                                                                                                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | Filter findings updated before a given date and time.                                                                                                                                                                                                                                                                                                         | 2022-02-23 22:00:00                                                                                                                                                                                                                                                                                                                                           |
| `statuses`                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | Filter findings by a list of comma separated statuses they're tagged with.                                                                                                                                                                                                                                                                                    | confirmed,unconfirmed,remediated,risk-accepted,closed,asset-no-longer-tracked                                                                                                                                                                                                                                                                                 |
| `business_unit_ids`                                                                                                                                                                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | Filter findings by a list of comma separated business unit IDs that they're related to.                                                                                                                                                                                                                                                                       | 1,2,3                                                                                                                                                                                                                                                                                                                                                         |
| `finding_impact_threshold`                                                                                                                                                                                                                                                                                                                                    | [Optional[models.FindingImpactThreshold]](../../models/findingimpactthreshold.md)                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | Impact Setting:<br/>* High - Prioritized Findings (vulnerabilities, misconfigurations and weaknesses) that could have an immediate, direct impact on your organization's security posture.<br/>* All - All Findings, a broader range of findings that may not directly impact your organization's security posture, but may represent deviations from best practices. |                                                                                                                                                                                                                                                                                                                                                               |
| `finding_title`                                                                                                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | Search findings by title contents.                                                                                                                                                                                                                                                                                                                            | Valid%20Credentials%20Discovered                                                                                                                                                                                                                                                                                                                              |
| `severities`                                                                                                                                                                                                                                                                                                                                                  | [Optional[models.Severities]](../../models/severities.md)                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | Filter findings by a list of comma separated severities they're tagged with.                                                                                                                                                                                                                                                                                  | critical,high,medium,low,info                                                                                                                                                                                                                                                                                                                                 |
| `asset_title`                                                                                                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | Search by findings by affected asset.                                                                                                                                                                                                                                                                                                                         | www.watchTowr.com                                                                                                                                                                                                                                                                                                                                             |
| `asset_types`                                                                                                                                                                                                                                                                                                                                                 | [Optional[models.AssetTypes]](../../models/assettypes.md)                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | Filter findings by a comma separated list of affected asset types.                                                                                                                                                                                                                                                                                            | domain,subdomain,ip                                                                                                                                                                                                                                                                                                                                           |
| `assignee`                                                                                                                                                                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>Filter findings by assignee. To filter findings that don't have an assignee, please use assignee=No Assignee.                                                                                                                | John Smith                                                                                                                                                                                                                                                                                                                                                    |
| `tags`                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | Filter findings by a comma separated list of tags.                                                                                                                                                                                                                                                                                                            | CISA-KEV,Defacement,Credentials                                                                                                                                                                                                                                                                                                                               |
| `only_validated_exploitable`                                                                                                                                                                                                                                                                                                                                  | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | Filter to only show findings validated as exploitable.                                                                                                                                                                                                                                                                                                        | true                                                                                                                                                                                                                                                                                                                                                          |
| `only_unacknowledged`                                                                                                                                                                                                                                                                                                                                         | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | Filter to only show unacknowledged findings.                                                                                                                                                                                                                                                                                                                  | true                                                                                                                                                                                                                                                                                                                                                          |
| `exploitation_risk_level`                                                                                                                                                                                                                                                                                                                                     | [Optional[models.ExploitationRiskLevel]](../../models/exploitationrisklevel.md)                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | Filter findings by a comma separated list of exploitation risk levels.                                                                                                                                                                                                                                                                                        | Unknown,Moderate,High                                                                                                                                                                                                                                                                                                                                         |
| `retries`                                                                                                                                                                                                                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                               |

### Response

**[models.PaginatedClientFindings](../../models/paginatedclientfindings.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## get_finding_details

Get the details of a specific finding.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.findings.get_finding_details(id=8884.68)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The ID of the finding to retrieve.                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ClientFindingData](../../models/clientfindingdata.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## export_pdf_for_finding

Export a PDF report for a specific finding.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    complete_watchtowr_platform_api_documentation.findings.export_pdf_for_finding(id=717.37)

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The ID of the finding to export.                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_available_finding_statuses

List all available statuses for findings.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    complete_watchtowr_platform_api_documentation.findings.get_available_finding_statuses()

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## update_finding_status

Update the status of a specific finding.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.findings.update_finding_status(id=515.74, status="confirmed", status_reason="Reason for change")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The ID of the finding to update.                                    |                                                                     |
| `status`                                                            | *str*                                                               | :heavy_check_mark:                                                  | Finding status.                                                     | confirmed                                                           |
| `status_reason`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Reason for the status change.                                       | Reason for change                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ClientFindingData](../../models/clientfindingdata.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## update_finding_state

Update the state of a specific finding.

### Example Usage

```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.findings.update_finding_state(id=431.2, state=watchtowr_complete_watchtowr_platform_api_documentation_python.UpdateClientFindingStateRequestBodyState.IN_PROGRESS)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 | Example                                                                                                     |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                        | *float*                                                                                                     | :heavy_check_mark:                                                                                          | The ID of the finding to update.                                                                            |                                                                                                             |
| `state`                                                                                                     | [models.UpdateClientFindingStateRequestBodyState](../../models/updateclientfindingstaterequestbodystate.md) | :heavy_check_mark:                                                                                          | Finding state. Different to status, this is about tracking how the finding is being handled.                | In Progress                                                                                                 |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |                                                                                                             |

### Response

**[models.ClientFindingData](../../models/clientfindingdata.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## start_specific_finding_retest

Initiate a retest for a specific finding.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.findings.start_specific_finding_retest(finding_id=3023.54, include_dns_connected=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                         | Example                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `finding_id`                                                                                                                                                                                                                                        | *float*                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                  | The ID of the finding to retest.                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                     |
| `include_dns_connected`                                                                                                                                                                                                                             | *Optional[bool]*                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                  | Include DNS-connected findings with the same vulnerability type in the retest. When enabled, the system will identify all findings with the same KB entry on assets connected via DNS A records (up to 10 findings total) and retest them together. | true                                                                                                                                                                                                                                                |
| `retries`                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                 |                                                                                                                                                                                                                                                     |

### Response

**[models.ClientFinding](../../models/clientfinding.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.Unauthorized         | 401                         | application/json            |
| models.ForbiddenResponse    | 403                         | application/json            |
| models.UnprocessableContent | 422                         | application/json            |
| models.APIError             | 4XX, 5XX                    | \*/\*                       |

## get_finding_notes

List all notes for a specific finding.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.findings.get_finding_notes(id=2829.09, page=1, page_size=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                             | *float*                                                                                                                                                          | :heavy_check_mark:                                                                                                                                               | The ID of the finding to list notes for.                                                                                                                         |                                                                                                                                                                  |
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

## create_finding_note

Create a new note for a specific finding.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.findings.create_finding_note(id=4650.48, note="Passed to the engineering team. Review on 01/07/2024", title="Initial Review - 01/01/2024")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The ID of the finding to create a note for.                         |                                                                     |
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

## create_finding_manual_ticket

Create a manual ticket reference for a specific finding.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.findings.create_finding_manual_ticket(id=3073.46, board_name="Acme Jira Board", issue_link="https://example.atlassian.net/browse/ABC-123")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The ID of the finding to create a manual ticket for.                |                                                                     |
| `board_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Name of the external board or ticketing system.                     | Acme Jira Board                                                     |
| `issue_link`                                                        | *str*                                                               | :heavy_check_mark:                                                  | URL of the manually created ticket.                                 | https://example.atlassian.net/browse/ABC-123                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ClientFindingManualTicketData](../../models/clientfindingmanualticketdata.md)**

### Errors

| Error Type                  | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| models.Unauthorized         | 401                         | application/json            |
| models.ForbiddenResponse    | 403                         | application/json            |
| models.NotFound             | 404                         | application/json            |
| models.UnprocessableContent | 422                         | application/json            |
| models.APIError             | 4XX, 5XX                    | \*/\*                       |

## update_finding_note

Update an existing note for a specific finding.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.findings.update_finding_note(id=4987.21, note_id=2947.79, note="Passed to the engineering team. Review on 01/07/2024", title="Initial Review - 01/01/2024")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The ID of the finding that contains the note.                       |                                                                     |
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

## delete_finding_note

Delete a specific note from a finding.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.findings.delete_finding_note(id=7951.65, note_id=9970.42)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The ID of the finding that contains the note.                       |
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

## get_custom_properties_finding

List the Custom Properties of a specific Finding.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.findings.get_custom_properties_finding(id=4698.1, page=1, page_size=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                             | *float*                                                                                                                                                          | :heavy_check_mark:                                                                                                                                               | The ID of the finding to list custom properties of.                                                                                                              |                                                                                                                                                                  |
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

## create_custom_property_finding

Create a Custom Property for a specific Finding.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.findings.create_custom_property_finding(id=1297.87, key="Severity", value={}, is_preset=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                              | *float*                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                | The ID of the finding to create a new custom property for.                                                                                                                                                                                        |                                                                                                                                                                                                                                                   |
| `key`                                                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                | The key of the custom property. Key provided must not be empty and must be unique for the model type. If is_preset is true, key must belong to one of watchTowr's preset custom properties. Accepted preset keys include: 'Criticality'.          | Severity                                                                                                                                                                                                                                          |
| `value`                                                                                                                                                                                                                                           | [models.Value](../../models/value.md)                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                | The value of the custom property. If existing custom property's preset is true, the value supplied must belong to one of the valid watchTowr preset values. Accepted preset values are 'Low', 'Medium', 'High', 'Unknown' for key: 'Criticality'. | Low                                                                                                                                                                                                                                               |
| `is_preset`                                                                                                                                                                                                                                       | *Optional[bool]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                | Defaults to false. If true, custom property is a watchTowr preset custom property.                                                                                                                                                                | false                                                                                                                                                                                                                                             |
| `retries`                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                               |                                                                                                                                                                                                                                                   |

### Response

**[models.ClientCustomProperty](../../models/clientcustomproperty.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.NotFound     | 404                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## update_custom_property_finding

Update a Custom Property for a specific Finding

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.findings.update_custom_property_finding(id=2139.97, custom_property_id=2380.63, key="Severity", value="Low")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                                              | Required                                                                                                                                                                                                                                          | Description                                                                                                                                                                                                                                       | Example                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                              | *float*                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                | The ID of the finding to update a custom property of.                                                                                                                                                                                             |                                                                                                                                                                                                                                                   |
| `custom_property_id`                                                                                                                                                                                                                              | *float*                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                | The ID of the custom property to update.                                                                                                                                                                                                          |                                                                                                                                                                                                                                                   |
| `key`                                                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                | The key of the custom property. Key provided must not be empty and must be unique for the model type. If is_preset is true, key must belong to one of watchTowr's preset custom properties. Accepted preset keys include: 'Criticality'.          | Severity                                                                                                                                                                                                                                          |
| `value`                                                                                                                                                                                                                                           | *str*                                                                                                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                                                                                                | The value of the custom property. If existing custom property's preset is true, the value supplied must belong to one of the valid watchTowr preset values. Accepted preset values are 'Low', 'Medium', 'High', 'Unknown' for key: 'Criticality'. | Low                                                                                                                                                                                                                                               |
| `retries`                                                                                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                                                                                               |                                                                                                                                                                                                                                                   |

### Response

**[models.ClientCustomProperty](../../models/clientcustomproperty.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.NotFound     | 404                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## delete_custom_property_finding

Delete a Custom Property for a specific Finding.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.findings.delete_custom_property_finding(id=3475.31, custom_property_id=7408.86)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The ID of the finding to delete a custom property of.               |
| `custom_property_id`                                                | *float*                                                             | :heavy_check_mark:                                                  | The ID of the custom property to delete.                            |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RemoveClientCustomPropertyResponseDto](../../models/removeclientcustompropertyresponsedto.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.NotFound     | 404                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |