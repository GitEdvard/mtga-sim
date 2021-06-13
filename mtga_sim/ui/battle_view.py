class BattleView(object):
    def __init__(self, battle_model):
        self.battle_model = battle_model

    def render(self):
        print(self.battle_model.defend_string)
        print(self.battle_model.attack_arrows_string)
        print(self.battle_model.attack_string)
