class Manoeuvre(object):
    """
    An action performed by a troop as one unit.
    Consists of a number of actions
    """
    def __init__(self, actions):
        self.actions = actions
        self.cache = {a.id: a for a in actions}

    def __getitem__(self, item):
        return self.actions[item]

    def get_by(self, id):
        return self.cache[id]

    def __hash__(self):
        return hash(a.id for a in self.actions)
