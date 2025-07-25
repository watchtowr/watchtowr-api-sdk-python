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

from watchtowr_api_sdk.models.client_port_data import ClientPortData

class TestClientPortData(unittest.TestCase):
    """ClientPortData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClientPortData:
        """Test ClientPortData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClientPortData`
        """
        model = ClientPortData()
        if include_optional:
            return ClientPortData(
                data = watchtowr_api_sdk.models.client_port.ClientPort(
                    type = 'TCP', 
                    status = 'verified', 
                    created_at = 2022-02-13T02:10:00.000000Z, 
                    updated_at = 2022-02-13T02:10:00.000000Z, 
                    last_seen_at = 2022-02-13T02:10:00.000000Z, 
                    deleted_at = 2022-02-13T02:10:00.000000Z, 
                    id = 123, 
                    ip = '123.123.123.123', 
                    ip_id = 333, 
                    port = 22, 
                    banner = 'OpenSSH6.6.1p1 Ubuntu 2ubuntu2.13Ubuntu Linux; protocol 2.0', 
                    service = 'ssh', 
                    business_units = [
                        watchtowr_api_sdk.models.client_business_unit.ClientBusinessUnit(
                            id = 1, 
                            name = 'Singapore Business Unit', )
                        ], )
            )
        else:
            return ClientPortData(
                data = watchtowr_api_sdk.models.client_port.ClientPort(
                    type = 'TCP', 
                    status = 'verified', 
                    created_at = 2022-02-13T02:10:00.000000Z, 
                    updated_at = 2022-02-13T02:10:00.000000Z, 
                    last_seen_at = 2022-02-13T02:10:00.000000Z, 
                    deleted_at = 2022-02-13T02:10:00.000000Z, 
                    id = 123, 
                    ip = '123.123.123.123', 
                    ip_id = 333, 
                    port = 22, 
                    banner = 'OpenSSH6.6.1p1 Ubuntu 2ubuntu2.13Ubuntu Linux; protocol 2.0', 
                    service = 'ssh', 
                    business_units = [
                        watchtowr_api_sdk.models.client_business_unit.ClientBusinessUnit(
                            id = 1, 
                            name = 'Singapore Business Unit', )
                        ], ),
        )
        """

    def testClientPortData(self):
        """Test ClientPortData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
