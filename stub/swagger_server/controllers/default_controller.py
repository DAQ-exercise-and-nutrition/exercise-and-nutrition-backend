import connexion
import six

from swagger_server.models.exercise import Exercise  # noqa: E501
from swagger_server.models.food import Food  # noqa: E501
from swagger_server import util


def controller_get_exercises(target=None, limit=None, random=None):  # noqa: E501
    """Get a list of all exercises

     # noqa: E501

    :param target: 
    :type target: str
    :param limit: 
    :type limit: int
    :param random: 
    :type random: bool

    :rtype: List[Exercise]
    """
    return 'do some magic!'


def controller_get_exercises_by_body_part(body_part, limit=None, random=None):  # noqa: E501
    """Get exercises for a specific body part

     # noqa: E501

    :param body_part: 
    :type body_part: str
    :param limit: 
    :type limit: int
    :param random: 
    :type random: bool

    :rtype: List[Exercise]
    """
    return 'do some magic!'


def controller_get_exercises_by_target(target, limit=None, random=None):  # noqa: E501
    """Get exercises for a specific target

     # noqa: E501

    :param target: 
    :type target: str
    :param limit: 
    :type limit: int
    :param random: 
    :type random: bool

    :rtype: List[Exercise]
    """
    return 'do some magic!'


def controller_get_foods(diet=None, meal_type=None, limit=None, random=None):  # noqa: E501
    """Get a list of all foods

     # noqa: E501

    :param diet: 
    :type diet: str
    :param meal_type: 
    :type meal_type: str
    :param limit: 
    :type limit: int
    :param random: 
    :type random: bool

    :rtype: List[Food]
    """
    return 'do some magic!'


def controller_get_foods_by_diet(diet, limit=None, random=None):  # noqa: E501
    """Get foods for a specific diet

     # noqa: E501

    :param diet: 
    :type diet: str
    :param limit: 
    :type limit: int
    :param random: 
    :type random: bool

    :rtype: List[Food]
    """
    return 'do some magic!'


def controller_get_foods_by_meal_type(meal_type, limit=None, random=None):  # noqa: E501
    """Get foods for a specific meal type

     # noqa: E501

    :param meal_type: 
    :type meal_type: str
    :param limit: 
    :type limit: int
    :param random: 
    :type random: bool

    :rtype: List[Food]
    """
    return 'do some magic!'
