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

from watchtowr_api_sdk.models.paginated_api_documentation import PaginatedApiDocumentation

class TestPaginatedApiDocumentation(unittest.TestCase):
    """PaginatedApiDocumentation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginatedApiDocumentation:
        """Test PaginatedApiDocumentation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginatedApiDocumentation`
        """
        model = PaginatedApiDocumentation()
        if include_optional:
            return PaginatedApiDocumentation(
                data = [
                    watchtowr_api_sdk.models.client_api_documentation_asset.ClientApiDocumentationAsset(
                        id = 1, 
                        type = 'apiDocumentation', 
                        name = 'example_docs/example-swagger-hub', 
                        source = 'module-adversarysight-swaggerhub-saas-discovery', 
                        platform = 'SwaggerHub API', 
                        status = 'verified', 
                        created_at = 2022-02-13T02:10:00.000000Z, 
                        url = 'https://app.swaggerhub.com/apis/example_docs/example-swagger-hub/', 
                        custom_properties = [{"id":10,"key":"Severity","value":"normal","isPreset":false,"modelType":"apiDocumentation","modelId":209,"createdAt":"2024-09-24T02:37:27.000Z","updatedAt":"2024-09-24T02:38:35.000Z"},{"id":11,"key":"Vulnerability","value":"low risk","isPreset":false,"modelType":"apiDocumentation","modelId":209,"createdAt":"2024-09-24T02:37:27.000Z","updatedAt":"2024-09-24T02:38:35.000Z"}], 
                        criticality = 'Medium', )
                    ],
                meta = watchtowr_api_sdk.models.meta.Meta(
                    pagination = {"total":20,"count":10,"per_page":10,"current_page":1,"total_pages":2,"links":{"previous":"url","next":"url"}}, )
            )
        else:
            return PaginatedApiDocumentation(
                data = [
                    watchtowr_api_sdk.models.client_api_documentation_asset.ClientApiDocumentationAsset(
                        id = 1, 
                        type = 'apiDocumentation', 
                        name = 'example_docs/example-swagger-hub', 
                        source = 'module-adversarysight-swaggerhub-saas-discovery', 
                        platform = 'SwaggerHub API', 
                        status = 'verified', 
                        created_at = 2022-02-13T02:10:00.000000Z, 
                        url = 'https://app.swaggerhub.com/apis/example_docs/example-swagger-hub/', 
                        custom_properties = [{"id":10,"key":"Severity","value":"normal","isPreset":false,"modelType":"apiDocumentation","modelId":209,"createdAt":"2024-09-24T02:37:27.000Z","updatedAt":"2024-09-24T02:38:35.000Z"},{"id":11,"key":"Vulnerability","value":"low risk","isPreset":false,"modelType":"apiDocumentation","modelId":209,"createdAt":"2024-09-24T02:37:27.000Z","updatedAt":"2024-09-24T02:38:35.000Z"}], 
                        criticality = 'Medium', )
                    ],
                meta = watchtowr_api_sdk.models.meta.Meta(
                    pagination = {"total":20,"count":10,"per_page":10,"current_page":1,"total_pages":2,"links":{"previous":"url","next":"url"}}, ),
        )
        """

    def testPaginatedApiDocumentation(self):
        """Test PaginatedApiDocumentation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
