from engine.util import add_to
from engine.combat_system import StatusEffect

archive = {}


@add_to(archive)
class Poison(StatusEffect):
    def __init__(self, damage=10, duration=3):
        self.name = "Poison"
        self.damage = damage
        self.duration = duration

    def affect(self, victim):
        self.iter()
        if self.counter:
            victim.damage_hp(self.damage)
        else:
            victim.remove_effect(self)


@add_to(archive)
class Burning(StatusEffect):
    def __init__(self, damage=20, duration=4):
        self.name = "Burning"
        self.damage = damage
        self.duration = duration

    def affect(self, victim):
        self.iter()
        if self.counter:
            victim.damage_hp(self.damage)
        else:
            victim.status_effects.remove(self)


@add_to(archive)
class Confusion(StatusEffect):
    def __init__(self, duration=3):
        self.name = "Confusion"
        self.duration = duration
        self.atk = None
        self.def_ = None

    def affect(self, victim):
        self.iter()
        if not self.atk and not self.def_:
            self.atk = victim.atk_multiplier
            self.def_ = victim.def_multiplier
            victim.atk_multiplier = 0
            victim.def_multiplier = 0
        if not self.counter:
            victim.atk_multiplier = self.atk
            victim.def_multiplier = self.def_
            self.atk_ = 0
            self.def_ = 0
            victim.status_effects.remove(self)


@add_to(archive)
class Freeze(StatusEffect):
    def __init__(self, duration=4):
        self.name = "Freeze"
        self.duration = duration
        self.atk_ = 0
        self.def_ = 0
        self.stamina_ = 0

    def affect(self, victim):
        self.iter()
        if self.counter == 1:
            self.atk_ = victim.atk_multiplier
            self.def_ = victim.def_multiplier
            self.stamina_ = victim.stamina
            victim.stamina = victim.atk_multiplier = victim.def_multiplier = 0

        elif not self.counter:
            victim.stamina = self.stamina_
            victim.atk_multiplier = self.atk_
            victim.def_multiplier = self.def_
            self.atk_ = 0
            self.def_ = 0
            self.stamina_ = 0
            victim.status_effects.remove(self)


@add_to(archive)
class Paralysed(StatusEffect):
    def __init__(self, duration=3):
        self.name = "Paralysed"
        self.duration = duration
        self.stamina_ = 0

    def affect(self, victim):
        self.iter()
        if not self.stamina_:
            self.stamina_ = victim.stamina
            victim.stamina_ = 0

        if not self.counter:
            victim.stamina = self.stamina_
            self.stamina_ = 0
            victim.status_effects.remove(self)
