import uuid


class Creature(object):

    def __init__(self, power, toughness):
        self.power = power
        self.toughness = toughness
        self.id = uuid.uuid4()

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return "{}/{}".format(self.power, self.toughness)


class Troop(object):
    def __init__(self, creatures=None):
        self.creatures = creatures or list()
        self.counter = None

    def append(self, card):
        self.creatures.append(card)

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < len(self.creatures):
            ret = self.creatures[self.counter]
            self.counter += 1
            return ret
        else:
            raise StopIteration

    def __len__(self):
        return len(self.creatures)

    def __getitem__(self, ind):
        return self.creatures[ind]

    def __str__(self):
        return " ".join([str(c) for c in self.creatures])
