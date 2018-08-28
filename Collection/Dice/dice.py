import random


class Die:
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError("Must have atleast 2 sides")
        if not isinstance(sides, int):
            raise ValueError("Sides must be a whole number")
        if not isinstance(value, int):
            raise ValueError("Value must be an whole number")
        if value > sides:
            raise ValueError("Value cannot exceed number of sides")
        self.value = value or random.randint(1, sides)

    def __int__(self):
        return self.value

    def __eq__(self, other):
        return int(self) == other

    def __ne__(self, other):
        return other != int(self)

    def __gt__(self, other):
        return int(self) > other

    def __lt__(self, other):
        return int(self) < other

    def __ge__(self, other):
        return int(self) > other or int(self) == other

    def __le__(self, other):
        return int(self) < other or int(self) == other

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return int(self) + other

    def __repr__(self):
        return str(self.value)


class D6(Die):
    def __init__(self, value = 0):
        super().__init__(sides=6, value=value)