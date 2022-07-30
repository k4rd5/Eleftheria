# entity.py
from .inventory import Inventory, Bank


class Stats:
    def __init__(self, name, xp=0, level=1, levelling_up=None):
        self.name = name
        self.level = level
        self.xp = xp
        self.levelling_up = levelling_up or {
            1: 100,
            2: 130,
            3: 140,
            4: 160,
            5: 200,
        }

    def update(self):
        xp_requirement = self.levelling_up[self.level]
        if self.xp >= xp_requirement and self.level + 1 in self.xp_requirement.keys():
            self.level += 1
            self.xp = 0

    def add_xp(self, xp):
        self.xp += xp
        self.update()


class Entity:

    name = None
    hp = 100
    mhp = 100
    mp = 100
    mmp = 100
    status_effects = []
    stamina = 100
    mstamina = 100
    combat_options = []
    counter = 0
    level = Stats(name="level", level=1)

    atk_multiplier = 10
    def_multiplier = 5

    @property
    def alive(self):
        return not self.hp == 0

    @property
    def full_health(self):
        return self.hp == self.mhp

    @property
    def is_monster(self):
        if type(self) is Monster:
            return True
        return False

    # status effect

    def apply_affect(self, list_):
        for status_effect in list_:
            if status_effect().name not in [
                effect.name for effect in self.status_effects
            ]:
                self.status_effects.append(status_effect())

    def affect(self):
        for status_effect in self.status_effects:
            status_effect.affect(self)

    def remove_effect(self, effect):
        for status_effect in list(self.status_effects):
            if status_effect.name == effect.name:
                self.status_effects.remove(status_effect)

    # heal

    def heal_hp(self, amount):
        self.hp += amount
        if self.hp > self.mhp:
            self.hp = self.mhp

    def heal_mp(self, amount):
        self.mp += amount
        if self.mp > self.mmp:
            self.mp = self.mmp

    def heal_stamina(self, amount):
        self.stamina += amount
        if self.stamina > self.mstamina:
            self.stamina = self.mstamina

    # damage

    def damage_hp(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def damage_mp(self, amount):
        self.mp -= amount
        if self.mp < 0:
            self.mp = 0

    def damage_stamina(self, amount):
        self.stamina -= amount
        if self.stamina < 0:
            self.stamina = 0

    def reset_stats(self):
        self.hp = self.mhp
        self.mp = self.mmp
        self.stamina = self.mstamina
        self.statusEffect = []
        self.counter = 0

    def use_action(self, victim, action):

        for req, val in action.requirements.items():  # check requirements
            if type(val) is int and getattr(self, req) < val:
                return False
            elif type(val) is not int and getattr(self, req) != val:
                return False
        for req, val in action.cost.items():  # remove cost
            newval = getattr(self, req) - val
            setattr(self, req, newval)
        return action.use(victim)

    # ok listen, what if your opponent in battle is another player
    def move_decide(self):
        move = self.combat_options[self.current_move_index]
        if self.current_move_index < len(self.combat_options)-1:
            self.current_move_index += 1
        else:
            self.current_move_index = 0
        return move

    def interact(self, npc):
        npc.on_interaction()
        npc.leave_interaction()


# player
class Player(Entity):

    def __init__(self, name, currency=None, combat_options=None):

        self.name = name
        self.hp = 200
        self.mhp = 200
        self.mp = 250
        self.mmp = 250
        self.combat_options = combat_options or []
        self.slots = {
            'forehand': None,
            'offhand': None,
            'armor': None,
            'shield': None,
        }
        self.stats = {
            "combat": Stats(name="combat"),
            "magic": Stats(name="magic"),
            "crafting": Stats(name="crafting"),
            "looting": Stats(name="looting"),
            "exploration": Stats(name="exploration"),
            "dungeoneering": Stats(name="dungeoneering"),
            "smithing": Stats(name="smithing"),
            "quest": Stats(name="quest"),
        }
        self.current_battle = None
        self.inventory = Inventory(currency=currency or {})
        self.bank = Bank()
        self.physical_stats = {"dex": 1, "int": 1, "str": 1, "vit": 1}
        self.stat_points = 10
        self.mastery_tree = {"sword": 0, "knife": 0,
                             "bow": 0, "axe": 0, "hammer": 0}
        self.mastery_points = 1

    @ property
    def dexterity(self):
        return self.physical_stats["dex"]

    @ property
    def intelligence(self):
        return self.physical_stats["int"]

    @ property
    def vitality(self):
        return self.physical_stats["vit"]

    @ property
    def strength(self):
        return self.physical_stats["str"]

    def equip(self, item):
        if item.equipable_slot and self.inventory.check_item(item):
            self.remove_item(item)
            item.equip(self)
        else:
            return False

    def unequip(self, slots):
        for slot in slots:
            if self.slots[slot]:
                self.slots[slot].unequip(self)

    def get_slot_object(self, slot):
        for slot_, item in self.slots.items():
            if slot == slot_:
                return self.slots[slot]

    def add_xp(self, level, xp):
        level.add_xp(xp)

    # if you are a player, you get to choose.
    def move_decide(self):
        print('Choose an action:')
        for num, option in enumerate(self.combat_options):
            print(f'[{num+1}] {option.name} - "{option.information}"')

        return self.combat_options[int(input("> ")) - 1]

    # item

    def add_item(self, item, amount=1):
        self.inventory.add_item(item, amount)

    def remove_item(self, item, amount=1):
        return self.inventory.remove_item(item, amount)

    def take_item(self, item, amount=1):
        return self.inventory.take_item(item, amount)

    def take_currencies(self, currency_dict):
        if not self.check_currencies(currency_dict):
            return False
        for currency, amount in currency_dict.items():
            self.inventory.take_currency(currency, amount)
        return True

    # testing purposes

    def information(self):
        print("-" * 20)
        print(
            f"name: {self.name}, money: {self.inventory.currency}, level: {self.level.level}"
        )
        print(f"status effect: {self.status_effects}")
        print(
            f"hp: {self.hp}/{self.mhp} \nmp: {self.mp}/{self.mmp} \nstamina: {self.stamina}/{self.mstamina}"
        )
        print(f"Items: {self.inventory.stackAmounts()}")
        print(f"slots: {self.slots} stat points: {self.physical_stats}")

    # inefficient

    def check_stats(self, stats={}):
        if stats:
            for stat in stats.keys():
                try:
                    if self.__dict__[stat] < stats[stat]:
                        return False
                except TypeError:
                    if self.__dict__[stat] != stats[stat]:
                        return False
            return True
        else:
            return True

    def check_levels(self, levels={}):
        if levels:
            for level in levels.keys():
                if self.levels[level].level < levels[level]:
                    return False
            return True
        else:
            return True

    def check_mastery(self, mastery={}):
        if mastery:
            for topic in mastery:
                if self.mastery_tree[topic] < mastery[topic]:
                    return False
            return True

    def check_currencies(self, currencies_dict):
        for currency, amount in currencies_dict.items():
            if not self.inventory.check_currency(currency, amount):
                return False
        return True

    def enter(self, location):
        return location.on_entry(self)

    def use_item(self, item, victim=None):
        if not victim and item.self_use:
            self.use_item(item, self)
        return self.inventory.use_item(item, victim)


class Monster(Entity):
    default_hp = 100
    default_mp = 100
    default_stamina = 100

    def __init__(
        self,
        name,
        drops=None,
        hp=None,
        mp=None,
        status_effects=None,
        stamina=None,
        combat_options=None,
        level=None,
    ):

        self.name = name
        self.hp = hp or self.default_hp
        self.mhp = hp or self.default_hp
        self.mp = mp or self.default_mp
        self.mmp = mp or self.default_mp
        self.status_effects = status_effects or []
        self.stamina = stamina or self.default_stamina
        self.mstamina = stamina or self.default_stamina
        self.combat_options = combat_options or []
        self.current_move_index = 0
        self.level = level or 0
        self.drops = drops or []

        # default monster behaviour algorithm:
        # attack patterns.
