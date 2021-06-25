class PassiveModel(object):
    """
    String representation of a passive attacker or defender.
    """
    def __init__(self, passive_action):
        self.passive_action = passive_action

    def __str__(self):
        return str(self.passive_action.creature)
