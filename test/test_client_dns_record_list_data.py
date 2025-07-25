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

from watchtowr_api_sdk.models.client_dns_record_list_data import ClientDnsRecordListData

class TestClientDnsRecordListData(unittest.TestCase):
    """ClientDnsRecordListData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClientDnsRecordListData:
        """Test ClientDnsRecordListData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClientDnsRecordListData`
        """
        model = ClientDnsRecordListData()
        if include_optional:
            return ClientDnsRecordListData(
                data = [{"id":1690,"name":"example.com","type":"A","ttl":922,"value":"123.123.123.123","discovered_on":"2024-08-19T08:58:26.000Z"},{"id":1685,"name":"example.com","type":"AAAA","ttl":2687,"value":"0000:0000:0000:0000:0000:ffff:7b7b:7b7b","discovered_on":"2024-08-19T08:58:26.000Z"},{"id":1684,"name":"example.com","type":"NS","ttl":17366,"value":"ns-1342.example.org","discovered_on":"2024-08-19T08:58:26.000Z"}],
                meta = watchtowr_api_sdk.models.meta.Meta(
                    pagination = {"total":20,"count":10,"per_page":10,"current_page":1,"total_pages":2,"links":{"previous":"url","next":"url"}}, )
            )
        else:
            return ClientDnsRecordListData(
                data = [{"id":1690,"name":"example.com","type":"A","ttl":922,"value":"123.123.123.123","discovered_on":"2024-08-19T08:58:26.000Z"},{"id":1685,"name":"example.com","type":"AAAA","ttl":2687,"value":"0000:0000:0000:0000:0000:ffff:7b7b:7b7b","discovered_on":"2024-08-19T08:58:26.000Z"},{"id":1684,"name":"example.com","type":"NS","ttl":17366,"value":"ns-1342.example.org","discovered_on":"2024-08-19T08:58:26.000Z"}],
                meta = watchtowr_api_sdk.models.meta.Meta(
                    pagination = {"total":20,"count":10,"per_page":10,"current_page":1,"total_pages":2,"links":{"previous":"url","next":"url"}}, ),
        )
        """

    def testClientDnsRecordListData(self):
        """Test ClientDnsRecordListData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
