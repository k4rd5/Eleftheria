# attack system

from .entity import Entity, Monster
from .util import clear
import math


class StatusEffect:
    name = None
    counter = 0
    duration = 0

    def iter(self):
        self.counter += 1
        if self.counter > self.duration:
            self.counter = 0


class Action:

    name = None
    information = None
    requirements = {}
    cost = {}
    cooldown = 0
    status_effects = []
    type_ = []

    def use(self, **args):
        pass

    def apply_effect(self, victim):
        for status_effect in self.status_effects:
            if status_effect().name not in [
                effect.name for effect in victim.status_effects
            ]:
                victim.status_effects.append(status_effect())


# works perfectly fine
# a bit boring though if both sides deal the same damage and it just ends with both player and opponent dead
# maybe add like a delay between opponent attacks, maybe like a stamina heal break or something to let the player attack

class Battle:
    def __init__(self, player1, player2, counter=0):
        self.player = player1
        self.opponent = player2
        self.counter = counter
        self.winner = None
        # unnecessary, can be fixed with logic but i want to make this system work first
        self.loser = None
        self.reset_stats_after_match = [Monster]

    def hp_bar(self, name, hp, char=None):
        if not char:
            char = "█"

        return (
            f'[{name}] '+"|"
            + char * math.floor((hp[0] / 10))
            + " " * math.floor((hp[1] - hp[0]) / 10)
            + "|" + f' [{hp[0]}/{hp[1]}]'
        )

    def start(self):
        self.player.current_battle = self
        self.reset()
        clear()
        while self.player.alive and self.opponent.alive:
            if self.counter != 0:
                # choose actions

                choice = self.player.move_decide()
                # if npc then attack pattern is set, unless specified otherwise
                opp_choice = self.opponent.move_decide()
                clear()

                # find who to use them on
                player_affects = self.opponent
                opponent_affects = self.player
                if 'self' in choice.type_:
                    player_affects = self.player
                if 'self' in opp_choice.type_:
                    opponent_affects = self.opponent

                # use actions on victims
                self.player.use_action(player_affects, choice)
                self.opponent.use_action(opponent_affects, opp_choice)

                self.player.affect()
                self.opponent.affect()

            # display player data
            print('----------------------')
            if self.counter == 0:
                print(
                    f'"{self.player.name}" has encountered "{self.opponent.name}"!')
            else:
                print(f'{self.player.name} used [{choice.name}]!')
            print('----------------------')
            print()
            print(self.hp_bar('HP', (self.player.hp, self.player.mhp)), end=' ')
            print([effect.name for effect in self.player.status_effects])
            print()
            print(self.hp_bar('MP', (self.player.mp, self.player.mmp)))
            print('     '+self.hp_bar('Stm', (self.player.stamina,
                  self.player.mstamina), char='*'))
            print()

            # display opponent data
            print('----------------------')
            if self.counter == 0:
                print(f'"{self.opponent.name}" has appeared!')
            else:
                print(f'{self.opponent.name} used [{opp_choice.name}]!')
            print('----------------------')
            print()
            print(self.hp_bar('HP', (self.opponent.hp, self.opponent.mhp)), end=' ')
            print([effect.name for effect in self.opponent.status_effects])
            print()
            print(self.hp_bar('MP', (self.opponent.mp, self.opponent.mmp)))
            print('     '+self.hp_bar('Stm', (self.opponent.stamina,
                  self.opponent.mstamina), char='*'))
            self.counter += 1

        # someone died and battle ended, what if they take each other out though?
        if not self.player.alive and not self.player.alive:
            print(f'Both {self.player.name} and {self.opponent.name} died.')
            return self.winner
        elif self.player.alive:
            self.winner = self.player
            self.loser = self.opponent
        else:
            self.winner = self.opponent
            self.loser = self.player

        # conclusion of the battle
        print(f'{self.winner.name} has defeated {self.loser.name}!')
        return self.winner

    def reset(self):
        self.counter = 0
        self.winner = None
        self.loser = None
        if type(self.opponent) in self.reset_stats_after_match:
            self.opponent.reset_stats()


# working on skill system and whole combat shit, also entity and player baseclass
