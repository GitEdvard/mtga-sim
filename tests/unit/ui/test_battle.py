from mtga_sim.battle import Battle
from mtga_sim.ui.battle_model import BattleModel
from mtga_sim.ui.skirmish_model import SkirmishModel
from tests.unit.test_base import TestBase


class TestBattle(TestBase):
    def _create_battle(self):
        attacking_creatures = self.create_standard_creatues(2)
        defending_creatures = self.create_standard_creatues(2)
        offensive_manoeuvre = self.attack_with(attacking_creatures)
        defensive_manoeuvre = self.defend_first_with(defending_creatures, offensive_manoeuvre)
        battle = Battle(offensive_manoeuvre, defensive_manoeuvre)
        battle.create_skirmishes()
        return battle

    def test_defend_string_for_two_skirmishes(self):
        battle = self._create_battle()

        # Act
        battle_model = BattleModel(battle, padding_str="+")

        # Assert
        assert battle_model.defend_string == '2/2 2/2++++'

    def test_attack_string_for_two_skirmishes(self):
        battle = self._create_battle()

        # Act
        battle_model = BattleModel(battle, padding_str="+")

        # Assert
        assert battle_model.attack_string == '2/2+++++2/2'

    def test_attack_arrow_string_for_two_skirmishes(self):
        battle = self._create_battle()

        # Act
        battle_model = BattleModel(battle, padding_str="+")

        # Assert
        expected = '{}+++++++{}++'.format(SkirmishModel.UPWARD_ARROW, SkirmishModel.UPWARD_ARROW)
        assert battle_model.attack_arrows_string == expected

