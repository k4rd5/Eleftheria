import random


def choose_environment(game):
    random.seed(game.dynamic_seed(time=False))
    environments = list(game.data.environments.list_)
    return random.choice(environments)()
