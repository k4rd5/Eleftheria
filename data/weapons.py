from engine.item_system import Magic, Combat, Rarity
from engine.util import add_to

archive = {}


@add_to(archive)
class SteelSword(Combat):
    def __init__(self):
        self.name = "Steel Sword"
        self.slot = ["forehand"]
        self.type = "atk"
        self.rarity = Rarity.COMMON
        self.damage = 15


@add_to(archive)
class GreatSword(Combat):
    def __init__(self):
        self.name = "Great Sword"
        self.slot = ["forehand", "offhand"]
        self.type = "atk"
        self.rarity = Rarity.EPIC
        self.damage = 65

    def equip(self, player):
        player.status_effects.append("RAGE")

    def unequip(self, player):
        player.status_effects.remove("RAGE")


@add_to(archive)
class Vantablack(Combat):
    def __init__(self):
        self.name = "Vantablack"
        self.slot = None
        self.type = None
        self.rarity = Rarity.MYTHICAL
        self.damage = 9000
        self.information = (
            "The original blade around which the crypts of Nethercastle were built."
        )
