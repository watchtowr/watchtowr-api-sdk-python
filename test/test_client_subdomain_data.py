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

from watchtowr_api_sdk.models.client_subdomain_data import ClientSubdomainData

class TestClientSubdomainData(unittest.TestCase):
    """ClientSubdomainData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClientSubdomainData:
        """Test ClientSubdomainData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClientSubdomainData`
        """
        model = ClientSubdomainData()
        if include_optional:
            return ClientSubdomainData(
                data = watchtowr_api_sdk.models.client_subdomain.ClientSubdomain(
                    type = 'subdomain', 
                    source = 'module-adversarysight-crtsh-domain-backend', 
                    status = 'verified', 
                    created_at = 2022-02-13T02:10:00.000000Z, 
                    updated_at = 2022-02-13T02:10:00.000000Z, 
                    deleted_at = 2022-02-13T02:10:00.000000Z, 
                    id = 123, 
                    name = 'subdomain.watchtowr.com', 
                    business_units = [
                        watchtowr_api_sdk.models.client_business_unit.ClientBusinessUnit(
                            id = 1, 
                            name = 'Singapore Business Unit', )
                        ], 
                    live = True, 
                    dns_records = [{"id":1690,"name":"subdomain.watchtowr.com","type":"A","ttl":922,"value":"123.123.123.123","discovered_on":"2024-08-19T08:58:26.000Z"},{"id":1685,"name":"subdomain.watchtowr.com","type":"AAAA","ttl":2687,"value":"0000:0000:0000:0000:0000:ffff:7b7b:7b7b","discovered_on":"2024-08-19T08:58:26.000Z"}], 
                    metadata = {"region":"us-west-1","service":"AWS"}, 
                    custom_properties = [{"id":10,"key":"Severity","value":"normal","isPreset":false,"modelType":"subdomain","modelId":209,"createdAt":"2024-09-24T02:37:27.000Z","updatedAt":"2024-09-24T02:38:35.000Z"},{"id":11,"key":"Vulnerability","value":"low risk","isPreset":false,"modelType":"subdomain","modelId":209,"createdAt":"2024-09-24T02:37:27.000Z","updatedAt":"2024-09-24T02:38:35.000Z"}], 
                    criticality = 'Medium', 
                    infrastructure = {"CDN":"AWS CloudFront"}, )
            )
        else:
            return ClientSubdomainData(
                data = watchtowr_api_sdk.models.client_subdomain.ClientSubdomain(
                    type = 'subdomain', 
                    source = 'module-adversarysight-crtsh-domain-backend', 
                    status = 'verified', 
                    created_at = 2022-02-13T02:10:00.000000Z, 
                    updated_at = 2022-02-13T02:10:00.000000Z, 
                    deleted_at = 2022-02-13T02:10:00.000000Z, 
                    id = 123, 
                    name = 'subdomain.watchtowr.com', 
                    business_units = [
                        watchtowr_api_sdk.models.client_business_unit.ClientBusinessUnit(
                            id = 1, 
                            name = 'Singapore Business Unit', )
                        ], 
                    live = True, 
                    dns_records = [{"id":1690,"name":"subdomain.watchtowr.com","type":"A","ttl":922,"value":"123.123.123.123","discovered_on":"2024-08-19T08:58:26.000Z"},{"id":1685,"name":"subdomain.watchtowr.com","type":"AAAA","ttl":2687,"value":"0000:0000:0000:0000:0000:ffff:7b7b:7b7b","discovered_on":"2024-08-19T08:58:26.000Z"}], 
                    metadata = {"region":"us-west-1","service":"AWS"}, 
                    custom_properties = [{"id":10,"key":"Severity","value":"normal","isPreset":false,"modelType":"subdomain","modelId":209,"createdAt":"2024-09-24T02:37:27.000Z","updatedAt":"2024-09-24T02:38:35.000Z"},{"id":11,"key":"Vulnerability","value":"low risk","isPreset":false,"modelType":"subdomain","modelId":209,"createdAt":"2024-09-24T02:37:27.000Z","updatedAt":"2024-09-24T02:38:35.000Z"}], 
                    criticality = 'Medium', 
                    infrastructure = {"CDN":"AWS CloudFront"}, ),
        )
        """

    def testClientSubdomainData(self):
        """Test ClientSubdomainData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
