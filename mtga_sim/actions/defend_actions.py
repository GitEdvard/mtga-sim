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


class SomeIllegalAction(DefendAction):
    def __init__(self, *args):
        super().__init__(*args)
        self.legal = False

    @classmethod
    def action_index(cls):
        return 0

    @classmethod
    def create_instances(cls, creature, attacking_manoeuvre):
        return [SomeIllegalAction(creature)]


class Pass(DefendAction):
    def __init__(self, *args):
        super().__init__(*args)
        self.legal = True

    @classmethod
    def action_index(cls):
        return 1

    @classmethod
    def create_instances(cls, creature, attacking_manoeuvre):
        return [Pass(creature)]


class Defend(DefendAction):
    def __init__(self, *args):
        super().__init__(*args)
        self.legal = True

    @classmethod
    def action_index(cls):
        return 2

    @classmethod
    def create_instances(cls, creature, attacking_manoeuvre):
        actions = list()
        for a in attacking_manoeuvre:
            if str(a) == 'Attack':
                actions.append(Defend(creature))
        return actions
