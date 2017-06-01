"""
    A decorator to remove the boiler plate for making lazy attributes/properties.
"""

import functools

class lazy_property(object):
    """
        A decorator to remove the boiler plate for making lazy attributes/properties.
    """
    def __init__(self, func):
        self.__func = func
        functools.wraps(self.__func)(self)

    def __get__(self, instance, owner):
        if instance is None:
            return self

        if not hasattr(instance, '__dict__'):
            # The attribute has not been set.
            raise AttributeError('{} object has no attribute: __dict__'.format(owner.__name__))

        name = self.__name__
        if name.startswith('__') and not name.endswith('__'):
            name = '_{}{}'.format(owner.__name__, name)

        value = self.__func(instance)
        instance.__dict__[name] = value
        return value
