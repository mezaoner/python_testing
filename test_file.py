class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern


    def __str__(self):
        output = ""
        for attr in self.pattern:
            if attr == ".":
                output += "dot"
            if attr == "_":
                output += "dash"
            output += "-"
        return output[:-1]