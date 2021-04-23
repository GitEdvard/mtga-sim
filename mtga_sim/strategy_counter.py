from mtga_sim.creature_action import Attack, Pass, Defend


class StrategyCounter(object):
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
        if next_trial_action_number < 3:
            action = self.get_action(next_trial_action_number)
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
            action = self.get_action(p)
            action_arr.append(action)

        return action_arr

    def get_action(self, action_number):
        action = None
        if action_number == 0:
            action = Attack(self.troop[self.troop_pointer])
        if action_number == 1:
            action = Pass(self.troop[self.troop_pointer])
        if action_number == 2:
            action = Defend(self.troop[self.troop_pointer])

        return action
