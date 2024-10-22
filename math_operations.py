""" Provides an abstract class for mathematical operations. """
from abc import abstractmethod, ABC


class MathOp(ABC):
    """
    An abstract class representing any (binary) mathematical operation.
    The method execute_op is abstract and must be overridden by concrete classes.
    The method result returns the result of the executed operation.
    Note: unary operations like the factorial (!) cannot be calculated.
    """

    def __init__(self):
        """
        Initializes the result of the operation.
        """
        self._result = 0.0

    @abstractmethod
    def execute_op(self, val1, val2):
        """
        Defines the interface for the calculation of a binary operation (operation with 2 values).
        The method receives two values as parameters and then performs the appropriate operation.
        The concrete operation is determined in the derived class.
        :param val1: first numerical value
        :param val2: second numerical value
        """
        pass

    @property
    def result(self):
        """
        Returns the result of the mathematical operation.
        :return: result of the operation
        """
        return self._result
