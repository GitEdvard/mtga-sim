from mtga_sim.ui.battle_model import BattleModel
from mtga_sim.ui.battle_view import BattleView


class BattleController(object):
    def __init__(self):
        pass

    def render(self, battle):
        battle_model = BattleModel(battle)
        battle_view = BattleView(battle_model)
        battle_view.render()
