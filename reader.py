""" Provides a class for reading user input. """
class Reader:
    """
    Reads the user input from the console.
    It is a singleton, as the input (keyboard) is a physical device that is present only once.
    """

    def __new__(cls):
        """ Singleton implementation """
        if not hasattr(cls, '_instance'):
            cls._instance = super(Reader, cls).__new__(cls)
        return cls._instance

    def screen_info(self):
        """
        User prompt for the input.
        """
        print('Geben Sie eine Rechnung in der Form 5 + 7 ein.')
        print('Führen Sie die Berechnung mit <ENTER> aus.')

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
