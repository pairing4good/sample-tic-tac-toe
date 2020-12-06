import platform
from os import system

class BuiltInsWrapper:
    def wrapped_print(self, value):
        print(value)

    def wrapped_print_no_return(self, value):
        print(value, end='')

    def wrapped_input(self, value):
        return input(value)

    def wrapped_exit(self):
        exit()

    def clean(self):
        """
        Clears the console
        """
        os_name = platform.system().lower()
        if 'windows' in os_name:
            system('cls')
        else:
            system('clear')
