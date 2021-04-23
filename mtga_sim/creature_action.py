import abc
import sys
import inspect

CURRENT_MODULE = sys.modules[__name__]
ACTION_ATTACK = "attack"
ACTION_PASS = "pass"
ACTION_DEFEND = "defend"


class Action(abc.ABC):
    def __init__(self, creature):
        self.creature = creature

    @property
    def power(self):
        return self.creature.power

    @property
    def toughness(self):
        return self.creature.toughness

    @classmethod
    def number_actions(cls):
        classes = cls._get_subclasses()
        return len([c for c in classes])

    @property
    def is_legal(self):
        return self.legal

    @classmethod
    def _get_subclasses(cls):
        ret = list()
        """Yield the classes in module ``mod`` that inherit from ``cls``"""
        for name, obj in inspect.getmembers(CURRENT_MODULE):
            if inspect.isclass(obj) and issubclass(obj, cls) and obj != cls:
                ret.append(obj)

        return ret

    @staticmethod
    def instantiate(action_number, creature):
        action = None
        if action_number == 0:
            action = Defend(creature)
        if action_number == 1:
            action = Attack(creature)
        if action_number == 2:
            action = Pass(creature)

        return action

    def __repr__(self):
        return self.__class__.__name__


class Attack(Action):
    def __init__(self, *args):
        super().__init__(*args)
        self.legal = True

    def action(self):
        return ACTION_ATTACK


class Pass(Action):
    def __init__(self, *args):
        super().__init__(*args)
        self.legal = True

    def action(self):
        return ACTION_PASS


class Defend(Action):
    def __init__(self, *args):
        super().__init__(*args)
        self.legal = False

    def action(self):
        return ACTION_DEFEND
