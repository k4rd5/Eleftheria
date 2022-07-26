import time


class Dialogue:
    def __init__(self, lines=[], question=None, answer_redirection={}):
        self.lines = lines
        self.question = question
        self.answer_redirection = answer_redirection

    def commence(self):
        if self.lines:
            for line in self.lines:
                print(line)

        if self.question:
            print(self.question)
            for n, answer in enumerate(self.answer_redirection.keys()):
                print(f'[{n+1}] {answer}')
            choice = int(input('> ').strip().lower())
            self.answer_redirection[list(self.answer_redirection)[choice-1]]()


class Npc:
    name = None
    hp = 100
    mhp = 100
    mp = 100
    mmp = 100
    quests = []
    lines = []

    def on_interaction(self, **args):
        for dialogue in self.lines:
            dialogue.commence()

    def leave_interaction(self, **args):
        pass
