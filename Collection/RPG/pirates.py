import random

from Collection.RPG.attributes import Agile, Sneaky
from Collection.RPG.characters import Character


class Pirate(Agile, Sneaky, Character):

    def pickpocket(self):
        return self.sneaky and (random.randint(0, 1))

