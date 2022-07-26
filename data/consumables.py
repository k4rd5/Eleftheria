from engine.item_system import Consumable
from engine.util import add_to

archive = {}


@add_to(archive)
class Bread(Consumable):
    name = "Bread"
    information = f"A loaf of {name}"
    heal_amount = 20
    cost = {'gold': 10}


@add_to(archive)
class Juice(Consumable):
    name = "Juice"
    information = f"A glass of cold {name} juice"
    heal_amount = 100


@add_to(archive)
class Burger(Consumable):
    name = "Burger"
    information = f"A steaming hot {name}, as if frozen in time."
    heal_amount = 35
