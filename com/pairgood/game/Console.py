from com.pairgood.wrapper.BuiltInsWrapper import BuiltInsWrapper


class Console:
    built_ins_wrapper: BuiltInsWrapper

    def __init__(self, built_ins_wrapper):
        self.built_ins_wrapper = built_ins_wrapper

    def display_computer_turn(self, c_choice):
        self.built_ins_wrapper.wrapped_print(f'Computer turn [{c_choice}]')

    def display_human_turn(self, h_choice):
        self.built_ins_wrapper.wrapped_print(f'Human turn [{h_choice}]')
