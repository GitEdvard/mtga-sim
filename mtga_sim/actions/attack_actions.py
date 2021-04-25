from abc import abstractmethod
from mtga_sim.actions.action import Action


class AttackAction(Action):
    @classmethod
    def number_actions(cls):
        classes = cls.get_subclasses()
        return len([c for c in classes])

    @property
    def is_legal(self):
        return self.legal

    @classmethod
    @abstractmethod
    def create_instances(cls, creature):
        pass


class SomeIllegalAction(AttackAction):
    def __init__(self, *args):
        super().__init__(*args)
        # TODO: refactor legal behaviour
        self.legal = False

    @classmethod
    def action_index(cls):
        return 0

    @classmethod
    def create_instances(cls, creature):
        return []


class Attack(AttackAction):
    def __init__(self, *args):
        super().__init__(*args)
        self.legal = True

    @classmethod
    def create_instances(cls, creature):
        return [Attack(creature)]

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

    @classmethod
    def create_instances(cls, creature):
        return [Pass(creature)]
