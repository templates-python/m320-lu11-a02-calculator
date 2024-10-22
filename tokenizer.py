""" Provide a class to tokenize a string into 3 tokens:"""
import ast

from exceptions import OperationException
from exceptions import NumberFormatException


class Tokenizer:
    """
    This class tokenizes an input (mathematical expression) into the 3 tokens
    - value_1
    - operation
    - value_2
    The tokens can be read using the properties.

    The allowed operation signs are defined in a list.
    Additional operation signs can be added using the method add_operation.
    The corresponding adjustments have to be made in the Calculator class as well as in the
    derived classes.

    Attributes
    ----------
    value1 : float
        1st value of the calculation
    operation : str
        operation sign of the calculation
    value2 : float
        2nd value of the calculation
    operations : char[]
        list of allowed operation signs

    """

    def __init__(self):
        """ Constructor """
        self._value1 = None
        self._operation = None
        self._value2 = None

        self._operations = ['+', '-', '*', '/']

    @property
    def value1(self):
        """
        return the first number
        :return: 1st number
        """

        return self._value1

    @property
    def value2(self):
        """
        return the second number
        :return: 2nd number
        """
        return self._value2

    @property
    def operation(self):
        """
        return the operation sign as string
        :return: operation sign
        """
        return self._operation

    def add_operation(self, operation):
        """
        Add an operation sign to the list of operations.
        The method checks if the sign is already part of the list.
        If the sign already exists, it is not added.
        :param operation: The sign of the operation
        """

        if operation not in self._operations:
            self._operations.append(operation)
        else:
            print(f'Zeichen {operation} ist schon Teil der Liste')

    @property
    def operations(self):
        """
        return the list of all operations (only used for testing)
        :return: list of operations
        """
        return self._operations

    def split(self, command_line):
        """
        Splits the string based on the occurrence of operation signs from the list.
        If the operation sign is missing, an OperationException is thrown.
        If a number value is invalid, a NumberFormatException is thrown.
        :param command_line: user input
        """

        # prüfen, ob ein gültiges Operationszeichen im String erkannt wird. Dazu die Liste aller Zeichen
        # abarbeiten. Wenn das Zeichen nicht erkannt wird, wird eine Exception erzeugt.
        for sign in self._operations:
            if sign in command_line:
                # die Zeichenkette entlang der Operationszeichen auftrennen
                elements = command_line.partition(sign)
                self._operation = sign
                # sicherstellen, dass es sich um gültige Zahlenwerte handelt
                try:
                    self._value1 = ast.literal_eval(elements[0].strip())
                except Exception:
                    raise NumberFormatException(elements[0])
                try:
                    self._value2 = ast.literal_eval(elements[2].strip())
                except Exception:
                    raise NumberFormatException(elements[2])
                return
        # es wurde kein Operationszeichen gefunden
        raise OperationException()


# TEST
if __name__ == '__main__':
    t = Tokenizer()
    print(t.operations)
    t.add_operation('+')
    t.add_operation('^')
    print(t.operations)
    try:
        t.split('3.25/7.568')
        #
        print(t.value1)
        print(t.operation)
        print(t.value2)
    except OperationException as exception:
        print(exception)
    except NumberFormatException as exception:
        print(exception)