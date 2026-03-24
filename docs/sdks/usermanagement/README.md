# UserManagement
(*user_management*)

## Overview

### Available Operations

* [list_users](#list_users) - List Users
* [get_user_details](#get_user_details) - Get User Details
* [invite_users](#invite_users) - Invite Users
* [update_user](#update_user) - Update User
* [delete_user](#delete_user) - Delete User

## list_users

Get a paginated list of users with filtering. Administrator role required.

### Example Usage

```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.user_management.list_users(page=1, page_size=10, name="John Doe", title="Security Manager", status=[
        watchtowr_complete_watchtowr_platform_api_documentation_python.QueryParamStatus.ACTIVE,
    ], role_ids=[
        1,
        2,
    ], created_from="2023-01-01T00:00:00Z", created_to="2023-12-31T23:59:59Z")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page`                                                                                                                                                           | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.       | 1                                                                                                                                                                |
| `page_size`                                                                                                                                                      | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | 10                                                                                                                                                               |
| `name`                                                                                                                                                           | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Search by user name                                                                                                                                              | John Doe                                                                                                                                                         |
| `title`                                                                                                                                                          | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Search by user title                                                                                                                                             | Security Manager                                                                                                                                                 |
| `status`                                                                                                                                                         | List[[models.QueryParamStatus](../../models/queryparamstatus.md)]                                                                                                | :heavy_minus_sign:                                                                                                                                               | Filter by user status                                                                                                                                            | [<br/>"Active"<br/>]                                                                                                                                             |
| `role_ids`                                                                                                                                                       | List[*float*]                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                               | Filter by role IDs                                                                                                                                               | [<br/>1,<br/>2<br/>]                                                                                                                                             |
| `created_from`                                                                                                                                                   | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Filter by creation date start                                                                                                                                    | 2023-01-01T00:00:00Z                                                                                                                                             |
| `created_to`                                                                                                                                                     | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Filter by creation date end                                                                                                                                      | 2023-12-31T23:59:59Z                                                                                                                                             |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |                                                                                                                                                                  |

### Response

**[models.PaginatedUsers](../../models/paginatedusers.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_user_details

Get detailed information about a specific user. Administrator role required.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.user_management.get_user_details(id=9150.36)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UserDetailData](../../models/userdetaildata.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## invite_users

Invite new users to the platform. Sends invitation emails to the specified email addresses. Administrator role required.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.user_management.invite_users(user_agent="<value>", users=[])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `user_agent`                                                            | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `users`                                                                 | List[[models.InviteClientUserDto](../../models/inviteclientuserdto.md)] | :heavy_check_mark:                                                      | List of users to invite                                                 |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.InviteUserResponseData](../../models/inviteuserresponsedata.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.BadRequestResponse | 400                       | application/json          |
| models.Unauthorized       | 401                       | application/json          |
| models.ForbiddenResponse  | 403                       | application/json          |
| models.APIError           | 4XX, 5XX                  | \*/\*                     |

## update_user

Update user details including locked status, role, and business unit assignments. Administrator role required.

### Example Usage

```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.user_management.update_user(id=599.27, user_agent="<value>", role_type=watchtowr_complete_watchtowr_platform_api_documentation_python.UpdateClientUserBodyDtoRoleType.USER, business_unit_ids=[
        1,
        2,
    ], locked=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               | Example                                                                                   |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `id`                                                                                      | *float*                                                                                   | :heavy_check_mark:                                                                        | N/A                                                                                       |                                                                                           |
| `user_agent`                                                                              | *str*                                                                                     | :heavy_check_mark:                                                                        | N/A                                                                                       |                                                                                           |
| `role_type`                                                                               | [models.UpdateClientUserBodyDtoRoleType](../../models/updateclientuserbodydtoroletype.md) | :heavy_check_mark:                                                                        | Role type to assign to the user                                                           | USER                                                                                      |
| `business_unit_ids`                                                                       | List[*float*]                                                                             | :heavy_check_mark:                                                                        | Business Unit IDs to assign (required for BU_USER roles)                                  | [<br/>1,<br/>2<br/>]                                                                      |
| `locked`                                                                                  | *bool*                                                                                    | :heavy_check_mark:                                                                        | Whether the user is locked (prevented from logging in)                                    | false                                                                                     |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |                                                                                           |

### Response

**[models.UpdateUserResponse](../../models/updateuserresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| models.BadRequestResponse | 400                       | application/json          |
| models.Unauthorized       | 401                       | application/json          |
| models.ForbiddenResponse  | 403                       | application/json          |
| models.NotFound           | 404                       | application/json          |
| models.APIError           | 4XX, 5XX                  | \*/\*                     |

## delete_user

Delete a user from the platform. This action is irreversible. Administrator role required.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.user_management.delete_user(id=3548.59)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteUserResponseData](../../models/deleteuserresponsedata.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.NotFound          | 404                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |