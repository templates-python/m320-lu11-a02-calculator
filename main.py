""" main routine for the calculator program """
from calculator import Calculator
from exceptions import OperationException, NumberFormatException
from tokenizer import Tokenizer


def main():
    """
    Creates the Tokenizer and Calculator objects
    Runs the calculator
    - Read the calculation from the user
    - Determine the operation
    - Perform the calculation
    All exceptions are caught and printed
    """

    calc = Calculator(Tokenizer())
    try:
        calc.read_input()
        calc.create_concrete_op()
        calc.calculate()
    except OperationException as op_ex:
        print(op_ex)
    except NumberFormatException as nf_ex:
        print(nf_ex)
    except ZeroDivisionError:
        print('ERROR: Division mit 0!')


if __name__ == '__main__':
    main()
