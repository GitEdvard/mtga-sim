class Creature(object):

    def __init__(self, power, toughness):
        self.power = power
        self.toughness = toughness

    def __str__(self):
        return "{}/{}".format(self.power, self.toughness)


class Troop(object):
    def __init__(self, creatures=None):
        self.cards = creatures or list()

    def append(self, card):
        self.cards.append(card)

    def __str__(self):
        return " ".join([str(c) for c in self.cards])
