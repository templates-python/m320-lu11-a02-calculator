import pytest

from adder import Adder
from divider import Divider
from math_operations import MathOp
from multiplier import Multiplier
from subtractor import Subtractor


class TestMathOp:
    def test_math_op_instantiate(self):
        with pytest.raises(TypeError):
            math_op = MathOp()
    def test_operation_created(self):
        adder = Adder()
        assert adder.result == 0.0

    def test_adder(self):
        adder = Adder()
        adder.execute_op(5, 8)
        assert adder.result == 13

    def test_subtraktor(self):
        subtractor = Subtractor()
        subtractor.execute_op(20, 8)
        assert subtractor.result == 12

    def test_multiplier(self):
        multiplier = Multiplier()
        multiplier.execute_op(3, 5)
        assert multiplier.result == 15

    def test_divider_well(self):
        divider = Divider()
        divider.execute_op(33, 3)
        assert divider.result == 11

    def test_divider_by_zero(self):
        divider = Divider()
        with pytest.raises(ZeroDivisionError):
            divider.execute_op(33, 0)