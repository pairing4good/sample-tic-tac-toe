class StubChoiceWrapper:
    answers: []

    def __init__(self, answers):
        self.answers = answers

    def choice(self, seq):
        return self.answers.pop(0)
