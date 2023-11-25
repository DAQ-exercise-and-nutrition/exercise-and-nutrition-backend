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

        Get a list of all exercises
        """
        query_string = [('target', 'target_example'),
                        ('limit', 2),
                        ('random', true)]
        response = self.client.open(
            '/exercise-and-nutrition-api/v3/exercises',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_exercises_by_body_part(self):
        """Test case for controller_get_exercises_by_body_part

        Get exercises for a specific body part
        """
        query_string = [('limit', 2),
                        ('random', true)]
        response = self.client.open(
            '/exercise-and-nutrition-api/v3/exercises/body_part/{bodyPart}'.format(body_part='body_part_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_exercises_by_target(self):
        """Test case for controller_get_exercises_by_target

        Get exercises for a specific target
        """
        query_string = [('limit', 2),
                        ('random', true)]
        response = self.client.open(
            '/exercise-and-nutrition-api/v3/exercises/target/{target}'.format(target='target_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_foods(self):
        """Test case for controller_get_foods

        Get a list of all foods
        """
        query_string = [('diet', 'diet_example'),
                        ('meal_type', 'meal_type_example'),
                        ('limit', 2),
                        ('random', true)]
        response = self.client.open(
            '/exercise-and-nutrition-api/v3/foods',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_foods_by_diet(self):
        """Test case for controller_get_foods_by_diet

        Get foods for a specific diet
        """
        query_string = [('limit', 2),
                        ('random', true)]
        response = self.client.open(
            '/exercise-and-nutrition-api/v3/foods/diet/{diet}'.format(diet='diet_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_foods_by_meal_type(self):
        """Test case for controller_get_foods_by_meal_type

        Get foods for a specific meal type
        """
        query_string = [('limit', 2),
                        ('random', true)]
        response = self.client.open(
            '/exercise-and-nutrition-api/v3/foods/meal_type/{mealType}'.format(meal_type='meal_type_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
