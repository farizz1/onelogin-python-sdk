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
from onelogin.models.create_app_request_one_of1_configuration import CreateAppRequestOneOf1Configuration  # noqa: E501
from onelogin.rest import ApiException

class TestCreateAppRequestOneOf1Configuration(unittest.TestCase):
    """CreateAppRequestOneOf1Configuration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateAppRequestOneOf1Configuration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateAppRequestOneOf1Configuration`
        """
        model = onelogin.models.create_app_request_one_of1_configuration.CreateAppRequestOneOf1Configuration()  # noqa: E501
        if include_optional :
            return CreateAppRequestOneOf1Configuration(
                signature_algorithm = '', 
                certificate_id = 56
            )
        else :
            return CreateAppRequestOneOf1Configuration(
                signature_algorithm = '',
                certificate_id = 56,
        )
        """

    def testCreateAppRequestOneOf1Configuration(self):
        """Test CreateAppRequestOneOf1Configuration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
