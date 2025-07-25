# coding: utf-8

"""
    Complete watchTowr Platform API Documentation

    The watchTowr Client API combining all watchTowr Platform APIs into a single comprehensive reference, including:       * Continuous Assurance API       * Adversary Sight API       * Intelligence API       * Platform API 

    The version of the OpenAPI document: 1.0
    Contact: support@watchTowr.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from watchtowr_api_sdk.models.hunt_overview_dto import HuntOverviewDto

class TestHuntOverviewDto(unittest.TestCase):
    """HuntOverviewDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HuntOverviewDto:
        """Test HuntOverviewDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HuntOverviewDto`
        """
        model = HuntOverviewDto()
        if include_optional:
            return HuntOverviewDto(
                total_hunts_executed = 25,
                total_unresolved_hunts = 3,
                latest_executed_hunts = [
                    watchtowr_api_sdk.models.latest_executed_hunt_dto.LatestExecutedHuntDto(
                        id = '1', 
                        title = 'CVE-2024-1234 Apache RCE', 
                        status = 'completed', 
                        total_findings = 2, 
                        total_assets = 5, 
                        need_investigation = False, 
                        request_type = 'SoftwareVulnerability', 
                        resolved_status = False, 
                        acknowledgement = null, 
                        threat_actors = [
                            watchtowr_api_sdk.models.threat_actor_dto.ThreatActorDto(
                                attacker_name = 'APT29', 
                                country = 'ru', )
                            ], )
                    ]
            )
        else:
            return HuntOverviewDto(
                total_hunts_executed = 25,
                total_unresolved_hunts = 3,
                latest_executed_hunts = [
                    watchtowr_api_sdk.models.latest_executed_hunt_dto.LatestExecutedHuntDto(
                        id = '1', 
                        title = 'CVE-2024-1234 Apache RCE', 
                        status = 'completed', 
                        total_findings = 2, 
                        total_assets = 5, 
                        need_investigation = False, 
                        request_type = 'SoftwareVulnerability', 
                        resolved_status = False, 
                        acknowledgement = null, 
                        threat_actors = [
                            watchtowr_api_sdk.models.threat_actor_dto.ThreatActorDto(
                                attacker_name = 'APT29', 
                                country = 'ru', )
                            ], )
                    ],
        )
        """

    def testHuntOverviewDto(self):
        """Test HuntOverviewDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
