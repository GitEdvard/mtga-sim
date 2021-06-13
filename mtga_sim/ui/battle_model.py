from mtga_sim.ui.skirmish_model import SkirmishModel


class BattleModel(object):
    SKIRMISH_MARGIN_LENGTH = 1

    def __init__(self, battle, padding_str=None):
        self.battle = battle
        if not padding_str:
            padding_str = " "
        self.padding_str = padding_str
        self.skirmish_views = [
            SkirmishModel(skirmish, padding_str=padding_str)
            for skirmish in battle.skirmishes
        ]

    @property
    def defend_string(self):
        margin = self.padding_str * self.SKIRMISH_MARGIN_LENGTH
        return margin.join([view.defender_string for view in self.skirmish_views])

    @property
    def attack_string(self):
        margin = self.padding_str * self.SKIRMISH_MARGIN_LENGTH
        return margin.join([view.attacker_string for view in self.skirmish_views])

    @property
    def attack_arrows_string(self):
        margin = self.padding_str * self.SKIRMISH_MARGIN_LENGTH
        return margin.join([view.attack_arrows_string for view in self.skirmish_views])
