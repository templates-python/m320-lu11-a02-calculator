""" Provides the Calculator class. """
from adder import Adder
from divider import Divider
from multiplier import Multiplier
from reader import Reader
from subtractor import Subtractor


class Calculator:
    """
    Provides a class for the calculator.
    The calculator reads the user input, splits it into its components,
    creates the concrete operation and executes it.
    """

    def __init__(self, tokenizer_object):
        """
        Creates a Calculator object.
        Initializes the Reader object and assigns the Tokenizer.
        :param tokenizer_object: Tokenizer object
        """
        self._math_op = None
        self._my_reader = Reader()
        self._tokenizer = tokenizer_object

    @property
    def math_op(self):
        """
        Returns the reference of the currently created MathOp object.
        :return: reference of the MathOp object
        """
        return self._math_op

    def read_input(self):
        """
        Reads a value from the keyboard and passes the string to the splitter.
        The exceptions that occur are only processed in the main program!
        """
        self._my_reader.screen_info()
        value = self._my_reader.read()
        self._tokenizer.split(value)

    def create_concrete_op(self):
        """
        Factory method for creating the concrete operation.
        The concrete operation is determined by the operation sign.
        If the operation sign is not recognized, the reference is set to None.
        Note: This case should never occur, as the Tokenizer otherwise throws an exception.
        But for safety reasons, it should be implemented this way.
        """
        if self._tokenizer.operation == '+':
            self._math_op = Adder()
        elif self._tokenizer.operation == '-':
            self._math_op = Subtractor()
        elif self._tokenizer.operation == '*':
            self._math_op = Multiplier()
        elif self._tokenizer.operation == '/':
            self._math_op = Divider()
        else:
            self._math_op = None

    def calculate(self):
        """
        Executes the operation created in create_concrete_op.
        Note: No exceptions are processed.
        """
        if self._math_op is not None:
            self._math_op.execute_op(self._tokenizer.value1, self._tokenizer.value2)
            print(f'Ergebnis: {self._math_op.result}')
