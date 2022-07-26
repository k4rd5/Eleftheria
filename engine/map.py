# movement.py

import random
from .util import dynamic_seed
from .mechanism import choose_environment


class Map:
    def __init__(self, seed=None, coordinates=[0, 0]):
        self.seed = seed or random.seed()
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.unit = 1

    @property
    def coordinates(self):
        return (self.x, self.y)

    def move(self, direction, steps=1):
        if direction == 0:  # a
            self.x -= steps * self.unit
        elif direction == 1:  # d
            self.x += steps * self.unit
        elif direction == 2:  # w
            self.y += steps * self.unit
        elif direction == 3:  # s
            self.y -= steps * self.unit

    def set_location(self, location):
        self.x = location[0]
        self.y = location[1]

    def generate_choice(self, list_, coordinates=None):
        if not coordinates:
            coordinates = self.coordinates
        random.seed(dynamic_seed(coordinates, seed=self.seed))
        return random.choice(list_)

    def get_temperature(
        self,
        time,
        coordinates=None,
        options=["Hot", "Warm", "Pleasant", "Chilly", "Rainy", "Cold", "Frigid"],
    ):
        if not coordinates:
            coordinates = self.coordinates
        random.seed(dynamic_seed(coordinates, seed=self.seed, time=time))
        return random.choice(options)

    # death
    def display(
        self,
        list_,
        radius=5,
    ):

        offsets = [
            [(x, y) for x in range(-radius, radius + 1)]
            for y in range(-radius, radius + 1)
        ]
        coordinates = self.coordinates
        offsets.reverse()
        for row in offsets:
            for offset in row:
                print(
                    self.generate_choice(
                        list_,
                        coordinates=(
                            coordinates[0] + offset[0],
                            coordinates[1] + offset[1],
                        ),
                    ),
                    end=" ",
                )
            print()
