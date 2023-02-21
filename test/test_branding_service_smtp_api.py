# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import onelogin
from onelogin.api.branding_service_smtp_api import BrandingServiceSMTPApi  # noqa: E501
from onelogin.rest import ApiException


class TestBrandingServiceSMTPApi(unittest.TestCase):
    """BrandingServiceSMTPApi unit test stubs"""

    def setUp(self):
        self.api = onelogin.api.branding_service_smtp_api.BrandingServiceSMTPApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_email_settings(self):
        """Test case for delete_email_settings

        Delete Custom Email Settings  # noqa: E501
        """
        pass

    def test_get_email_settings(self):
        """Test case for get_email_settings

        Get Email Settings  # noqa: E501
        """
        pass

    def test_update_email_settings(self):
        """Test case for update_email_settings

        Update Email Settings  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
