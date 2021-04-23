from mtga_sim.creature_action import Attack, Pass, Defend
from mtga_sim.creature_action import Action


class ManoeuvreIterator(object):
    """
    Can iterate over all possible troop actions for one player during one turn
    """
    def __init__(self, troop):
        self.troop = troop
        self.permutation_array = None
        self.troop_pointer = None
        self.first = None

    @property
    def permutation_start_array(self):
        return [0] * len(self.troop)

    def __iter__(self):
        self.first = True
        self.permutation_array = self.permutation_start_array
        self.troop_pointer = len(self.permutation_array) - 1
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
        next_trial_action_number = self.permutation_array[troop_pointer] + 1
        self.permutation_array[troop_pointer] = next_trial_action_number
        action = None
        if next_trial_action_number < Action.number_actions():
            action = Action.instantiate(next_trial_action_number, self.troop[troop_pointer])
        else:
            # Current rank is at max number, go to next rank and reset current
            self.permutation_array[troop_pointer] = 0
            self.increment_rec(troop_pointer - 1)
        if action is not None and not action.is_legal():
            # Continue count at current rank
            self.increment_rec(troop_pointer)

    def convert(self):
        action_arr = list()
        for idx, p in enumerate(self.permutation_array):
            action = Action.instantiate(p, self.troop[idx])
            action_arr.append(action)

        return action_arr
