import pickle
import colorama
from os import system, name
from colorama import Fore, Back, Style
import random

colorama.init()

# Note: Please find a way to move high priority functions to game files because
# having them in util is messy and strange

# HIGH PRIORITY
world_seed = "3301"


def status(game, env_list):
    print(f"Location: {game.location.coordinates}")
    print(
        f"Time: {game.clock.time} Weather: {game.location.get_temperature(game.clock.time)}"
    )
    print(f"Seed: {game.dynamic_seed()}")
    print(f'Place: {game.location.generate_choice(list(env_list.values()))}')


def dynamic_seed(coordinates, time=False, seed=None):
    if not seed:
        seed = world_seed

    seed = str(seed) + str(coordinates[0]) + str(coordinates[1])

    if time is not False:
        seed += str(time)
    return seed


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def add_to(dict_):
    def decorate(class_):
        dict_[class_.__name__] = class_

    return decorate

# TESTING AND DATA MANIPULATION


def save(content, filename="save", directory="..\\saves\\", saves=".sav"):
    with open(directory + filename + saves, "wb") as f:
        pickle.dump(content, f, pickle.HIGHEST_PROTOCOL)


def load(filename="save", directory="..\\saves\\", saves=".sav"):
    with open(directory + filename + saves, "rb") as f:
        content = pickle.load(f)
    return content


# EASE OF LIFE AND EXPERIMENTAL
variables = {
    "colors": {  # colors for coloroma -- #print('{fore[yellow]}{back[magenta]} lol {reset}'.format(**variables['colors']))
        "fore": {
            "black": Fore.BLACK,
            "green": Fore.GREEN,
            "yellow": Fore.YELLOW,
            "red": Fore.RED,
            "blue": Fore.BLUE,
            "magenta": Fore.MAGENTA,
            "cyan": Fore.CYAN,
            "white": Fore.WHITE,
            "reset": Style.RESET_ALL,
        },
        "back": {
            "black": Back.BLACK,
            "green": Back.GREEN,
            "yellow": Back.YELLOW,
            "red": Back.RED,
            "blue": Back.BLUE,
            "magenta": Back.MAGENTA,
            "cyan": Back.CYAN,
            "white": Back.WHITE,
            "reset": Style.RESET_ALL,
        },
        "reset": Style.RESET_ALL,
    },
}


def get_temperature(
    coordinates,
    time,
    options=["Hot", "Warm", "Pleasant", "Chilly", "Rainy", "Cold", "Frigid"],
):
    random.seed(f"{coordinates[0]}{coordinates[1]}{time}")
    return random.choice(options)


text_interface = {"divider": "-" * 90}


def heal_buff(heal, player):
    return int((heal * player.mhp * 0.001) + player.vit * 0.1)


def mana_buff(heal, player):
    return int((heal * player.mmp * 0.001) + player.int * 0.1)
