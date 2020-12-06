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
