# game.py


from .clock import Clock
from .map import Map
from .entity import Player
from data import consumables, weapons, magic_items, misc_items, actions, status_effects
from environments import town, forest
from .util import world_seed, dynamic_seed
import pickle


# DATA SECTION


class ItemData:
    def __init__(self):
        self.consumables = consumables.archive
        self.weapons = weapons.archive
        self.magic = magic_items.archive
        self.misc = misc_items.archive


class EnvironmentData:
    def __init__(self):
        self.town = town.Town
        self.forest = forest.Forest

    @property
    def list_(self):
        return [place for place in self.__dict__.values()]


class CombatData:
    def __init__(self):
        self.actions = actions.archive
        self.status_effects = status_effects.archive


class GameData:
    items = ItemData()
    environments = EnvironmentData()
    combat = CombatData()


# GAME SECTION


class Game:
    def __init__(self, name, currency={}, location=[0, 0], seed=None):
        self.seed = seed or world_seed
        self.location = Map(seed=self.seed, coordinates=location)
        self.clock = Clock()
        self.data = GameData()
        self.player = Player(name, currency=currency)

    def save(self, filename="save"):
        with open("saves\\" + filename + ".sav", "wb") as f:
            pickle.dump(self.__dict__, f, pickle.HIGHEST_PROTOCOL)

    def load(self, filename="save"):
        with open("saves\\" + filename + ".sav", "rb") as f:
            load_game = pickle.load(f)
        self.__dict__.update(load_game)

    # look into this asap, i do not remember how deep and messy this rabbit hole is
    def dynamic_seed(self, coordinates=None, time=True):
        if time:
            time = self.clock.time
        if not coordinates:
            coordinates = self.location.coordinates
        return dynamic_seed(coordinates, time, self.seed)


if __name__ == "__main__":
    pass
