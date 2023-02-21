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
from onelogin.models.get_event_types200_response_data_inner import GetEventTypes200ResponseDataInner  # noqa: E501
from onelogin.rest import ApiException

class TestGetEventTypes200ResponseDataInner(unittest.TestCase):
    """GetEventTypes200ResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GetEventTypes200ResponseDataInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetEventTypes200ResponseDataInner`
        """
        model = onelogin.models.get_event_types200_response_data_inner.GetEventTypes200ResponseDataInner()  # noqa: E501
        if include_optional :
            return GetEventTypes200ResponseDataInner(
                name = 'APP_REMOVED_FROM_ROLE', 
                description = 'App %app% removed from role %role%', 
                id = 2
            )
        else :
            return GetEventTypes200ResponseDataInner(
        )
        """

    def testGetEventTypes200ResponseDataInner(self):
        """Test GetEventTypes200ResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
