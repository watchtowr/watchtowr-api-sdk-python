# KillSwitch
(*kill_switch*)

## Overview

### Available Operations

* [get_kill_switch_status](#get_kill_switch_status) - Get Kill Switch Status
* [update_kill_switch](#update_kill_switch) - Update Kill Switch

## get_kill_switch_status

Get the current status of the kill switch and whether client control is allowed.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.kill_switch.get_kill_switch_status()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.KillSwitchStatusData](../../models/killswitchstatusdata.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.Unauthorized             | 401                             | application/json                |
| models.KillSwitchForbiddenError | 403                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |

## update_kill_switch

Enable or disable the kill switch. Administrator or User role required.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.kill_switch.update_kill_switch(value=True, reason="Emergency response to security incident", request_support=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             | Example                                                                 |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `value`                                                                 | *bool*                                                                  | :heavy_check_mark:                                                      | Kill switch value (true to enable, false to disable)                    | true                                                                    |
| `reason`                                                                | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Reason for enabling the kill switch (required when enabling)            | Emergency response to security incident                                 |
| `request_support`                                                       | *Optional[bool]*                                                        | :heavy_minus_sign:                                                      | Whether to request support from watchTowr (optional, defaults to false) | false                                                                   |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |                                                                         |

### Response

**[models.UpdateKillSwitchData](../../models/updatekillswitchdata.md)**

### Errors

| Error Type                      | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| models.KillSwitchDisabledError  | 400                             | application/json                |
| models.Unauthorized             | 401                             | application/json                |
| models.KillSwitchForbiddenError | 403                             | application/json                |
| models.APIError                 | 4XX, 5XX                        | \*/\*                           |