import connexion
import six

from swagger_server.models.exercise import Exercise  # noqa: E501
from swagger_server.models.food import Food  # noqa: E501
from swagger_server import util


def controller_get_exercises():  # noqa: E501
    """Get a list of exercises

     # noqa: E501


    :rtype: List[Exercise]
    """
    return 'do some magic!'


def controller_get_exercises_by_body_part(body_part):  # noqa: E501
    """Get exercises for a specific body part

     # noqa: E501

    :param body_part: 
    :type body_part: str

    :rtype: List[Exercise]
    """
    return 'do some magic!'


def controller_get_exercises_by_target(target):  # noqa: E501
    """Get exercises for a specific target

     # noqa: E501

    :param target: 
    :type target: str

    :rtype: List[Exercise]
    """
    return 'do some magic!'


def controller_get_foods():  # noqa: E501
    """Get a list of foods

     # noqa: E501


    :rtype: List[Food]
    """
    return 'do some magic!'


def controller_get_foods_by_diet(diet):  # noqa: E501
    """Get foods for a specific diet

     # noqa: E501

    :param diet: 
    :type diet: str

    :rtype: List[Food]
    """
    return 'do some magic!'


def controller_get_foods_by_meal_type(meal_type):  # noqa: E501
    """Get foods for a specific meal type

     # noqa: E501

    :param meal_type: 
    :type meal_type: str

    :rtype: List[Food]
    """
    return 'do some magic!'
