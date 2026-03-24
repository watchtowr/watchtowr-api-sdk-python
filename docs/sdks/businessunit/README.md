# BusinessUnit
(*business_unit*)

## Overview

### Available Operations

* [get_list_business_unit](#get_list_business_unit) - List Business Units
* [create_business_unit](#create_business_unit) - Create Business Unit
* [update_business_unit](#update_business_unit) - Update Business Unit
* [delete_business_unit](#delete_business_unit) - Delete Business Unit
* [get_business_unit_details](#get_business_unit_details) - Get Business Unit Details
* [create_business_unit_rule](#create_business_unit_rule) - Create Business Unit Rule
* [delete_business_unit_rule](#delete_business_unit_rule) - Delete Business Unit Rule

## get_list_business_unit

List all business units available to the current user.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation
from watchtowr_complete_watchtowr_platform_api_documentation_python.utils import parse_datetime


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.business_unit.get_list_business_unit(page=1, page_size=10, created_from=parse_datetime("2022-02-22 22:00:00"), created_to=parse_datetime("2022-02-23 22:00:00"), updated_from=parse_datetime("2022-02-22 22:00:00"), updated_to=parse_datetime("2022-02-23 22:00:00"), search="Singapore Business Unit")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page`                                                                                                                                                           | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.       | 1                                                                                                                                                                |
| `page_size`                                                                                                                                                      | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | 10                                                                                                                                                               |
| `created_from`                                                                                                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                             | :heavy_minus_sign:                                                                                                                                               | Filter business units created after a given date and time.                                                                                                       | 2022-02-22 22:00:00                                                                                                                                              |
| `created_to`                                                                                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                             | :heavy_minus_sign:                                                                                                                                               | Filter business units created before a given date and time.                                                                                                      | 2022-02-23 22:00:00                                                                                                                                              |
| `updated_from`                                                                                                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                             | :heavy_minus_sign:                                                                                                                                               | Filter business units updated after a given date and time.                                                                                                       | 2022-02-22 22:00:00                                                                                                                                              |
| `updated_to`                                                                                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                             | :heavy_minus_sign:                                                                                                                                               | Filter business units updated before a given date and time.                                                                                                      | 2022-02-23 22:00:00                                                                                                                                              |
| `search`                                                                                                                                                         | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Search business units by name.                                                                                                                                   | Singapore Business Unit                                                                                                                                          |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |                                                                                                                                                                  |

### Response

**[models.PaginatedBusinessUnit](../../models/paginatedbusinessunit.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## create_business_unit

Create a new business unit with name, description, type, and optional user assignments.

### Example Usage

```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.business_unit.create_business_unit(name="Singapore Business Unit", type_=watchtowr_complete_watchtowr_platform_api_documentation_python.CreateClientBusinessUnitDtoType.DEPARTMENT, description="Singapore based assets", parent_id=1, user_ids=[
        1,
        2,
        3,
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               | Example                                                                                   |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `name`                                                                                    | *str*                                                                                     | :heavy_check_mark:                                                                        | Business unit name                                                                        | Singapore Business Unit                                                                   |
| `type`                                                                                    | [models.CreateClientBusinessUnitDtoType](../../models/createclientbusinessunitdtotype.md) | :heavy_check_mark:                                                                        | Business unit type                                                                        | DEPARTMENT                                                                                |
| `description`                                                                             | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | Business unit description                                                                 | Singapore based assets                                                                    |
| `parent_id`                                                                               | *Optional[float]*                                                                         | :heavy_minus_sign:                                                                        | Parent business unit ID                                                                   | 1                                                                                         |
| `user_ids`                                                                                | List[*float*]                                                                             | :heavy_minus_sign:                                                                        | Array of user IDs to assign to this business unit                                         | [<br/>1,<br/>2,<br/>3<br/>]                                                               |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |                                                                                           |

### Response

**[models.ClientBusinessUnitData](../../models/clientbusinessunitdata.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## update_business_unit

Update an existing business unit with name, description, type, parent, and user assignments.

### Example Usage

```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.business_unit.update_business_unit(id=5950.44, name="Updated Business Unit Name", type_=watchtowr_complete_watchtowr_platform_api_documentation_python.UpdateClientBusinessUnitDtoType.DEPARTMENT, description="Updated description", parent_id=1, user_ids=[
        1,
        2,
        3,
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               | Example                                                                                   |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `id`                                                                                      | *float*                                                                                   | :heavy_check_mark:                                                                        | The ID of the business unit to update.                                                    |                                                                                           |
| `name`                                                                                    | *str*                                                                                     | :heavy_check_mark:                                                                        | Business unit name                                                                        | Updated Business Unit Name                                                                |
| `type`                                                                                    | [models.UpdateClientBusinessUnitDtoType](../../models/updateclientbusinessunitdtotype.md) | :heavy_check_mark:                                                                        | Business unit type                                                                        | DEPARTMENT                                                                                |
| `description`                                                                             | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | Business unit description                                                                 | Updated description                                                                       |
| `parent_id`                                                                               | *OptionalNullable[float]*                                                                 | :heavy_minus_sign:                                                                        | Parent business unit ID. Set to null to remove parent relationship.                       | 1                                                                                         |
| `user_ids`                                                                                | List[*float*]                                                                             | :heavy_minus_sign:                                                                        | Array of user IDs to assign to this business unit                                         | [<br/>1,<br/>2,<br/>3<br/>]                                                               |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |                                                                                           |

### Response

**[models.ClientBusinessUnitData](../../models/clientbusinessunitdata.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## delete_business_unit

Delete an existing business unit.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.business_unit.delete_business_unit(id=314.53)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The ID of the business unit to delete.                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteClientBusinessUnitResponseDto](../../models/deleteclientbusinessunitresponsedto.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## get_business_unit_details

Get the details of a specific business unit including paginated rules.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.business_unit.get_business_unit_details(id=1182.08, rule_page=1, rule_page_size=10)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `rule_page`                                                         | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | Page number for rules pagination                                    | 1                                                                   |
| `rule_page_size`                                                    | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | Page size for rules pagination                                      | 10                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ClientBusinessUnitDetailWithRulesData](../../models/clientbusinessunitdetailwithrulesdata.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## create_business_unit_rule

Create a new rule for a specific business unit.

### Example Usage

```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.business_unit.create_business_unit_rule(id=6666.97, name="Singapore Assets Rule", type_=watchtowr_complete_watchtowr_platform_api_documentation_python.CreateClientBusinessUnitRuleDtoType.KEYWORD, keyword_matcher="example.com", keyword_rule_type=watchtowr_complete_watchtowr_platform_api_documentation_python.KeywordRuleType.HOSTNAME, country_code="SG", integration_type=watchtowr_complete_watchtowr_platform_api_documentation_python.IntegrationType.AWS, integration_id=1, cascade_subdomain=True, cascade_ip=True, include_all_integrations=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                    | Example                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`                                                                                                                                                                                                                                                                           | *float*                                                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                             | The ID of the business unit to create a rule for.                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                |
| `name`                                                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                             | Rule name                                                                                                                                                                                                                                                                      | Singapore Assets Rule                                                                                                                                                                                                                                                          |
| `type`                                                                                                                                                                                                                                                                         | [models.CreateClientBusinessUnitRuleDtoType](../../models/createclientbusinessunitruledtotype.md)                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                                                                                             | Rule type                                                                                                                                                                                                                                                                      | keyword                                                                                                                                                                                                                                                                        |
| `keyword_matcher`                                                                                                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                             | Keyword for matching assets (required when type is keyword). Supports wildcard patterns: %.sg, %abc%, %abc.com, abc.com. Wildcards can be defined using %.                                                                                                                     | example.com                                                                                                                                                                                                                                                                    |
| `keyword_rule_type`                                                                                                                                                                                                                                                            | [Optional[models.KeywordRuleType]](../../models/keywordruletype.md)                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                             | Keyword rule type (optional, defaults to HOSTNAME when keyword_matcher is provided). HOSTNAME: matches domain/subdomain names. CNAME: matches CNAME DNS record values. TLS_SSL: matches TLS/SSL certificate subject names.                                                     | HOSTNAME                                                                                                                                                                                                                                                                       |
| `country_code`                                                                                                                                                                                                                                                                 | *Optional[str]*                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                             | Geographical location 2-letter country code (ISO 3166-1 alpha-2) for matching IPs (required when type is country). Examples: SG, US, GB, AU                                                                                                                                    | SG                                                                                                                                                                                                                                                                             |
| `integration_type`                                                                                                                                                                                                                                                             | [Optional[models.IntegrationType]](../../models/integrationtype.md)                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                             | Integration type for matching cloud assets (required when type is integration). Valid values: aws, azure, googlecloud, cloudflare, alibabacloud, prismacloud, prismacloudapigee, huaweicloud, tencentcloud, wiz, servicenowcmdb, akamaiedge, armiscentrix, qualysvmdr, tenable | aws                                                                                                                                                                                                                                                                            |
| `integration_id`                                                                                                                                                                                                                                                               | *Optional[float]*                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                             | Integration ID for matching cloud assets (required when type is integration)                                                                                                                                                                                                   | 1                                                                                                                                                                                                                                                                              |
| `cascade_subdomain`                                                                                                                                                                                                                                                            | *Optional[bool]*                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                             | Whether to cascade rule to subdomains                                                                                                                                                                                                                                          | true                                                                                                                                                                                                                                                                           |
| `cascade_ip`                                                                                                                                                                                                                                                                   | *Optional[bool]*                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                             | Whether to cascade rule to IPs                                                                                                                                                                                                                                                 | true                                                                                                                                                                                                                                                                           |
| `include_all_integrations`                                                                                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                             | Whether to include all integrations                                                                                                                                                                                                                                            | false                                                                                                                                                                                                                                                                          |
| `retries`                                                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                |

### Response

**[models.ClientBusinessUnitRuleData](../../models/clientbusinessunitruledata.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |

## delete_business_unit_rule

Delete an existing rule for a specific business unit.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.business_unit.delete_business_unit_rule(id=4149.12, rule_id=2460.86)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The ID of the business unit.                                        |
| `rule_id`                                                           | *float*                                                             | :heavy_check_mark:                                                  | The ID of the rule to delete.                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteClientBusinessUnitRuleResponseDto](../../models/deleteclientbusinessunitruleresponsedto.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |