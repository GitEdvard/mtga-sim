import abc


ACTION_ATTACK = "attack"
ACTION_PASS = "pass"
ACTION_DEFEND = "defend"


class Action(abc.ABC):
    def __init__(self, creature):
        self.creature = creature

    @abc.abstractmethod
    @property
    def action(self):
        pass

    @property
    def power(self):
        return self.creature.power

    @property
    def toughness(self):
        return self.creature.toughness


class Attack(Action):
    def action(self):
        return ACTION_ATTACK


class Pass(Action):
    def action(self):
        return ACTION_PASS


class Defend(Action):
    def action(self):
        return ACTION_DEFEND
