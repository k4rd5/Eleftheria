from engine.combat_system import Action
from .status_effects import archive as effects
from engine.util import add_to

archive = {}

# Action class types:
# > Action associated with an object
# > Action associated with a spell
# > Player Actions
# > Entity Actions


@add_to(archive)
class Punch(Action):
    name = 'Punch'
    information = 'Punch the opponent'
    requirements = {'stamina': 10}
    cost = {'stamina': 10}
    type_ = ['melee', 'attack']
    status_effects = [effects['Poison']]
    damage = 10

    def use(self, victim):
        self.apply_effect(victim)
        victim.damage_hp(self.damage)
        return True


@add_to(archive)
class Rest(Action):
    name = 'Rest'
    information = 'Replenish stamina'
    type_ = ['self', 'heal']
    amount = 10

    def use(self, user):
        user.heal_stamina(self.amount)
        return True
