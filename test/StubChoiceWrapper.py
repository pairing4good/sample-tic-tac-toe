class StubChoiceWrapper:
    answers: []

    def __init__(self, answers):
        self.answers = answers

    def choice(self, seq):
        self.answers.pop(0)