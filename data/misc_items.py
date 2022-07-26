from engine.item_system import Item, Rarity
from engine.util import add_to

archive = {}


class Scroll(Item):
    def __init__(self, name, data, information=None):
        self.name = name
        self.information = information
        self.stackable = False
        self.self_use = False
        self.usable = False
        self.data = data

    def use(self):
        lines = self.data.split("\n")
        newlines = ""
        length = 0
        a = lines + [
            "SCROLL NAME:  " + self.name,
            "SCROLL INFORMATION  " + str(self.information),
        ]
        for line in a:
            if len(line) > length:
                length = len(line)
        for line in lines:
            newlines += "| " + line + " " * (length - len(line)) + " |\n"
        length += 2

        return f"+{'-'*length}+\n| SCROLL NAME: {self.name}{' '*(length-14-len(self.name))}|\n| SCROLL INFORMATION: {self.information}{' '*(length-21-len(str(self.information)))}|\n+{'-'*length}+\n{newlines}+{'-'*length}+"
