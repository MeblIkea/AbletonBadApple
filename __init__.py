import Live
from .BadApple import BadApple


def create_instance(c_instance):
    """ Creates and returns the APC20 script """
    return BadApple(c_instance)
