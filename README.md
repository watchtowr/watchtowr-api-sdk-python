# complete-watchtowr-platform-api-documentation-python

Developer-friendly, idiomatic Python SDK for the *complete-watchtowr-platform-api-documentation-python* API.

<div align="left">
    <a href="https://www.scalar.com/?utm_source=complete-watchtowr-platform-api-documentation-python&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20scalar+speakeasy-212015?style=for-the-badge&logo=scalar&labelColor=252525" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>

<br />

## Summary

Complete watchTowr Platform API Documentation: The watchTowr Client API combining all watchTowr Platform APIs into a single comprehensive reference, including:
* Automated Red Teaming API
* Adversary Sight API
* Intelligence API
* Platform API
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [watchtowr-complete-watchtowr-platform-api-documentation-python](#watchtowr-complete-watchtowr-platform-api-documentation-python)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install watchtowr-complete-watchtowr-platform-api-documentation-python
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add watchtowr-complete-watchtowr-platform-api-documentation-python
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from watchtowr-complete-watchtowr-platform-api-documentation-python python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "watchtowr-complete-watchtowr-platform-api-documentation-python",
# ]
# ///

from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation

sdk = CompleteWatchtowrPlatformAPIDocumentation(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

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

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name     | Type | Scheme      |
| -------- | ---- | ----------- |
| `bearer` | http | HTTP Bearer |

To authenticate with the API the `bearer` parameter must be set when initializing the SDK client instance. For example:
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
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [activity_log](docs/sdks/activitylog/README.md)

* [get_list_activity_logs](docs/sdks/activitylog/README.md#get_list_activity_logs) - List Activity Logs

### [add_asset](docs/sdks/addasset/README.md)

* [submit_asset](docs/sdks/addasset/README.md#submit_asset) - Submit Seed Data
* [list_submitted_assets](docs/sdks/addasset/README.md#list_submitted_assets) - List Submitted Assets

### [api_documentation](docs/sdks/apidocumentation/README.md)

* [get_list_asset_api_documentation](docs/sdks/apidocumentation/README.md#get_list_asset_api_documentation) - List API Documentation
* [get_asset_api_documentation_details](docs/sdks/apidocumentation/README.md#get_asset_api_documentation_details) - Get API Documentation Details
* [get_asset_api_documentation_changelog](docs/sdks/apidocumentation/README.md#get_asset_api_documentation_changelog) - Get API Documentation Changelog
* [update_asset_api_documentation_status](docs/sdks/apidocumentation/README.md#update_asset_api_documentation_status) - Update API Documentation Status
* [get_asset_api_documentation_notes](docs/sdks/apidocumentation/README.md#get_asset_api_documentation_notes) - List API Documentation Notes
* [add_asset_api_documentation_note](docs/sdks/apidocumentation/README.md#add_asset_api_documentation_note) - Create Note
* [update_asset_api_documentation_note](docs/sdks/apidocumentation/README.md#update_asset_api_documentation_note) - Update Note
* [delete_asset_api_documentation_note](docs/sdks/apidocumentation/README.md#delete_asset_api_documentation_note) - Delete Note
* [get_custom_properties_api_documentation](docs/sdks/apidocumentation/README.md#get_custom_properties_api_documentation) - List Custom Properties
* [create_custom_property_api_documentation](docs/sdks/apidocumentation/README.md#create_custom_property_api_documentation) - Create Custom Property
* [update_custom_property_api_documentation](docs/sdks/apidocumentation/README.md#update_custom_property_api_documentation) - Update Custom Property
* [delete_custom_property_api_documentation](docs/sdks/apidocumentation/README.md#delete_custom_property_api_documentation) - Delete Custom Property
* [assign_api_documentation_to_business_units](docs/sdks/apidocumentation/README.md#assign_api_documentation_to_business_units) - Assign API Documentation to Business Units
* [unassign_api_documentation_from_business_units](docs/sdks/apidocumentation/README.md#unassign_api_documentation_from_business_units) - Unassign API Documentation from Business Units
* [set_criticality_api_documentation](docs/sdks/apidocumentation/README.md#set_criticality_api_documentation) - Set Criticality

### [business_unit](docs/sdks/businessunit/README.md)

* [get_list_business_unit](docs/sdks/businessunit/README.md#get_list_business_unit) - List Business Units
* [create_business_unit](docs/sdks/businessunit/README.md#create_business_unit) - Create Business Unit
* [update_business_unit](docs/sdks/businessunit/README.md#update_business_unit) - Update Business Unit
* [delete_business_unit](docs/sdks/businessunit/README.md#delete_business_unit) - Delete Business Unit
* [get_business_unit_details](docs/sdks/businessunit/README.md#get_business_unit_details) - Get Business Unit Details
* [create_business_unit_rule](docs/sdks/businessunit/README.md#create_business_unit_rule) - Create Business Unit Rule
* [delete_business_unit_rule](docs/sdks/businessunit/README.md#delete_business_unit_rule) - Delete Business Unit Rule

### [certificates](docs/sdks/certificates/README.md)

* [get_list_certificates](docs/sdks/certificates/README.md#get_list_certificates) - List Certificates
* [get_certificate_details](docs/sdks/certificates/README.md#get_certificate_details) - Get Certificate Details

### [cloud_integration_assets](docs/sdks/cloudintegrationassets/README.md)

* [get_list_asset_cloud_asset](docs/sdks/cloudintegrationassets/README.md#get_list_asset_cloud_asset) - List Cloud Assets
* [get_asset_cloud_asset_details](docs/sdks/cloudintegrationassets/README.md#get_asset_cloud_asset_details) - Get Cloud Asset Details
* [get_asset_cloud_asset_changelog](docs/sdks/cloudintegrationassets/README.md#get_asset_cloud_asset_changelog) - Get Cloud Asset Changelog
* [update_asset_cloud_asset_status](docs/sdks/cloudintegrationassets/README.md#update_asset_cloud_asset_status) - Update Cloud Asset Status
* [get_asset_cloud_asset_notes](docs/sdks/cloudintegrationassets/README.md#get_asset_cloud_asset_notes) - List Notes
* [add_asset_cloud_asset_note](docs/sdks/cloudintegrationassets/README.md#add_asset_cloud_asset_note) - Create Note
* [update_asset_cloud_asset_note](docs/sdks/cloudintegrationassets/README.md#update_asset_cloud_asset_note) - Update Note
* [delete_asset_cloud_asset_note](docs/sdks/cloudintegrationassets/README.md#delete_asset_cloud_asset_note) - Delete Note
* [get_custom_properties_cloud_asset](docs/sdks/cloudintegrationassets/README.md#get_custom_properties_cloud_asset) - List Custom Properties
* [create_custom_property_cloud_asset](docs/sdks/cloudintegrationassets/README.md#create_custom_property_cloud_asset) - Create Custom Property
* [update_custom_property_cloud_asset](docs/sdks/cloudintegrationassets/README.md#update_custom_property_cloud_asset) - Update Custom Property
* [delete_custom_property_cloud_asset](docs/sdks/cloudintegrationassets/README.md#delete_custom_property_cloud_asset) - Delete Custom Property
* [assign_cloud_asset_to_business_units](docs/sdks/cloudintegrationassets/README.md#assign_cloud_asset_to_business_units) - Assign Cloud Integration Asset to Business Units
* [unassign_cloud_asset_from_business_units](docs/sdks/cloudintegrationassets/README.md#unassign_cloud_asset_from_business_units) - Unassign Cloud Integration Asset from Business Units
* [set_criticality_cloud_asset](docs/sdks/cloudintegrationassets/README.md#set_criticality_cloud_asset) - Set Criticality

### [cloud_storage](docs/sdks/cloudstorage/README.md)

* [get_list_asset_cloud_storages](docs/sdks/cloudstorage/README.md#get_list_asset_cloud_storages) - List Cloud Storage
* [get_asset_cloud_storage_details](docs/sdks/cloudstorage/README.md#get_asset_cloud_storage_details) - Get Cloud Storage
* [get_asset_cloud_storage_changelog](docs/sdks/cloudstorage/README.md#get_asset_cloud_storage_changelog) - Get Cloud Storage Changelog
* [update_asset_cloud_storage_status](docs/sdks/cloudstorage/README.md#update_asset_cloud_storage_status) - Update Status
* [get_asset_cloud_storage_notes](docs/sdks/cloudstorage/README.md#get_asset_cloud_storage_notes) - List Notes
* [add_asset_cloud_storage_note](docs/sdks/cloudstorage/README.md#add_asset_cloud_storage_note) - Create Note
* [update_asset_cloud_storage_note](docs/sdks/cloudstorage/README.md#update_asset_cloud_storage_note) - Update Note
* [delete_asset_cloud_storage_note](docs/sdks/cloudstorage/README.md#delete_asset_cloud_storage_note) - Delete Note
* [get_custom_properties_cloud_storage](docs/sdks/cloudstorage/README.md#get_custom_properties_cloud_storage) - List Custom Properties
* [create_custom_property_cloud_storage](docs/sdks/cloudstorage/README.md#create_custom_property_cloud_storage) - Create Custom Property
* [update_custom_property_cloud_storage](docs/sdks/cloudstorage/README.md#update_custom_property_cloud_storage) - Update Custom Property
* [delete_custom_property_cloud_storage](docs/sdks/cloudstorage/README.md#delete_custom_property_cloud_storage) - Delete Custom Property
* [assign_cloud_storage_to_business_units](docs/sdks/cloudstorage/README.md#assign_cloud_storage_to_business_units) - Assign Cloud Storage to Business Units
* [unassign_cloud_storage_from_business_units](docs/sdks/cloudstorage/README.md#unassign_cloud_storage_from_business_units) - Unassign Cloud Storage from Business Units
* [set_criticality_cloud_storage](docs/sdks/cloudstorage/README.md#set_criticality_cloud_storage) - Set Criticality


### [containers](docs/sdks/containers/README.md)

* [get_list_asset_container](docs/sdks/containers/README.md#get_list_asset_container) - List Containers
* [get_asset_container_details](docs/sdks/containers/README.md#get_asset_container_details) - Get Container
* [get_asset_container_changelog](docs/sdks/containers/README.md#get_asset_container_changelog) - Get Container Changelog
* [update_asset_container_status](docs/sdks/containers/README.md#update_asset_container_status) - Update Status
* [get_asset_container_notes](docs/sdks/containers/README.md#get_asset_container_notes) - List Notes
* [create_note_container](docs/sdks/containers/README.md#create_note_container) - Create Note
* [update_note_container](docs/sdks/containers/README.md#update_note_container) - Update Note
* [delete_note_container](docs/sdks/containers/README.md#delete_note_container) - Delete Note
* [get_custom_properties_container](docs/sdks/containers/README.md#get_custom_properties_container) - List Custom Properties
* [create_custom_property_container](docs/sdks/containers/README.md#create_custom_property_container) - Create Custom Property
* [update_custom_property_container](docs/sdks/containers/README.md#update_custom_property_container) - Update Custom Property
* [delete_custom_property_container](docs/sdks/containers/README.md#delete_custom_property_container) - Delete Custom Property
* [assign_container_to_business_units](docs/sdks/containers/README.md#assign_container_to_business_units) - Assign Container to Business Units
* [unassign_container_from_business_units](docs/sdks/containers/README.md#unassign_container_from_business_units) - Unassign Container from Business Units
* [set_criticality_container](docs/sdks/containers/README.md#set_criticality_container) - Set Criticality

### [dns_record_analysis](docs/sdks/dnsrecordanalysis/README.md)

* [get_list_dns_records](docs/sdks/dnsrecordanalysis/README.md#get_list_dns_records) - List DNS Records

### [domains](docs/sdks/domains/README.md)

* [get_list_asset_domains](docs/sdks/domains/README.md#get_list_asset_domains) - List Domains
* [get_asset_domain_details](docs/sdks/domains/README.md#get_asset_domain_details) - Get Domain Details
* [get_asset_domain_changelog](docs/sdks/domains/README.md#get_asset_domain_changelog) - Get Domain Changelog
* [update_asset_domain_status](docs/sdks/domains/README.md#update_asset_domain_status) - Update Status
* [get_asset_domain_notes](docs/sdks/domains/README.md#get_asset_domain_notes) - List Notes
* [create_asset_domain_note](docs/sdks/domains/README.md#create_asset_domain_note) - Create Note
* [update_asset_domain_note](docs/sdks/domains/README.md#update_asset_domain_note) - Update Note
* [delete_asset_domain_note](docs/sdks/domains/README.md#delete_asset_domain_note) - Delete Note
* [get_asset_domain_dns_records](docs/sdks/domains/README.md#get_asset_domain_dns_records) - List DNS Records
* [get_custom_properties_domain](docs/sdks/domains/README.md#get_custom_properties_domain) - List Custom Properties
* [create_custom_property_domain](docs/sdks/domains/README.md#create_custom_property_domain) - Create Custom Property
* [update_custom_property_domain](docs/sdks/domains/README.md#update_custom_property_domain) - Update Custom Property
* [delete_custom_property_domain](docs/sdks/domains/README.md#delete_custom_property_domain) - Delete Custom Property
* [assign_domain_to_business_units](docs/sdks/domains/README.md#assign_domain_to_business_units) - Assign Domain to Business Units
* [unassign_domain_from_business_units](docs/sdks/domains/README.md#unassign_domain_from_business_units) - Unassign Domain from Business Units
* [get_asset_domain_engine_settings](docs/sdks/domains/README.md#get_asset_domain_engine_settings) - Get Domain Engine Settings
* [update_asset_domain_engine_settings](docs/sdks/domains/README.md#update_asset_domain_engine_settings) - Update Domain Engine Settings
* [set_criticality_domain](docs/sdks/domains/README.md#set_criticality_domain) - Set Criticality

### [finding_retest_history](docs/sdks/findingretesthistory/README.md)

* [get_list_finding_retest_history](docs/sdks/findingretesthistory/README.md#get_list_finding_retest_history) - List Finding Retest History

### [findings](docs/sdks/findings/README.md)

* [get_list_findings](docs/sdks/findings/README.md#get_list_findings) - List Findings
* [get_finding_details](docs/sdks/findings/README.md#get_finding_details) - Get Finding Details
* [export_pdf_for_finding](docs/sdks/findings/README.md#export_pdf_for_finding) - Export Finding PDF
* [get_available_finding_statuses](docs/sdks/findings/README.md#get_available_finding_statuses) - List Finding Statuses
* [update_finding_status](docs/sdks/findings/README.md#update_finding_status) - Update Finding Status
* [update_finding_state](docs/sdks/findings/README.md#update_finding_state) - Update Finding State
* [start_specific_finding_retest](docs/sdks/findings/README.md#start_specific_finding_retest) - Retest Finding
* [get_finding_notes](docs/sdks/findings/README.md#get_finding_notes) - List Finding Notes
* [create_finding_note](docs/sdks/findings/README.md#create_finding_note) - Create Finding Note
* [create_finding_manual_ticket](docs/sdks/findings/README.md#create_finding_manual_ticket) - Create Finding Manual Ticket
* [update_finding_note](docs/sdks/findings/README.md#update_finding_note) - Update Finding Note
* [delete_finding_note](docs/sdks/findings/README.md#delete_finding_note) - Delete Finding Note
* [get_custom_properties_finding](docs/sdks/findings/README.md#get_custom_properties_finding) - List Custom Properties
* [create_custom_property_finding](docs/sdks/findings/README.md#create_custom_property_finding) - Create Custom Property
* [update_custom_property_finding](docs/sdks/findings/README.md#update_custom_property_finding) - Update Custom Property
* [delete_custom_property_finding](docs/sdks/findings/README.md#delete_custom_property_finding) - Delete Custom Property

### [hunts](docs/sdks/hunts/README.md)

* [get_client_hunts](docs/sdks/hunts/README.md#get_client_hunts) - List Hunts
* [show_the_detail_hunt](docs/sdks/hunts/README.md#show_the_detail_hunt) - Get Hunt Details
* [get_list_finding_by_hunt](docs/sdks/hunts/README.md#get_list_finding_by_hunt) - List Hunt Findings
* [get_list_asset_by_hunt](docs/sdks/hunts/README.md#get_list_asset_by_hunt) - List Assets

### [ip_addresses](docs/sdks/ipaddresses/README.md)

* [get_list_asset_ips](docs/sdks/ipaddresses/README.md#get_list_asset_ips) - List IP Addresses
* [get_asset_ip_details](docs/sdks/ipaddresses/README.md#get_asset_ip_details) - Get IP Address Details
* [get_asset_ip_changelog](docs/sdks/ipaddresses/README.md#get_asset_ip_changelog) - Get IP Address Changelog
* [get_asset_ip_ports](docs/sdks/ipaddresses/README.md#get_asset_ip_ports) - List Ports
* [get_asset_ip_port_details](docs/sdks/ipaddresses/README.md#get_asset_ip_port_details) - Get Port
* [update_asset_ip_status](docs/sdks/ipaddresses/README.md#update_asset_ip_status) - Update Status
* [get_asset_ip_notes](docs/sdks/ipaddresses/README.md#get_asset_ip_notes) - List Notes
* [create_asset_ip_note](docs/sdks/ipaddresses/README.md#create_asset_ip_note) - Create Note
* [update_asset_ip_note](docs/sdks/ipaddresses/README.md#update_asset_ip_note) - Update Note
* [delete_asset_ip_note](docs/sdks/ipaddresses/README.md#delete_asset_ip_note) - Delete Note
* [get_asset_ip_dns_records](docs/sdks/ipaddresses/README.md#get_asset_ip_dns_records) - List DNS Records
* [get_custom_properties_ip](docs/sdks/ipaddresses/README.md#get_custom_properties_ip) - List Custom Properties
* [create_custom_property_ip](docs/sdks/ipaddresses/README.md#create_custom_property_ip) - Create Custom Property
* [update_custom_property_ip](docs/sdks/ipaddresses/README.md#update_custom_property_ip) - Update Custom Property
* [delete_custom_property_ip](docs/sdks/ipaddresses/README.md#delete_custom_property_ip) - Delete Custom Property
* [assign_ip_to_business_units](docs/sdks/ipaddresses/README.md#assign_ip_to_business_units) - Assign IP to Business Units
* [unassign_ip_from_business_units](docs/sdks/ipaddresses/README.md#unassign_ip_from_business_units) - Unassign IP from Business Units
* [get_asset_ip_engine_settings](docs/sdks/ipaddresses/README.md#get_asset_ip_engine_settings) - Get IP Engine Settings
* [update_asset_ip_engine_settings](docs/sdks/ipaddresses/README.md#update_asset_ip_engine_settings) - Update IP Engine Settings
* [set_criticality_ip](docs/sdks/ipaddresses/README.md#set_criticality_ip) - Set Criticality

### [ip_ranges](docs/sdks/ipranges/README.md)

* [get_list_asset_ipranges](docs/sdks/ipranges/README.md#get_list_asset_ipranges) - List IP Ranges
* [get_asset_iprange_details](docs/sdks/ipranges/README.md#get_asset_iprange_details) - Get IP Range
* [get_asset_iprange_changelog](docs/sdks/ipranges/README.md#get_asset_iprange_changelog) - Get IP Range Changelog
* [update_asset_ip_range_status](docs/sdks/ipranges/README.md#update_asset_ip_range_status) - Update Status
* [get_asset_ip_range_notes](docs/sdks/ipranges/README.md#get_asset_ip_range_notes) - List Notes
* [create_note_ip_range](docs/sdks/ipranges/README.md#create_note_ip_range) - Create Note
* [update_note_ip_range](docs/sdks/ipranges/README.md#update_note_ip_range) - Update Note
* [delete_note_ip_range](docs/sdks/ipranges/README.md#delete_note_ip_range) - Delete Note
* [get_custom_properties_ip_range](docs/sdks/ipranges/README.md#get_custom_properties_ip_range) - List Custom Properties
* [create_custom_property_ip_range](docs/sdks/ipranges/README.md#create_custom_property_ip_range) - Create Custom Property
* [update_custom_property_ip_range](docs/sdks/ipranges/README.md#update_custom_property_ip_range) - Update Custom Property
* [delete_custom_property_ip_range](docs/sdks/ipranges/README.md#delete_custom_property_ip_range) - Delete Custom Property
* [assign_ip_range_to_business_units](docs/sdks/ipranges/README.md#assign_ip_range_to_business_units) - Assign IP Range to Business Units
* [unassign_ip_range_from_business_units](docs/sdks/ipranges/README.md#unassign_ip_range_from_business_units) - Unassign IP Range from Business Units
* [set_criticality_ip_range](docs/sdks/ipranges/README.md#set_criticality_ip_range) - Set Criticality

### [kill_switch](docs/sdks/killswitch/README.md)

* [get_kill_switch_status](docs/sdks/killswitch/README.md#get_kill_switch_status) - Get Kill Switch Status
* [update_kill_switch](docs/sdks/killswitch/README.md#update_kill_switch) - Update Kill Switch

### [mobile_applications](docs/sdks/mobileapplications/README.md)

* [get_list_asset_mobile_apps](docs/sdks/mobileapplications/README.md#get_list_asset_mobile_apps) - List Mobile Applications
* [get_asset_mobile_app_details](docs/sdks/mobileapplications/README.md#get_asset_mobile_app_details) - Get Mobile Application
* [get_asset_mobile_app_changelog](docs/sdks/mobileapplications/README.md#get_asset_mobile_app_changelog) - Get Mobile Application Changelog
* [update_asset_mobile_app_status](docs/sdks/mobileapplications/README.md#update_asset_mobile_app_status) - Update Status
* [get_asset_mobile_app_notes](docs/sdks/mobileapplications/README.md#get_asset_mobile_app_notes) - List Notes
* [create_note_mobile_app](docs/sdks/mobileapplications/README.md#create_note_mobile_app) - Create Note
* [update_note_mobile_app](docs/sdks/mobileapplications/README.md#update_note_mobile_app) - Update Note
* [delete_note_mobile_app](docs/sdks/mobileapplications/README.md#delete_note_mobile_app) - Delete Note
* [get_custom_properties_mobile_app](docs/sdks/mobileapplications/README.md#get_custom_properties_mobile_app) - List Custom Properties
* [create_custom_property_mobile_app](docs/sdks/mobileapplications/README.md#create_custom_property_mobile_app) - Create Custom Property
* [update_custom_property_mobile_app](docs/sdks/mobileapplications/README.md#update_custom_property_mobile_app) - Update Custom Property
* [delete_custom_property_mobile_app](docs/sdks/mobileapplications/README.md#delete_custom_property_mobile_app) - Delete Custom Property
* [assign_mobile_app_to_business_units](docs/sdks/mobileapplications/README.md#assign_mobile_app_to_business_units) - Assign Mobile App to Business Units
* [unassign_mobile_app_from_business_units](docs/sdks/mobileapplications/README.md#unassign_mobile_app_from_business_units) - Unassign Mobile App from Business Units
* [set_criticality_mobile_app](docs/sdks/mobileapplications/README.md#set_criticality_mobile_app) - Set Criticality

### [package_managers](docs/sdks/packagemanagers/README.md)

* [get_list_asset_package_managers](docs/sdks/packagemanagers/README.md#get_list_asset_package_managers) - List Package Managers
* [get_asset_package_manager_details](docs/sdks/packagemanagers/README.md#get_asset_package_manager_details) - Get Package Manager
* [get_asset_package_manager_changelog](docs/sdks/packagemanagers/README.md#get_asset_package_manager_changelog) - Get Package Manager Changelog
* [update_asset_package_manager_status](docs/sdks/packagemanagers/README.md#update_asset_package_manager_status) - Update Status
* [get_asset_package_manager_notes](docs/sdks/packagemanagers/README.md#get_asset_package_manager_notes) - List Notes
* [add_asset_package_manager_note](docs/sdks/packagemanagers/README.md#add_asset_package_manager_note) - Create Note
* [update_asset_package_manager_note](docs/sdks/packagemanagers/README.md#update_asset_package_manager_note) - Update Note
* [delete_asset_package_manager_note](docs/sdks/packagemanagers/README.md#delete_asset_package_manager_note) - Delete Note
* [get_custom_properties_package_manager](docs/sdks/packagemanagers/README.md#get_custom_properties_package_manager) - List Custom Properties
* [create_custom_property_package_manager](docs/sdks/packagemanagers/README.md#create_custom_property_package_manager) - Create Custom Property
* [update_custom_property_package_manager](docs/sdks/packagemanagers/README.md#update_custom_property_package_manager) - Update Custom Property
* [delete_custom_property_by_id](docs/sdks/packagemanagers/README.md#delete_custom_property_by_id) - Delete Custom Property
* [assign_package_manager_to_business_units](docs/sdks/packagemanagers/README.md#assign_package_manager_to_business_units) - Assign Package Manager to Business Units
* [unassign_package_manager_from_business_units](docs/sdks/packagemanagers/README.md#unassign_package_manager_from_business_units) - Unassign Package Manager from Business Units
* [set_criticality_package_manager](docs/sdks/packagemanagers/README.md#set_criticality_package_manager) - Set Criticality

### [pending_domains](docs/sdks/pendingdomains/README.md)

* [get_list_pending_domains](docs/sdks/pendingdomains/README.md#get_list_pending_domains) - List Pending Domains

### [platform_whitelisting](docs/sdks/platformwhitelisting/README.md)

* [get_platform_dashboard_whitelist_ips](docs/sdks/platformwhitelisting/README.md#get_platform_dashboard_whitelist_ips) - List Dashboard Whitelisted IPs
* [create_platform_dashboard_whitelist_ip](docs/sdks/platformwhitelisting/README.md#create_platform_dashboard_whitelist_ip) - Add Dashboard Whitelisted IP
* [get_platform_dashboard_whitelist_status](docs/sdks/platformwhitelisting/README.md#get_platform_dashboard_whitelist_status) - Get Dashboard Whitelisting Status
* [update_platform_dashboard_whitelist_status](docs/sdks/platformwhitelisting/README.md#update_platform_dashboard_whitelist_status) - Update Dashboard Whitelisting Status
* [update_platform_dashboard_whitelist_ip](docs/sdks/platformwhitelisting/README.md#update_platform_dashboard_whitelist_ip) - Update Dashboard Whitelisted IP
* [delete_platform_dashboard_whitelist_ip](docs/sdks/platformwhitelisting/README.md#delete_platform_dashboard_whitelist_ip) - Remove Dashboard Whitelisted IP
* [get_platform_api_whitelist_ips](docs/sdks/platformwhitelisting/README.md#get_platform_api_whitelist_ips) - List API Whitelisted IPs
* [create_platform_api_whitelist_ip](docs/sdks/platformwhitelisting/README.md#create_platform_api_whitelist_ip) - Add API Whitelisted IP
* [get_platform_api_whitelist_status](docs/sdks/platformwhitelisting/README.md#get_platform_api_whitelist_status) - Get API Whitelisting Status
* [update_platform_api_whitelist_status](docs/sdks/platformwhitelisting/README.md#update_platform_api_whitelist_status) - Update API Whitelisting Status
* [update_platform_api_whitelist_ip](docs/sdks/platformwhitelisting/README.md#update_platform_api_whitelist_ip) - Update API Whitelisted IP
* [delete_platform_api_whitelist_ip](docs/sdks/platformwhitelisting/README.md#delete_platform_api_whitelist_ip) - Remove API Whitelisted IP

### [points_of_interest](docs/sdks/pointsofinterestsdk/README.md)

* [get_list_points_of_interest](docs/sdks/pointsofinterestsdk/README.md#get_list_points_of_interest) - List Points of Interest
* [convert_poi_to_finding](docs/sdks/pointsofinterestsdk/README.md#convert_poi_to_finding) - Convert Point of Interest to Finding

### [ports](docs/sdks/ports/README.md)

* [get_list_asset_ports](docs/sdks/ports/README.md#get_list_asset_ports) - List Ports
* [get_asset_port_details](docs/sdks/ports/README.md#get_asset_port_details) - Get Port

### [repositories](docs/sdks/repositories/README.md)

* [get_list_asset_repositories](docs/sdks/repositories/README.md#get_list_asset_repositories) - List Repositories
* [get_asset_repository_details](docs/sdks/repositories/README.md#get_asset_repository_details) - Get Repository
* [get_asset_repository_changelog](docs/sdks/repositories/README.md#get_asset_repository_changelog) - Get Repository Changelog
* [update_asset_repository_status](docs/sdks/repositories/README.md#update_asset_repository_status) - Update Status
* [get_asset_repository_notes](docs/sdks/repositories/README.md#get_asset_repository_notes) - List Notes
* [create_note_repository](docs/sdks/repositories/README.md#create_note_repository) - Create Note
* [update_note_repository](docs/sdks/repositories/README.md#update_note_repository) - Update Note
* [delete_note_repository](docs/sdks/repositories/README.md#delete_note_repository) - Delete Note
* [get_custom_properties_repository](docs/sdks/repositories/README.md#get_custom_properties_repository) - List Custom Properties
* [create_custom_property_repository](docs/sdks/repositories/README.md#create_custom_property_repository) - Create Custom Property
* [update_custom_property_repository](docs/sdks/repositories/README.md#update_custom_property_repository) - Update Custom Property
* [delete_custom_property_repository](docs/sdks/repositories/README.md#delete_custom_property_repository) - Delete Custom Property
* [assign_repository_to_business_units](docs/sdks/repositories/README.md#assign_repository_to_business_units) - Assign Repository to Business Units
* [unassign_repository_from_business_units](docs/sdks/repositories/README.md#unassign_repository_from_business_units) - Unassign Repository from Business Units
* [set_criticality_repository](docs/sdks/repositories/README.md#set_criticality_repository) - Set Criticality

### [saa_s_platforms](docs/sdks/saasplatforms/README.md)

* [get_list_asset_saas_platforms](docs/sdks/saasplatforms/README.md#get_list_asset_saas_platforms) - List SaaS Platforms
* [get_asset_saas_platform_details](docs/sdks/saasplatforms/README.md#get_asset_saas_platform_details) - Get SaaS Platform
* [get_asset_saas_platform_changelog](docs/sdks/saasplatforms/README.md#get_asset_saas_platform_changelog) - Get SaaS Platform Changelog
* [update_asset_saas_platform_status](docs/sdks/saasplatforms/README.md#update_asset_saas_platform_status) - Update Status
* [get_asset_saas_platform_notes](docs/sdks/saasplatforms/README.md#get_asset_saas_platform_notes) - List Notes
* [create_note_saas_platform](docs/sdks/saasplatforms/README.md#create_note_saas_platform) - Create Note
* [update_note_saas_platform](docs/sdks/saasplatforms/README.md#update_note_saas_platform) - Update Note
* [delete_note_saas_platform](docs/sdks/saasplatforms/README.md#delete_note_saas_platform) - Delete Note
* [get_custom_properties_saas_platform](docs/sdks/saasplatforms/README.md#get_custom_properties_saas_platform) - List Custom Properties
* [create_custom_property_saas_platform](docs/sdks/saasplatforms/README.md#create_custom_property_saas_platform) - Create Custom Property
* [update_custom_property_saas_platform](docs/sdks/saasplatforms/README.md#update_custom_property_saas_platform) - Update Custom Property
* [delete_custom_property_saas_platform](docs/sdks/saasplatforms/README.md#delete_custom_property_saas_platform) - Delete Custom Property
* [assign_saas_platform_to_business_units](docs/sdks/saasplatforms/README.md#assign_saas_platform_to_business_units) - Assign SaaS Platform to Business Units
* [unassign_saas_platform_from_business_units](docs/sdks/saasplatforms/README.md#unassign_saas_platform_from_business_units) - Unassign SaaS Platform from Business Units
* [set_criticality_saas_platform](docs/sdks/saasplatforms/README.md#set_criticality_saas_platform) - Set Criticality

### [security_posture_dashboard](docs/sdks/securityposturedashboard/README.md)

* [get_security_posture_dashboard](docs/sdks/securityposturedashboard/README.md#get_security_posture_dashboard) - Get Security Posture Dashboard

### [service_discovery](docs/sdks/servicediscovery/README.md)

* [get_list_service_listing](docs/sdks/servicediscovery/README.md#get_list_service_listing) - List Services
* [get_technology_statistics](docs/sdks/servicediscovery/README.md#get_technology_statistics) - List Technology Statistics

### [source_ip_addresses](docs/sdks/sourceipaddresses/README.md)

* [get_list_source_ip_addresses](docs/sdks/sourceipaddresses/README.md#get_list_source_ip_addresses) - List Testing Infrastructure

### [subdomains](docs/sdks/subdomains/README.md)

* [get_list_asset_subdomains](docs/sdks/subdomains/README.md#get_list_asset_subdomains) - List Subdomains
* [get_asset_subdomain_details](docs/sdks/subdomains/README.md#get_asset_subdomain_details) - Get Subdomain Details
* [get_asset_subdomain_changelog](docs/sdks/subdomains/README.md#get_asset_subdomain_changelog) - Get Subdomain Changelog
* [update_asset_subdomain_status](docs/sdks/subdomains/README.md#update_asset_subdomain_status) - Update Subdomain Status
* [get_notes_subdomain](docs/sdks/subdomains/README.md#get_notes_subdomain) - List Subdomain Notes
* [create_note_subdomain](docs/sdks/subdomains/README.md#create_note_subdomain) - Create Subdomain Note
* [update_note_subdomain](docs/sdks/subdomains/README.md#update_note_subdomain) - Update Subdomain Note
* [delete_note_subdomain](docs/sdks/subdomains/README.md#delete_note_subdomain) - Delete Subdomain Note
* [get_asset_subdomain_dns_records](docs/sdks/subdomains/README.md#get_asset_subdomain_dns_records) - List Subdomain DNS Records
* [get_custom_properties_subdomain](docs/sdks/subdomains/README.md#get_custom_properties_subdomain) - List Subdomain Custom Properties
* [create_custom_property_subdomain](docs/sdks/subdomains/README.md#create_custom_property_subdomain) - Create Subdomain Custom Property
* [update_custom_property_subdomain](docs/sdks/subdomains/README.md#update_custom_property_subdomain) - Update Subdomain Custom Property
* [delete_custom_property_subdomain](docs/sdks/subdomains/README.md#delete_custom_property_subdomain) - Delete Subdomain Custom Property
* [assign_subomain_to_business_units](docs/sdks/subdomains/README.md#assign_subomain_to_business_units) - Assign Subdomain to Business Units
* [unassign_subomain_from_business_units](docs/sdks/subdomains/README.md#unassign_subomain_from_business_units) - Unassign Subdomain from Business Units
* [get_asset_subdomain_engine_settings](docs/sdks/subdomains/README.md#get_asset_subdomain_engine_settings) - Get Subdomain Engine Settings
* [update_asset_subdomain_engine_settings](docs/sdks/subdomains/README.md#update_asset_subdomain_engine_settings) - Update Subdomain Engine Settings
* [set_criticality_subdomain](docs/sdks/subdomains/README.md#set_criticality_subdomain) - Set Criticality

### [suspicious_domains](docs/sdks/suspiciousdomains/README.md)

* [get_list_suspicious_domain](docs/sdks/suspiciousdomains/README.md#get_list_suspicious_domain) - List Suspicious Domains
* [get_suspicious_domain_details](docs/sdks/suspiciousdomains/README.md#get_suspicious_domain_details) - Get Suspicious Domain Details

### [user_management](docs/sdks/usermanagement/README.md)

* [list_users](docs/sdks/usermanagement/README.md#list_users) - List Users
* [get_user_details](docs/sdks/usermanagement/README.md#get_user_details) - Get User Details
* [invite_users](docs/sdks/usermanagement/README.md#invite_users) - Invite Users
* [update_user](docs/sdks/usermanagement/README.md#update_user) - Update User
* [delete_user](docs/sdks/usermanagement/README.md#delete_user) - Delete User

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation
from watchtowr_complete_watchtowr_platform_api_documentation_python.utils import BackoffStrategy, RetryConfig, parse_datetime


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.findings.get_list_findings(page=1, page_size=10, created_from=parse_datetime("2022-02-22 22:00:00"), created_to=parse_datetime("2022-02-23 22:00:00"), updated_from=parse_datetime("2022-02-22 22:00:00"), updated_to=parse_datetime("2022-02-23 22:00:00"), statuses="confirmed,unconfirmed,remediated,risk-accepted,closed,asset-no-longer-tracked", business_unit_ids="1,2,3", finding_title="Valid%20Credentials%20Discovered", severities=watchtowr_complete_watchtowr_platform_api_documentation_python.Severities.MEDIUM, asset_title="www.watchTowr.com", asset_types=watchtowr_complete_watchtowr_platform_api_documentation_python.AssetTypes.PORT, tags="CISA-KEV,Defacement,Credentials", only_validated_exploitable=False, only_unacknowledged=False, exploitation_risk_level=watchtowr_complete_watchtowr_platform_api_documentation_python.ExploitationRiskLevel.HIGH,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation
from watchtowr_complete_watchtowr_platform_api_documentation_python.utils import BackoffStrategy, RetryConfig, parse_datetime


with CompleteWatchtowrPlatformAPIDocumentation(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.findings.get_list_findings(page=1, page_size=10, created_from=parse_datetime("2022-02-22 22:00:00"), created_to=parse_datetime("2022-02-23 22:00:00"), updated_from=parse_datetime("2022-02-22 22:00:00"), updated_to=parse_datetime("2022-02-23 22:00:00"), statuses="confirmed,unconfirmed,remediated,risk-accepted,closed,asset-no-longer-tracked", business_unit_ids="1,2,3", finding_title="Valid%20Credentials%20Discovered", severities=watchtowr_complete_watchtowr_platform_api_documentation_python.Severities.MEDIUM, asset_title="www.watchTowr.com", asset_types=watchtowr_complete_watchtowr_platform_api_documentation_python.AssetTypes.PORT, tags="CISA-KEV,Defacement,Credentials", only_validated_exploitable=False, only_unacknowledged=False, exploitation_risk_level=watchtowr_complete_watchtowr_platform_api_documentation_python.ExploitationRiskLevel.HIGH)

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.APIError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `get_list_findings_async` method may raise the following exceptions:

| Error Type          | Status Code | Content Type     |
| ------------------- | ----------- | ---------------- |
| models.Unauthorized | 401         | application/json |
| models.APIError     | 4XX, 5XX    | \*/\*            |

### Example

```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation, models
from watchtowr_complete_watchtowr_platform_api_documentation_python.utils import parse_datetime


with CompleteWatchtowrPlatformAPIDocumentation(
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:
    res = None
    try:

        res = complete_watchtowr_platform_api_documentation.findings.get_list_findings(page=1, page_size=10, created_from=parse_datetime("2022-02-22 22:00:00"), created_to=parse_datetime("2022-02-23 22:00:00"), updated_from=parse_datetime("2022-02-22 22:00:00"), updated_to=parse_datetime("2022-02-23 22:00:00"), statuses="confirmed,unconfirmed,remediated,risk-accepted,closed,asset-no-longer-tracked", business_unit_ids="1,2,3", finding_title="Valid%20Credentials%20Discovered", severities=watchtowr_complete_watchtowr_platform_api_documentation_python.Severities.MEDIUM, asset_title="www.watchTowr.com", asset_types=watchtowr_complete_watchtowr_platform_api_documentation_python.AssetTypes.PORT, tags="CISA-KEV,Defacement,Credentials", only_validated_exploitable=False, only_unacknowledged=False, exploitation_risk_level=watchtowr_complete_watchtowr_platform_api_documentation_python.ExploitationRiskLevel.HIGH)

        # Handle response
        print(res)

    except models.Unauthorized as e:
        # handle e.data: models.UnauthorizedData
        raise(e)
    except models.APIError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Server Variables

The default server `https://{tenant-id}.{region}.client.watchtowr.io` contains variables and is set to `https://your-tenant-id.sg.client.watchtowr.io` by default. To override default values, the following parameters are available when initializing the SDK client instance:

| Variable    | Parameter                     | Supported Values                                | Default            | Description            |
| ----------- | ----------------------------- | ----------------------------------------------- | ------------------ | ---------------------- |
| `tenant-id` | `tenant_id: str`              | str                                             | `"your-tenant-id"` | Your tenant identifier |
| `region`    | `region: models.ServerRegion` | - `"sg"`<br/>- `"au"`<br/>- `"eu"`<br/>- `"us"` | `"sg"`             | Region                 |

#### Example

```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation
from watchtowr_complete_watchtowr_platform_api_documentation_python.utils import parse_datetime


with CompleteWatchtowrPlatformAPIDocumentation(
    tenant_id="<id>"
    region="us"
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.findings.get_list_findings(page=1, page_size=10, created_from=parse_datetime("2022-02-22 22:00:00"), created_to=parse_datetime("2022-02-23 22:00:00"), updated_from=parse_datetime("2022-02-22 22:00:00"), updated_to=parse_datetime("2022-02-23 22:00:00"), statuses="confirmed,unconfirmed,remediated,risk-accepted,closed,asset-no-longer-tracked", business_unit_ids="1,2,3", finding_title="Valid%20Credentials%20Discovered", severities=watchtowr_complete_watchtowr_platform_api_documentation_python.Severities.MEDIUM, asset_title="www.watchTowr.com", asset_types=watchtowr_complete_watchtowr_platform_api_documentation_python.AssetTypes.PORT, tags="CISA-KEV,Defacement,Credentials", only_validated_exploitable=False, only_unacknowledged=False, exploitation_risk_level=watchtowr_complete_watchtowr_platform_api_documentation_python.ExploitationRiskLevel.HIGH)

    # Handle response
    print(res)

```

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import watchtowr_complete_watchtowr_platform_api_documentation_python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation
from watchtowr_complete_watchtowr_platform_api_documentation_python.utils import parse_datetime


with CompleteWatchtowrPlatformAPIDocumentation(
    server_url="https://your-tenant-id.sg.client.watchtowr.io",
    bearer="<YOUR_BEARER_TOKEN_HERE>",
) as complete_watchtowr_platform_api_documentation:

    res = complete_watchtowr_platform_api_documentation.findings.get_list_findings(page=1, page_size=10, created_from=parse_datetime("2022-02-22 22:00:00"), created_to=parse_datetime("2022-02-23 22:00:00"), updated_from=parse_datetime("2022-02-22 22:00:00"), updated_to=parse_datetime("2022-02-23 22:00:00"), statuses="confirmed,unconfirmed,remediated,risk-accepted,closed,asset-no-longer-tracked", business_unit_ids="1,2,3", finding_title="Valid%20Credentials%20Discovered", severities=watchtowr_complete_watchtowr_platform_api_documentation_python.Severities.MEDIUM, asset_title="www.watchTowr.com", asset_types=watchtowr_complete_watchtowr_platform_api_documentation_python.AssetTypes.PORT, tags="CISA-KEV,Defacement,Credentials", only_validated_exploitable=False, only_unacknowledged=False, exploitation_risk_level=watchtowr_complete_watchtowr_platform_api_documentation_python.ExploitationRiskLevel.HIGH)

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = CompleteWatchtowrPlatformAPIDocumentation(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation
from watchtowr_complete_watchtowr_platform_api_documentation_python.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = CompleteWatchtowrPlatformAPIDocumentation(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `CompleteWatchtowrPlatformAPIDocumentation` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation
def main():

    with CompleteWatchtowrPlatformAPIDocumentation(
        bearer="<YOUR_BEARER_TOKEN_HERE>",
    ) as complete_watchtowr_platform_api_documentation:
        # Rest of application here...


# Or when using async:
async def amain():

    async with CompleteWatchtowrPlatformAPIDocumentation(
        bearer="<YOUR_BEARER_TOKEN_HERE>",
    ) as complete_watchtowr_platform_api_documentation:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from watchtowr_complete_watchtowr_platform_api_documentation_python import CompleteWatchtowrPlatformAPIDocumentation
import logging

logging.basicConfig(level=logging.DEBUG)
s = CompleteWatchtowrPlatformAPIDocumentation(debug_logger=logging.getLogger("watchtowr_complete_watchtowr_platform_api_documentation_python"))
```
<!-- End Debugging [debug] -->

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release.

### SDK Created by [Scalar](https://www.scalar.com/?utm_source=complete-watchtowr-platform-api-documentation-python&utm_campaign=python)