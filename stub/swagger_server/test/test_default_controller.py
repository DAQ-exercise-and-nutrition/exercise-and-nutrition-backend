# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.exercise import Exercise  # noqa: E501
from swagger_server.models.food import Food  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_controller_get_exercises(self):
        """Test case for controller_get_exercises

        Get a list of exercises
        """
        response = self.client.open(
            '/exercise-and-nutrition-api/v3/exercises',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_foods(self):
        """Test case for controller_get_foods

        Get a list of foods
        """
        response = self.client.open(
            '/exercise-and-nutrition-api/v3/foods',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
