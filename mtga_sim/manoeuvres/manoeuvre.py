class Manoeuvre(object):
    """
    An action performed by a troop as one unit.
    Consists of a number of actions
    """
    def __init__(self, actions):
        self.actions = actions

    def __getitem__(self, item):
        return self.actions[item]
