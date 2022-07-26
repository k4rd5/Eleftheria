from engine.item_system import Magic, Rarity
from engine.util import add_to, heal_buff, mana_buff

archive = {}


class MagicItem(Magic):
    stackable = True
    self_use = True


@add_to(archive)
class HealthPotion(MagicItem):
    def __init__(self):
        self.name = "Health Potion"
        self.information = "A common health potion from Numarre."
        self.hp_heal_amount = 500
        self.mana_heal_amount = 200

    def use(self, target):
        target.heal_hp(heal_buff(self.hp_heal_amount, target))
        target.heal_mp(mana_buff(self.mana_heal_amount, target))
