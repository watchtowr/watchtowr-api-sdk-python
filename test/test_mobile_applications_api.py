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

from watchtowr_api_sdk.api.mobile_applications_api import MobileApplicationsApi


class TestMobileApplicationsApi(unittest.TestCase):
    """MobileApplicationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MobileApplicationsApi()

    def tearDown(self) -> None:
        pass

    def test_assign_mobile_app_to_business_units(self) -> None:
        """Test case for assign_mobile_app_to_business_units

        Assign Mobile App to Business Units
        """
        pass

    def test_create_custom_property_mobile_app(self) -> None:
        """Test case for create_custom_property_mobile_app

        Create Custom Property
        """
        pass

    def test_create_note_mobile_app(self) -> None:
        """Test case for create_note_mobile_app

        Create Note
        """
        pass

    def test_delete_custom_property_mobile_app(self) -> None:
        """Test case for delete_custom_property_mobile_app

        Delete Custom Property
        """
        pass

    def test_delete_note_mobile_app(self) -> None:
        """Test case for delete_note_mobile_app

        Delete Note
        """
        pass

    def test_get_asset_mobile_app_details(self) -> None:
        """Test case for get_asset_mobile_app_details

        Get Mobile Application
        """
        pass

    def test_get_asset_mobile_app_notes(self) -> None:
        """Test case for get_asset_mobile_app_notes

        List Notes
        """
        pass

    def test_get_custom_properties_mobile_app(self) -> None:
        """Test case for get_custom_properties_mobile_app

        List Custom Properties
        """
        pass

    def test_get_list_asset_mobile_apps(self) -> None:
        """Test case for get_list_asset_mobile_apps

        List Mobile Applications
        """
        pass

    def test_unassign_mobile_app_from_business_units(self) -> None:
        """Test case for unassign_mobile_app_from_business_units

        Unassign Mobile App from Business Units
        """
        pass

    def test_update_asset_mobile_app_status(self) -> None:
        """Test case for update_asset_mobile_app_status

        Update Status
        """
        pass

    def test_update_custom_property_mobile_app(self) -> None:
        """Test case for update_custom_property_mobile_app

        Update Custom Property
        """
        pass

    def test_update_note_mobile_app(self) -> None:
        """Test case for update_note_mobile_app

        Update Note
        """
        pass


if __name__ == '__main__':
    unittest.main()
