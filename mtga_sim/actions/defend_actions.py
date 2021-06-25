from abc import abstractmethod
from mtga_sim.actions.action import Action


class DefendAction(Action):
    @classmethod
    def number_actions(cls):
        classes = cls.get_subclasses()
        return len([c for c in classes])

    @classmethod
    @abstractmethod
    def create_instances(cls, creature, attacking_manoeuvre):
        pass

    @classmethod
    @abstractmethod
    def is_legal(cls, attacking_action):
        pass


class SomeIllegalAction(DefendAction):
    def __init__(self, *args):
        super().__init__(*args)

    @classmethod
    def action_index(cls):
        return 0

    @staticmethod
    def is_active():
        return False

    @classmethod
    def is_legal(cls, attacking_action):
        return False

    @classmethod
    def create_instances(cls, creature, attacking_manoeuvre):
        actions = list()
        for a in attacking_manoeuvre:
            if cls.is_legal(a):
                actions.append(SomeIllegalAction(creature))

        return actions


class Pass(DefendAction):
    def __init__(self, *args):
        super().__init__(*args)

    @classmethod
    def action_index(cls):
        return 1

    @staticmethod
    def is_active():
        return False

    @classmethod
    def is_legal(cls, attacking_action):
        return True

    @classmethod
    def create_instances(cls, creature, attacking_manoeuvre):
        return [Pass(creature)]


class Defend(DefendAction):
    def __init__(self, *args, referenced_id):
        super().__init__(*args)
        self.referenced_id = referenced_id

    @classmethod
    def action_index(cls):
        return 2

    @staticmethod
    def is_active():
        return True

    @classmethod
    def is_legal(cls, attacking_action):
        return True

    @classmethod
    def create_instances(cls, creature, attacking_manoeuvre):
        actions = list()
        for a in attacking_manoeuvre:
            if str(a) == 'Attack' and cls.is_legal(a):
                actions.append(Defend(creature, referenced_id=a.id))
        return actions
