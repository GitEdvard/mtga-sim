import abc


ACTION_ATTACK = "attack"
ACTION_PASS = "pass"
ACTION_DEFEND = "defend"


class Action(abc.ABC):
    def __init__(self, creature):
        self.creature = creature

    @abc.abstractmethod
    def is_legal(self):
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

    def is_legal(self):
        return True


class Pass(Action):
    def action(self):
        return ACTION_PASS

    def is_legal(self):
        return True


class Defend(Action):
    def action(self):
        return ACTION_DEFEND

    def is_legal(self):
        return False
