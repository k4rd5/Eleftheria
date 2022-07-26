import random
from engine.game import Game
from engine.entity import Entity, Monster
import engine.util as util
import engine.mechanism as mechanism
import engine.combat_system as cs
import data.misc_items as items
import data.actions as actions
from environments import town, forest
from engine.npc import Npc, Dialogue
from environments.shops import Shop


# TEST VARIABLES
game = Game('persons')
bread = game.data.items.consumables["Bread"]()
shop = Shop(game.data.items.consumables, 'food')


def set_inventory():
    bread = game.data.items.consumables["Bread"]()
    game.player.add_item(bread, 64)
    game.player.inventory.give_currency("gold", 20)


def move():
    x = random.randrange(0, 3)
    y = random.randrange(0, 3)
    game.location.set_location((x, y))


def move_time():
    time = random.randrange(1, 10)
    game.clock.tick(time)


def status():
    print(f"Location: {game.location.coordinates}")
    print(
        f"Time: {game.clock.time} Weather: {game.location.get_temperature(game.clock.time)}"
    )
    print(f"Seed: {game.dynamic_seed()}")


def player_status():
    print(f"Name: {game.player.name}")
    print(f"HP: [{game.player.hp}/{game.player.mhp}]")
    print(f"MP: [{game.player.mp}/{game.player.mmp}]")
    print(
        f"Status effect: {[effect.name for effect in game.player.status_effects]}")
    print(game.player.atk_multiplier,
          game.player.def_multiplier, game.player.stamina)
    print("-" * 10)


def status_effect_test():
    player_status()
    for i in range(4):
        print("Turn", i + 1)

        game.player.affect([cs.Poison()])
        player_status()
    player_status()


def move_around_and_shit():
    town = (
        util.variables["colors"]["fore"]["yellow"]
        + "T"
        + util.variables["colors"]["reset"]
    )
    forest = (
        util.variables["colors"]["fore"]["green"]
        + "F"
        + util.variables["colors"]["reset"]
    )
    while True:
        util.clear()
        status()
        game.location.display([town, forest])
        print("\n[w] [a] [s] [d]")
        direction = input("> ").lower().strip()
        if direction == "w":
            game.location.move(2)
        elif direction == "s":
            game.location.move(3)
        elif direction == "a":
            game.location.move(0)
        elif direction == "d":
            game.location.move(1)
        else:
            break


def use_action_test():
    gavin = Game('gavin')
    poke = Game('poke')

    attack = actions.archive['Punch']()

    print(gavin.player.hp)
    print(poke.player.stamina)
    print('Attack Success:', poke.player.use_action(gavin.player, attack))
    print(gavin.player.hp)
    print(poke.player.stamina)


def test():
    poke = Game('Poke')

    rest = actions.archive['Rest']()
    punch = actions.archive['Punch']()

    print(poke.player.stamina)
    poke.player.use_action(poke.player, punch)
    print(poke.player.stamina)
    poke.player.use_action(poke.player, rest)
    print(poke.player.stamina)


def battle_test():
    game1 = Game("Puck")
    monster = Monster('Avaster')

    punch = actions.archive['Punch']()
    rest = actions.archive['Rest']()

    game1.player.combat_options.extend([punch, rest])
    monster.combat_options.extend([punch, rest])

    battle = cs.Battle(game1.player, monster)
    battle.start()


def npctest():

    n1 = Npc()

    def no():
        print('quitting anyway lol')
        quit()

    n1.lines = [Dialogue(lines=['Hey there!'], question='Do you want to quit?',
                         answer_redirection={'Yes': quit, 'No': no})]
    poke = Game('poke')
    poke.player.interact(n1)


def shop_demo():
    game.player.inventory.give_currency('gold', 8000)
    shop.on_entry(game.player)
