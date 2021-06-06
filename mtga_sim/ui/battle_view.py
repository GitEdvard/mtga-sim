from mtga_sim.ui.skirmish_view import SkirmishView


class BattleView(object):
    SKIRMISH_MARGIN_LENGTH = 1

    def __init__(self, battle):
        self.battle = battle
        self.skirmish_views = [
            SkirmishView(skirmish) for skirmish in battle.skirmishes
        ]

    @property
    def defend_string(self):
        margin = " " * self.SKIRMISH_MARGIN_LENGTH
        return margin.join([view.defender_string for view in self.skirmish_views])

    @property
    def attack_string(self):
        margin = " " * self.SKIRMISH_MARGIN_LENGTH
        return margin.join([view.attacker_string for view in self.skirmish_views])
