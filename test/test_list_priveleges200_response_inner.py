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
from onelogin.models.list_priveleges200_response_inner import ListPriveleges200ResponseInner  # noqa: E501
from onelogin.rest import ApiException

class TestListPriveleges200ResponseInner(unittest.TestCase):
    """ListPriveleges200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListPriveleges200ResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListPriveleges200ResponseInner`
        """
        model = onelogin.models.list_priveleges200_response_inner.ListPriveleges200ResponseInner()  # noqa: E501
        if include_optional :
            return ListPriveleges200ResponseInner(
                id = '2c963197-bee2-4607-abc0-4786f1bfa55a', 
                name = 'User Administrator', 
                description = 'Can administer users', 
                privilege = onelogin.models.list_priveleges_200_response_inner_privilege.listPriveleges_200_response_inner_privilege(
                    version = '2018-05-18', 
                    statement = [
                        onelogin.models.list_priveleges_200_response_inner_privilege_statement_inner.listPriveleges_200_response_inner_privilege_Statement_inner(
                            effect = 'Allow', 
                            action = ["Users:Delete","Users:ResetPassword","Users:Unlock","Users:Get"], 
                            scope = [
                                '*'
                                ], )
                        ], )
            )
        else :
            return ListPriveleges200ResponseInner(
                name = 'User Administrator',
                privilege = onelogin.models.list_priveleges_200_response_inner_privilege.listPriveleges_200_response_inner_privilege(
                    version = '2018-05-18', 
                    statement = [
                        onelogin.models.list_priveleges_200_response_inner_privilege_statement_inner.listPriveleges_200_response_inner_privilege_Statement_inner(
                            effect = 'Allow', 
                            action = ["Users:Delete","Users:ResetPassword","Users:Unlock","Users:Get"], 
                            scope = [
                                '*'
                                ], )
                        ], ),
        )
        """

    def testListPriveleges200ResponseInner(self):
        """Test ListPriveleges200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
