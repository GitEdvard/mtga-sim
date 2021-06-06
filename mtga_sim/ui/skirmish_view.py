from mtga_sim.troop import Troop


class SkirmishView(object):
    UPWARD_ARROW = '\u2191'

    def __init__(self, skirmish, padding_str=None):
        self.skirmish = skirmish
        if not padding_str:
            padding_str = " "
        self.padding_str = padding_str

    @property
    def width(self):
        return max(self._attacker_len, self._defender_len)

    @property
    def defender_string(self):
        padding_cand = self.width - self._defender_len
        padding = padding_cand if padding_cand > 0 else 0
        return "{}{}".format(self._defender_troop, self.padding_str * padding)

    @property
    def attacker_string(self):
        padding_cand = self.width - self._attacker_len
        padding = padding_cand if padding_cand > 0 else 0
        return "{}{}".format(self._attacker_creature, self.padding_str * padding)

    @property
    def attack_arrows_string(self):
        padding_cand = self.width - 1
        padding = padding_cand if padding_cand > 0 else 0
        return "{}{}".format(self.UPWARD_ARROW, self.padding_str * padding)

    @property
    def _defender_len(self):
        return len(str(self._defender_troop))

    @property
    def _attacker_len(self):
        return len(str(self._attacker_creature))

    @property
    def _attacker_creature(self):
        return self.skirmish.attacker.creature

    @property
    def _defender_troop(self):
        return Troop([d.creature for d in self.skirmish.defenders])
