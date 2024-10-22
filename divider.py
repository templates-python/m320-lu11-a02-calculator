""" provides the class Divider, which divides two numbers """
from math_operations import MathOp


class Divider(MathOp):
    """
    Divide two numbers.
    It must be ensured that the dividend is not 0!
    """

    def execute_op(self, val1, val2):
        """
        Executes the operation val1 / val2.
        The result can be read via the getter method of result.
        If the divisor is delivered the value 0, a ZeroDivisionError is raised.
        :param val1: first numerical value
        :param val2: second numerical value
        """
        if val2 != 0:
            self._result = val1 / val2
        else:
            raise ZeroDivisionError()
