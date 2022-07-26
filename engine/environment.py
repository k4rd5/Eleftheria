import random


class Environment:
    name = None
    information = "No information available."

    special_coordinates = None
    size = (15, 40)  # min and max
    sub_env = []

    npcs = []
    monsters = []
    loot = []
    map_ = None
    local_coordinates = []

    entry_requirements = {}
    inside = False

    def on_entry(self, **args):
        self.inside = True

    def on_exit(self, **args):
        self.inside = False
