<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
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

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation
from watchtowr_complete_watchtowr_platform_api_documentation_python.utils import parse_datetime

async def main():

    async with CompleteWatchtowrPlatformAPIDocumentation(
        bearer="<YOUR_BEARER_TOKEN_HERE>",
    ) as complete_watchtowr_platform_api_documentation:

        res = await complete_watchtowr_platform_api_documentation.findings.get_list_findings_async(page=1, page_size=10, created_from=parse_datetime("2022-02-22 22:00:00"), created_to=parse_datetime("2022-02-23 22:00:00"), updated_from=parse_datetime("2022-02-22 22:00:00"), updated_to=parse_datetime("2022-02-23 22:00:00"), statuses="confirmed,unconfirmed,remediated,risk-accepted,closed,asset-no-longer-tracked", business_unit_ids="1,2,3", finding_title="Valid%20Credentials%20Discovered", severities=watchtowr_complete_watchtowr_platform_api_documentation_python.Severities.MEDIUM, asset_title="www.watchTowr.com", asset_types=watchtowr_complete_watchtowr_platform_api_documentation_python.AssetTypes.PORT, tags="CISA-KEV,Defacement,Credentials", only_validated_exploitable=False, only_unacknowledged=False, exploitation_risk_level=watchtowr_complete_watchtowr_platform_api_documentation_python.ExploitationRiskLevel.HIGH)

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->