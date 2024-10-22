""" Provides the Adder class. """
from math_operations import MathOp


class Adder(MathOp):
    """
    Adds two numbers.
    """
    def execute_op(self, val1, val2):
        """
        Executes the operation val1 + val2.
        The result can be read via the getter method of result.
        :param val1: first numerical value
        :param val2: second numerical value
        """
        self._result = val1 + val2
