from abc import ABCMeta, abstractmethod

class Renderer(object):
    """
    Abstract base class for all renders configs
    to insure consistent interface implementation

    Every class that inherit from this class have to
    emplement all abstractmethod of Renderer class
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_linear_settings(self):
        pass
