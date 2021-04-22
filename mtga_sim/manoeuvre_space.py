from mtga_sim.creature_action import Attack, Pass, Defend


class ManoeuvreSpace(object):
    """
    Can iterate over all possible troop actions for one player during one turn
    """
    def __init__(self, troop):
        self.troop = troop
        self.permutation_array = None
        self.troop_pointer = None

    @property
    def permutation_start_array(self):
        return [0] * len(self.troop)

    def __iter__(self):
        self.permutation_array = self.permutation_start_array
        self.troop_pointer = len(self.permutation_array) - 1
        return self

    def __len__(self):
        return len([p for p in self])

    def __next__(self):
        if self.permutation_array[self.troop_pointer] >= 3:
            self.troop_pointer -= 1
        if self.troop_pointer < 0:
            raise StopIteration
        self.increment_rec()
        return self.convert()

    def increment_rec(self):
        self.permutation_array[self.troop_pointer] += 1
        next_trial_action_number = self.permutation_array[self.troop_pointer]
        action = None
        if next_trial_action_number < 3:
            action = self.get_action(next_trial_action_number)
        if action is not None and not action.is_legal():
            self.increment_rec()

    def convert(self):
        action_arr = list()
        for idx, p in enumerate(self.permutation_array):
            action = self.get_action(idx)
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
