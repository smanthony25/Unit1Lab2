class Rat:
    def __init__(self, sex, weight):
        self.sex = sex
        self.weight = weight
        self.litters = 0

    def __str__(self):
        return f"{self.weight}{self.sex}"

    def __repr__(self):
        return f"{self.weight}{self.sex}"

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __ge__(self, other):
        return self.weight >= other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __radd__(self, other):
        if type(other) is Rat:
            other = other.weight
        return self.weight + other

    def getWeight(self):
        return self.weight

    def getSex(self):
        return self.sex

    def canBreed(self):
        if self.litters > 4:
            return False
        else:
            return True

    def mutuate(self, scale):
        self.weight = round(self.weight * scale)