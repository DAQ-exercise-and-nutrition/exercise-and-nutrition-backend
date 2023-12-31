# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Nutrition(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, nutrition_id: int=None, nutrition_recomend: str=None, goal: str=None, exercise_recommend: str=None):  # noqa: E501
        """Nutrition - a model defined in Swagger

        :param nutrition_id: The nutrition_id of this Nutrition.  # noqa: E501
        :type nutrition_id: int
        :param nutrition_recomend: The nutrition_recomend of this Nutrition.  # noqa: E501
        :type nutrition_recomend: str
        :param goal: The goal of this Nutrition.  # noqa: E501
        :type goal: str
        :param exercise_recommend: The exercise_recommend of this Nutrition.  # noqa: E501
        :type exercise_recommend: str
        """
        self.swagger_types = {
            'nutrition_id': int,
            'nutrition_recomend': str,
            'goal': str,
            'exercise_recommend': str
        }

        self.attribute_map = {
            'nutrition_id': 'nutrition_id',
            'nutrition_recomend': 'nutrition_recomend',
            'goal': 'goal',
            'exercise_recommend': 'exercise_recommend'
        }
        self._nutrition_id = nutrition_id
        self._nutrition_recomend = nutrition_recomend
        self._goal = goal
        self._exercise_recommend = exercise_recommend

    @classmethod
    def from_dict(cls, dikt) -> 'Nutrition':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Nutrition of this Nutrition.  # noqa: E501
        :rtype: Nutrition
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nutrition_id(self) -> int:
        """Gets the nutrition_id of this Nutrition.


        :return: The nutrition_id of this Nutrition.
        :rtype: int
        """
        return self._nutrition_id

    @nutrition_id.setter
    def nutrition_id(self, nutrition_id: int):
        """Sets the nutrition_id of this Nutrition.


        :param nutrition_id: The nutrition_id of this Nutrition.
        :type nutrition_id: int
        """

        self._nutrition_id = nutrition_id

    @property
    def nutrition_recomend(self) -> str:
        """Gets the nutrition_recomend of this Nutrition.


        :return: The nutrition_recomend of this Nutrition.
        :rtype: str
        """
        return self._nutrition_recomend

    @nutrition_recomend.setter
    def nutrition_recomend(self, nutrition_recomend: str):
        """Sets the nutrition_recomend of this Nutrition.


        :param nutrition_recomend: The nutrition_recomend of this Nutrition.
        :type nutrition_recomend: str
        """

        self._nutrition_recomend = nutrition_recomend

    @property
    def goal(self) -> str:
        """Gets the goal of this Nutrition.


        :return: The goal of this Nutrition.
        :rtype: str
        """
        return self._goal

    @goal.setter
    def goal(self, goal: str):
        """Sets the goal of this Nutrition.


        :param goal: The goal of this Nutrition.
        :type goal: str
        """

        self._goal = goal

    @property
    def exercise_recommend(self) -> str:
        """Gets the exercise_recommend of this Nutrition.


        :return: The exercise_recommend of this Nutrition.
        :rtype: str
        """
        return self._exercise_recommend

    @exercise_recommend.setter
    def exercise_recommend(self, exercise_recommend: str):
        """Sets the exercise_recommend of this Nutrition.


        :param exercise_recommend: The exercise_recommend of this Nutrition.
        :type exercise_recommend: str
        """

        self._exercise_recommend = exercise_recommend
