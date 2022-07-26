from engine.environment import Environment
from engine.util import text_interface


class Tavern(Environment):
    name = "Tavern"

    def on_entry(self):
        print("you have entered the Tavern")


class Market(Environment):
    name = "Market"

    def on_entry(self):
        print("you have entered the Market")


class Library(Environment):
    name = "Library"

    def on_entry(self):
        print("you have entered the Library")


class TownHall(Environment):
    name = "Townhill"

    def on_entry(self):
        print("you have entered the Town Hall")


class Town(Environment):
    def __init__(
        self,
        name=None,
        information="No information available.",
        special_coord=(0, 0),
        npcs=[],
        monsters=[],
        loot=[],
    ):
        self.name = name
        self.information = information
        self.special_coordinates = special_coord
        self.sub_env = {"T": Tavern, "M": Market, "L": Library, "H": TownHall}
        self.npcs = npcs
        self.loot = loot
        self.monsters = monsters

    def on_entry(self, player):
        self.inside = True
        print(
            f"You have entered a town{[(a:=f' called, {self.name}') if self.name else (a:='')][0]}! \n"
        )
        self.main_menu(player)

    def main_menu(self, player):
        while self.inside:
            print(text_interface["divider"])
            [print(self.name) if self.name else print("Town")]
            print(text_interface["divider"])
            [
                print(f"[{identifier}] {env.name} -- {env.information}")
                for identifier, env in self.sub_env.items()
            ]
            print("[X] Exit")
            print(text_interface["divider"])
            choice = input("> ").strip().lower()
            for identifier in self.sub_env.keys():
                if choice == identifier.strip().lower():
                    self.sub_env[identifier].on_entry(player)

            if choice == "x":
                self.inside = False
                self.on_exit(player)

    def on_exit(self, player):
        # doesnt remove current location because we need to keep
        # the previous location saved instead of setting the value to None

        pass
