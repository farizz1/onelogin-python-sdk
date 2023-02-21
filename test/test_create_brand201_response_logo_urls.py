# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import onelogin
from onelogin.models.create_brand201_response_logo_urls import CreateBrand201ResponseLogoUrls  # noqa: E501
from onelogin.rest import ApiException

class TestCreateBrand201ResponseLogoUrls(unittest.TestCase):
    """CreateBrand201ResponseLogoUrls unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateBrand201ResponseLogoUrls
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateBrand201ResponseLogoUrls`
        """
        model = onelogin.models.create_brand201_response_logo_urls.CreateBrand201ResponseLogoUrls()  # noqa: E501
        if include_optional :
            return CreateBrand201ResponseLogoUrls(
                original = '', 
                login = '', 
                navigation = ''
            )
        else :
            return CreateBrand201ResponseLogoUrls(
                original = '',
                login = '',
                navigation = '',
        )
        """

    def testCreateBrand201ResponseLogoUrls(self):
        """Test CreateBrand201ResponseLogoUrls"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
