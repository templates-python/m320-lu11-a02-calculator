""" Provides a class for reading user input. """
class Reader:
    """
    Reads the user input from the console.
    It is a singleton, as the input (keyboard) is a physical device that is present only once.
    """

    def __new__(self):
        """ Singleton implementation """
        if not hasattr(self, '_instance'):
            self._instance = super(Reader, self).__new__(self)
        return self._instance

    def screen_info(self):
        """
        User prompt for the input.
        """
        print(f'Geben Sie eine Rechnung in der Form 5 + 7 ein. \nFühren Sie die Berechnung mit <ENTER> aus.')

    def read(self):
        """
        Reads the user input (as string)
        """
        return input('Eingabe: ')


# TEST
if __name__ == '__main__':
    reader = Reader()
    reader.screen_info()
    value = reader.read()
    print(value)