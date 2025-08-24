# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from watchtowr_api_sdk.api.api_documentation_api import APIDocumentationApi
    from watchtowr_api_sdk.api.activity_log_api import ActivityLogApi
    from watchtowr_api_sdk.api.add_asset_api import AddAssetApi
    from watchtowr_api_sdk.api.business_unit_api import BusinessUnitApi
    from watchtowr_api_sdk.api.certificates_api import CertificatesApi
    from watchtowr_api_sdk.api.cloud_integration_assets_api import CloudIntegrationAssetsApi
    from watchtowr_api_sdk.api.cloud_storage_api import CloudStorageApi
    from watchtowr_api_sdk.api.containers_api import ContainersApi
    from watchtowr_api_sdk.api.dns_record_analysis_api import DNSRecordAnalysisApi
    from watchtowr_api_sdk.api.domains_api import DomainsApi
    from watchtowr_api_sdk.api.finding_retest_history_api import FindingRetestHistoryApi
    from watchtowr_api_sdk.api.findings_api import FindingsApi
    from watchtowr_api_sdk.api.hunts_api import HuntsApi
    from watchtowr_api_sdk.api.ip_addresses_api import IPAddressesApi
    from watchtowr_api_sdk.api.ip_ranges_api import IPRangesApi
    from watchtowr_api_sdk.api.kill_switch_api import KillSwitchApi
    from watchtowr_api_sdk.api.mobile_applications_api import MobileApplicationsApi
    from watchtowr_api_sdk.api.package_managers_api import PackageManagersApi
    from watchtowr_api_sdk.api.pending_domains_api import PendingDomainsApi
    from watchtowr_api_sdk.api.points_of_interest_api import PointsOfInterestApi
    from watchtowr_api_sdk.api.ports_api import PortsApi
    from watchtowr_api_sdk.api.repositories_api import RepositoriesApi
    from watchtowr_api_sdk.api.saa_s_platforms_api import SaaSPlatformsApi
    from watchtowr_api_sdk.api.security_posture_dashboard_api import SecurityPostureDashboardApi
    from watchtowr_api_sdk.api.service_discovery_api import ServiceDiscoveryApi
    from watchtowr_api_sdk.api.source_ip_addresses_api import SourceIPAddressesApi
    from watchtowr_api_sdk.api.subdomains_api import SubdomainsApi
    from watchtowr_api_sdk.api.suspicious_domains_api import SuspiciousDomainsApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from watchtowr_api_sdk.api.api_documentation_api import APIDocumentationApi
from watchtowr_api_sdk.api.activity_log_api import ActivityLogApi
from watchtowr_api_sdk.api.add_asset_api import AddAssetApi
from watchtowr_api_sdk.api.business_unit_api import BusinessUnitApi
from watchtowr_api_sdk.api.certificates_api import CertificatesApi
from watchtowr_api_sdk.api.cloud_integration_assets_api import CloudIntegrationAssetsApi
from watchtowr_api_sdk.api.cloud_storage_api import CloudStorageApi
from watchtowr_api_sdk.api.containers_api import ContainersApi
from watchtowr_api_sdk.api.dns_record_analysis_api import DNSRecordAnalysisApi
from watchtowr_api_sdk.api.domains_api import DomainsApi
from watchtowr_api_sdk.api.finding_retest_history_api import FindingRetestHistoryApi
from watchtowr_api_sdk.api.findings_api import FindingsApi
from watchtowr_api_sdk.api.hunts_api import HuntsApi
from watchtowr_api_sdk.api.ip_addresses_api import IPAddressesApi
from watchtowr_api_sdk.api.ip_ranges_api import IPRangesApi
from watchtowr_api_sdk.api.kill_switch_api import KillSwitchApi
from watchtowr_api_sdk.api.mobile_applications_api import MobileApplicationsApi
from watchtowr_api_sdk.api.package_managers_api import PackageManagersApi
from watchtowr_api_sdk.api.pending_domains_api import PendingDomainsApi
from watchtowr_api_sdk.api.points_of_interest_api import PointsOfInterestApi
from watchtowr_api_sdk.api.ports_api import PortsApi
from watchtowr_api_sdk.api.repositories_api import RepositoriesApi
from watchtowr_api_sdk.api.saa_s_platforms_api import SaaSPlatformsApi
from watchtowr_api_sdk.api.security_posture_dashboard_api import SecurityPostureDashboardApi
from watchtowr_api_sdk.api.service_discovery_api import ServiceDiscoveryApi
from watchtowr_api_sdk.api.source_ip_addresses_api import SourceIPAddressesApi
from watchtowr_api_sdk.api.subdomains_api import SubdomainsApi
from watchtowr_api_sdk.api.suspicious_domains_api import SuspiciousDomainsApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
