from engine.item_system import Magic, Combat, Rarity
from engine.util import add_to

archive = {}


@add_to(archive)
class SteelSword(Combat):
    def __init__(self):
        self.name = "Steel Sword"
        self.equipable_slot = ["forehand"]
        self.type = "atk"
        self.rarity = Rarity.COMMON
        self.damage = 15
        self.number_of_uses = 20


@add_to(archive)
class GreatSword(Combat):
    def __init__(self):
        self.name = "Great Sword"
        self.equipable_slot = ["forehand", "offhand"]
        self.type = "atk"
        self.rarity = Rarity.EPIC
        self.damage = 65
        self.number_of_uses = 30


@add_to(archive)
class Vantablack(Combat):
    def __init__(self):
        self.name = "Vantablack"
        self.type = None
        self.rarity = Rarity.MYTHICAL
        self.damage = 9000
        self.information = (
            "The original blade around which the crypts of Nethercastle were built."
        )
        self.number_of_uses = 2000
