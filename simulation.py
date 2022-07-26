from engine.util import save, load
from engine.game import Game

game = Game('')
game.__dict__ = load(filename='save', directory='saves\\')


def stats():
    print(f'Name:{game.player.name}')
    print(f'HP:[{game.player.hp}/{game.player.mhp}]')
    print(f'MP:[{game.player.mp}/{game.player.mmp}]')


stats()
