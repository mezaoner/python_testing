import random

from attributes import Agile, Sneaky
from characters import Character


class Pirate(Agile, Sneaky, Character):

    def pickpocket(self):
        return self.sneaky and (random.randint(0, 1))

