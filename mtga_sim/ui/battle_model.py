from mtga_sim.ui.passive_model import PassiveModel
from mtga_sim.ui.skirmish_model import SkirmishModel


class BattleModel(object):
    SKIRMISH_MARGIN_LENGTH = 2
    PASSIVE_MARGIN_LENGTH = 1
    LONG_MARGIN = 4

    def __init__(self, battle, padding_str=None):
        if not padding_str:
            padding_str = " "
        self.padding_str = padding_str
        self.skirmish_margin = self.padding_str * self.SKIRMISH_MARGIN_LENGTH
        self.passive_margin = self.padding_str * self.PASSIVE_MARGIN_LENGTH
        self.long_margin = self.padding_str * self.LONG_MARGIN
        self.skirmish_models = [
            SkirmishModel(skirmish, padding_str=padding_str)
            for skirmish in battle.skirmishes
        ]
        self.offensive_passive_models = [
            PassiveModel(a) for a in battle.offensive_passives
        ]
        self.defensive_passive_models = [
            PassiveModel(d) for d in battle.defensive_passives
        ]

    @property
    def defend_string(self):
        active_defenders = self.skirmish_margin.join(
            [view.defender_string for view in self.skirmish_models]
        )
        passive_defenders = self.passive_margin.join(
            [str(p) for p in self.defensive_passive_models]
        )
        defend_row = self.long_margin.join([active_defenders, passive_defenders])
        return defend_row

    @property
    def attack_string(self):
        attackers = self.skirmish_margin.join(
            [view.attacker_string for view in self.skirmish_models]
        )
        passives = self.passive_margin.join(
            [str(p) for p in self.offensive_passive_models]
        )
        offensive_row = self.long_margin.join([attackers, passives])
        return offensive_row

    @property
    def attack_arrows_string(self):
        margin = self.padding_str * self.SKIRMISH_MARGIN_LENGTH
        return margin.join([view.attack_arrows_string for view in self.skirmish_models])
