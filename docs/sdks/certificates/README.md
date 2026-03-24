# Certificates
(*certificates*)

## Overview

### Available Operations

* [get_list_certificates](#get_list_certificates) - List Certificates
* [get_certificate_details](#get_certificate_details) - Get Certificate Details

## get_list_certificates

List all discovered TLS/SSL certificate assets, ordered by discovery date.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation
from watchtowr_complete_watchtowr_platform_api_documentation_python.utils import parse_datetime


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.certificates.get_list_certificates(page=1, page_size=10, created_from=parse_datetime("2022-02-22 22:00:00"), created_to=parse_datetime("2022-02-23 22:00:00"), updated_from=parse_datetime("2022-02-22 22:00:00"), updated_to=parse_datetime("2022-02-23 22:00:00"), not_after_from=parse_datetime("2022-02-22 22:00:00"), not_after_to=parse_datetime("2022-02-23 22:00:00"), subject_common_name_search="example.com", subject_alt_name_search="example.com", subject_organisation_search="example", asset_name_search="example.watchTowr.com", statuses="Expired,Expiring Within 30 Days,Valid", business_unit_ids="1,2,3")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      | Example                                                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page`                                                                                                                                                           | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The page number for paginated results. If the page field is not provided in the request, it defaults to 1, which corresponds to the first page of results.       | 1                                                                                                                                                                |
| `page_size`                                                                                                                                                      | *Optional[float]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                               | The number of items to be included on each page of paginated results. If the pageSize field is not specified, it defaults to 10. The maximum for pageSize is 30. | 10                                                                                                                                                               |
| `created_from`                                                                                                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                             | :heavy_minus_sign:                                                                                                                                               | Filter certificates created after a given date and time.                                                                                                         | 2022-02-22 22:00:00                                                                                                                                              |
| `created_to`                                                                                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                             | :heavy_minus_sign:                                                                                                                                               | Filter certificates created before a given date and time.                                                                                                        | 2022-02-23 22:00:00                                                                                                                                              |
| `updated_from`                                                                                                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                             | :heavy_minus_sign:                                                                                                                                               | Filter certificates updated after a given date and time.                                                                                                         | 2022-02-22 22:00:00                                                                                                                                              |
| `updated_to`                                                                                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                             | :heavy_minus_sign:                                                                                                                                               | Filter certificates updated before a given date and time.                                                                                                        | 2022-02-23 22:00:00                                                                                                                                              |
| `not_after_from`                                                                                                                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                             | :heavy_minus_sign:                                                                                                                                               | Filter certificates that do not expire after a given date and time.                                                                                              | 2022-02-22 22:00:00                                                                                                                                              |
| `not_after_to`                                                                                                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                             | :heavy_minus_sign:                                                                                                                                               | Filter certificates that do not expire before a given date and time.                                                                                             | 2022-02-23 22:00:00                                                                                                                                              |
| `subject_common_name_search`                                                                                                                                     | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Search certificates by Subject Common Name.                                                                                                                      | example.com                                                                                                                                                      |
| `subject_alt_name_search`                                                                                                                                        | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Search certificates by Subject Alt Name.                                                                                                                         | example.com                                                                                                                                                      |
| `subject_organisation_search`                                                                                                                                    | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Search by subject organization.                                                                                                                                  | example                                                                                                                                                          |
| `subject_countries`                                                                                                                                              | List[*str*]                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                               | Filter certificates by a list of comma separated subject countries that they're related to.                                                                      |                                                                                                                                                                  |
| `asset_name_search`                                                                                                                                              | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Search Certificates by the name of the associated asset.                                                                                                         | example.watchTowr.com                                                                                                                                            |
| `statuses`                                                                                                                                                       | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Filter certificates by a list of comma separated statuses that they're tagged with.                                                                              | Expired,Expiring Within 30 Days,Valid                                                                                                                            |
| `business_unit_ids`                                                                                                                                              | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Filter certificates by a list of comma separated business unit IDs they're related to.                                                                           | 1,2,3                                                                                                                                                            |
| `retries`                                                                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Configuration to override the default retry behavior of the client.                                                                                              |                                                                                                                                                                  |

### Response

**[models.PaginatedServiceInformationResponse](../../models/paginatedserviceinformationresponse.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.Unauthorized | 401                 | application/json    |
| models.APIError     | 4XX, 5XX            | \*/\*               |

## get_certificate_details

Get the details of a specific TLS/SSL certificate.

### Example Usage

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.certificates.get_certificate_details(id=6334.62)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *float*                                                             | :heavy_check_mark:                                                  | The asset ID of the certificate to retrieve.                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ClientServiceInformationResponseData](../../models/clientserviceinformationresponsedata.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| models.Unauthorized      | 401                      | application/json         |
| models.ForbiddenResponse | 403                      | application/json         |
| models.APIError          | 4XX, 5XX                 | \*/\*                    |