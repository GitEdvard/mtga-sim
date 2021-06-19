from mtga_sim.ui.passive_model import PassiveModel
from mtga_sim.ui.skirmish_model import SkirmishModel


class BattleModel(object):
    SKIRMISH_MARGIN_LENGTH = 1

    def __init__(self, battle, padding_str=None):
        if not padding_str:
            padding_str = " "
        self.padding_str = padding_str
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
        margin = self.padding_str * self.SKIRMISH_MARGIN_LENGTH
        active_defenders = [view.defender_string for view in self.skirmish_models]
        passive_defenders = [str(p) for p in self.defensive_passive_models]
        defend_row = active_defenders + passive_defenders
        return margin.join(defend_row)

    @property
    def attack_string(self):
        margin = self.padding_str * self.SKIRMISH_MARGIN_LENGTH
        attackers = [view.attacker_string for view in self.skirmish_models]
        passives = [str(p) for p in self.offensive_passive_models]
        return margin.join(attackers + passives)

    @property
    def attack_arrows_string(self):
        margin = self.padding_str * self.SKIRMISH_MARGIN_LENGTH
        return margin.join([view.attack_arrows_string for view in self.skirmish_models])
