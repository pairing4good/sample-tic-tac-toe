
class StubBuiltInsWrapper:
    console = ''
    recorded_inputs = []

    def __init__(self, recorded_inputs):
        self.recorded_inputs = recorded_inputs

    def wrapped_print(self, value):
        self.console += (value + '\n')

    def wrapped_print_no_return(self, value):
        self.console += value

    def wrapped_input(self, value):
        out = self.recorded_inputs.pop(0)
        self.console += (value + str(out) + '\n')
        return out

    def wrapped_exit(self):
        return

    def actual_console(self):
        return self.console

    def clean(self):
        return
