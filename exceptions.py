""" Provides custom exceptions for the calculator. """
class OperationException(Exception):
    """
    This exception is raised when no valid operation sign is recognized
    during the split of the input.
    """
    def __init__(self):
        super().__init__('ERROR: ungültiges Operationszeichen eingegeben!')


class NumberFormatException(Exception):
    """
    This exception is raised when an invalid number format is detected.
    """
    def __init__(self, value):
        super().__init__(f'ERROR:  {value}  ist ein ungültiger Zahlenwert')
