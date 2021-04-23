import abc
import sys
import inspect

CURRENT_MODULE = sys.modules[__name__]


class Action(abc.ABC):
    def __init__(self, creature):
        self.creature = creature
        self.legal = False

    @classmethod
    @abc.abstractmethod
    def action_index(cls):
        pass

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

    def __repr__(self):
        return self.__class__.__name__

    @classmethod
    def instantiate(cls, action_number, creature):
        for clazz in cls._get_subclasses():
            if clazz.action_index() == action_number:
                return clazz(creature)


class AttackAction(Action):
    pass


class SomeIllegalAction(AttackAction):
    def __init__(self, *args):
        super().__init__(*args)
        self.legal = False

    @classmethod
    def action_index(cls):
        return 0


class Attack(AttackAction):
    def __init__(self, *args):
        super().__init__(*args)
        self.legal = True

    @classmethod
    def action_index(cls):
        return 1


class Pass(AttackAction):
    def __init__(self, *args):
        super().__init__(*args)
        self.legal = True

    @classmethod
    def action_index(cls):
        return 2
