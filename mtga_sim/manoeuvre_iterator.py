import abc
from mtga_sim.actions.attack_actions import AttackAction
from mtga_sim.actions.defend_actions import DefendAction


class ManoeuvreIterator(object):
    """
    Can iterate over all possible troop actions for one player during one turn
    """
    def __init__(self, troop):
        self.troop = troop
        self.permutation_array = None
        self.first = None

    @property
    def permutation_start_array(self):
        start_arr = [0] * len(self.troop)
        for i in range(len(self.troop)):
            start_arr[i] = self.first_legal_action_index(i)

        return start_arr

    def __iter__(self):
        self.first = True
        self.permutation_array = self.permutation_start_array
        return self

    def __len__(self):
        return len([p for p in self])

    def __next__(self):
        if self.first is True:
            self.first = False
        else:
            self.increment()
        return self.convert()

    def increment(self):
        troop_pointer = len(self.permutation_array) - 1
        self.increment_rec(troop_pointer)

    def increment_rec(self, troop_pointer):
        # Increment lowest rank that are less than max
        if troop_pointer < 0:
            raise StopIteration
        trial_idx = self.permutation_array[troop_pointer] + 1
        self.permutation_array[troop_pointer] = trial_idx
        action = None
        if trial_idx < self.number_actions():
            action = self.instantiate_action(trial_idx, self.troop[troop_pointer])
        else:
            # Current rank is at max number, go to next rank and reset current
            self.permutation_array[troop_pointer] = \
                self.first_legal_action_index(troop_pointer)
            self.increment_rec(troop_pointer - 1)
        if action is not None and not action.is_legal:
            # Continue count at current rank
            self.increment_rec(troop_pointer)

    def first_legal_action_index(self, troop_pointer):
        creature = self.troop[troop_pointer]
        for i in range(self.number_actions()):
            action = self.instantiate_action(i, creature)
            if action.is_legal:
                return i
        return self.number_actions()

    def convert(self):
        action_arr = list()
        for idx, p in enumerate(self.permutation_array):
            action = self.instantiate_action(p, self.troop[idx])
            action_arr.append(action)

        return action_arr

    @abc.abstractmethod
    def instantiate_action(self, action_number, creature):
        pass

    @abc.abstractmethod
    def number_actions(self):
        pass


class AttackManoeuvreIterator(ManoeuvreIterator):
    def instantiate_action(self, action_number, creature):
        return AttackAction.instantiate(action_number, creature)

    def number_actions(self):
        return AttackAction.number_actions()


class DefendManoeuvreIterator(ManoeuvreIterator):
    def __init__(self, troop, attacking_manoeuvre):
        super().__init__(troop)
        self.attacking_manoeuvre = attacking_manoeuvre

    def instantiate_action(self, action_number, creature):
        return DefendAction.instantiate(action_number, creature)

    def number_actions(self):
        return DefendAction.number_actions()
