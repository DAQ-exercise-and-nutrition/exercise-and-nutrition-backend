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


def controller_get_foods():  # noqa: E501
    """Get a list of foods

     # noqa: E501


    :rtype: List[Food]
    """
    return 'do some magic!'
