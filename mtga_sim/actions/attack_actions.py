from mtga_sim.actions.action import Action


class AttackAction(Action):
    @classmethod
    def number_actions(cls):
        classes = cls.get_subclasses()
        return len([c for c in classes])

    @property
    def is_legal(self):
        return self.legal


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
