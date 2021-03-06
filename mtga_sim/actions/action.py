import abc
import sys
import inspect
import uuid


class Action(abc.ABC):
    def __init__(self, creature):
        self.creature = creature
        self.legal = False
        self.id = uuid.uuid4()

    @classmethod
    @abc.abstractmethod
    def action_index(cls):
        pass

    def __hash__(self):
        return hash(self.id)

    @staticmethod
    @abc.abstractmethod
    def is_active():
        pass

    @property
    def power(self):
        return self.creature.power

    @property
    def toughness(self):
        return self.creature.toughness

    @classmethod
    @abc.abstractmethod
    def number_actions(cls):
        pass

    @classmethod
    def get_subclasses(cls):
        ret = list()
        """Yield the classes in module ``mod`` that inherit from ``cls``"""
        current_module = sys.modules[cls.__module__]
        for name, obj in inspect.getmembers(current_module):
            if inspect.isclass(obj) and issubclass(obj, cls) and obj != cls:
                ret.append(obj)

        return ret

    def __repr__(self):
        return self.__class__.__name__

    @classmethod
    def instantiate(cls, action_number, creature):
        for clazz in cls.get_subclasses():
            if clazz.action_index() == action_number:
                return clazz(creature)

        raise AssertionError("No class instance was found")
