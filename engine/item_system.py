# item system

""" ok first of all no use function, that will be called in main.py so that the
game variable can be passed to it"""  # what??


class Rarity:
    COMMON = "common"
    UNCOMMON = "uncommon"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"
    RELIC = "relic"
    MYTHICAL = "mythical"
    UNOBTAINABLE = "unobtainable"


class Item:
    name = None
    information = None
    stackable = True
    self_use = True
    usable = True
    cost = {}

    def __str__(self):
        return self.name

    def use(self, **args):
        return False

    def equip(self, **args):
        if "slot" in self.__dict__.keys():
            return None
        return False

    def unequip(self, **args):
        if "slot" in self.__dict__.keys():
            return None
        return False


class Consumable(Item):
    name = None
    stackable = True
    information = None
    self_use = True
    heal_amount = 0

    def use(self, target):
        target.heal_hp(self.heal_amount)


class Magic(Item):
    name = None
    stackable = False
    information = None
    self_use = False
    mana_usage = 0


class Combat(Item):
    name = None
    stackable = False
    information = None
    self_use = False
    slot = None
    cost = 0
    crafting_recipe = None
    rarity = None
    type_ = None


class Stack:
    def __init__(self, item, amount=1):
        self.name = item.name
        self.item = item
        self.amount = amount
        self.STACK_LIMIT = 32
        self.set_stack_limit()

    def set_stack_limit(self):
        if not self.item.stackable:
            self.STACK_LIMIT = 1

    @property
    def isempty(self):
        return self.amount <= 0

    @property
    def isfull(self):
        return self.amount >= self.STACK_LIMIT

    def get(self, amount=1):  # get item object, and remove amount
        """warning: changing item's properties changes the properties of items in the stack,
        so its better to make the stackability of the object False if you plan to change its
        properties"""

        self.remove(amount)
        return self.item

    def add(
        self, amount=1
    ):  # increment stack amount and return remainder, used with player.add_to_stack
        remainder = amount - (self.STACK_LIMIT - self.amount)
        if remainder <= 0:
            self.increment(amount)
            remainder = 0
        else:
            self.increment(amount - remainder)
        return remainder

    def remove(self, amount=1):
        remainder = self.amount - amount  # left to subtract

        if remainder <= 0:
            self.decrement(amount)
            remainder = -remainder
        else:
            self.decrement(amount)
            remainder = 0

        return remainder

    def increment(self, amount=1):
        self.amount += amount
        if self.amount > self.STACK_LIMIT:
            self.amount = self.STACK_LIMIT
            return False  # full
        return True  # space left

    def decrement(self, amount=1):

        self.amount -= amount
        if self.amount < 0:
            self.amount = 0
            return False  # empty
        return True  # not empty yet

    def reset(self):
        self.amount = 0
