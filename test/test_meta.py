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

from watchtowr_api_sdk.models.meta import Meta

class TestMeta(unittest.TestCase):
    """Meta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Meta:
        """Test Meta
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Meta`
        """
        model = Meta()
        if include_optional:
            return Meta(
                pagination = watchtowr_api_sdk.models.pagination.Pagination(
                    total = 1.337, 
                    count = 1.337, 
                    per_page = 1.337, 
                    current_page = 1.337, 
                    total_pages = 1.337, 
                    links = watchtowr_api_sdk.models.link.Link(
                        previous = '', 
                        next = '', ), )
            )
        else:
            return Meta(
                pagination = watchtowr_api_sdk.models.pagination.Pagination(
                    total = 1.337, 
                    count = 1.337, 
                    per_page = 1.337, 
                    current_page = 1.337, 
                    total_pages = 1.337, 
                    links = watchtowr_api_sdk.models.link.Link(
                        previous = '', 
                        next = '', ), ),
        )
        """

    def testMeta(self):
        """Test Meta"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
