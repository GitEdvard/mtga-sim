from abc import abstractmethod
from mtga_sim.actions.attack_actions import AttackAction
from mtga_sim.actions.defend_actions import DefendAction


class ManoeuvreSpaceBase(object):
    def __init__(self, troop):
        self.troop = troop
        self.space = dict()

    def __getitem__(self, item):
        return self.space[item]

    def number_actions_for(self, creature):
        return len(self[creature])

    def number_nodes(self):
        return sum([len(self.space[key]) for key in self.space])

    @abstractmethod
    def build(self):
        pass


class DefendManoeuvreSpace(ManoeuvreSpaceBase):
    """
    All possible actions for a troop at a single round.
    Could be either defend och attacking mode.
    """
    def __init__(self, troop, attacking_manoeuvre):
        super().__init__(troop)
        self.attacking_manoeuvre = attacking_manoeuvre
        self.build()

    def build(self):
        for creature in self.troop:
            actions = list()
            for clazz in DefendAction.get_subclasses():
                actions.extend(clazz.create_instances(creature, self.attacking_manoeuvre))

            self.space[creature] = actions


class AttackManoeuvreSpace(ManoeuvreSpaceBase):
    def __init__(self, troop):
        super().__init__(troop)
        self.build()

    def build(self):
        for creature in self.troop:
            actions = list()
            for clazz in AttackAction.get_subclasses():
                actions.extend(clazz.create_instances(creature))

            self.space[creature] = actions


class ManoeuvreIterator(object):
    def __init__(self, manoeuvre_space):
        self.manoeuvre_space = manoeuvre_space
        self.creature_iterator = None
        self.current_key = None
        self.current_state = None
        self.gen = None

    def __iter__(self):
        self.creature_iterator = iter(self.manoeuvre_space.space)
        self.current_state = None
        self.gen = self.increment_rec(self.manoeuvre_space.space, [])
        return self

    def __len__(self):
        return len([i for i in self])

    def __next__(self):
        return next(self.gen)

    def increment_rec(self, manoeuvre_space, prev_actions):
        try:
            current_key = next(iter(manoeuvre_space))
            next_space = {
                key: manoeuvre_space[key]
                for key in manoeuvre_space if not key == current_key
            }
        except StopIteration:
            yield prev_actions
            return

        for action in manoeuvre_space[current_key]:
            yield from self.increment_rec(next_space, prev_actions + [action])


class CombinedManoeuvreIterator(object):
    def __init__(self, troop_a, troop_b):
        self.troop_a = troop_a
        self.troop_b = troop_b
        self.gen = None

    def __iter__(self):
        self.gen = self.increment()
        return self

    def __next__(self):
        return next(self.gen)

    def increment(self):
        attack_space = AttackManoeuvreSpace(self.troop_a)
        attack_it = ManoeuvreIterator(attack_space)
        for attack_manoeuvre in attack_it:
            defend_space = DefendManoeuvreSpace(self.troop_b, attack_manoeuvre)
            defend_it = ManoeuvreIterator(defend_space)
            for defend_manoeuvre in defend_it:
                yield attack_manoeuvre, defend_manoeuvre
