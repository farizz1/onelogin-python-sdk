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
from onelogin.models.generate_saml_assert_request import GenerateSamlAssertRequest  # noqa: E501
from onelogin.rest import ApiException

class TestGenerateSamlAssertRequest(unittest.TestCase):
    """GenerateSamlAssertRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GenerateSamlAssertRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GenerateSamlAssertRequest`
        """
        model = onelogin.models.generate_saml_assert_request.GenerateSamlAssertRequest()  # noqa: E501
        if include_optional :
            return GenerateSamlAssertRequest(
                username_or_email = '', 
                password = '', 
                app_id = '', 
                subdomain = '', 
                ip_address = ''
            )
        else :
            return GenerateSamlAssertRequest(
                username_or_email = '',
                password = '',
                app_id = '',
                subdomain = '',
        )
        """

    def testGenerateSamlAssertRequest(self):
        """Test GenerateSamlAssertRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
