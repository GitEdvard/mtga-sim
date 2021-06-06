from mtga_sim.manoeuvres.manoeuvre import Manoeuvre
from mtga_sim.skirmish import Skirmish
from mtga_sim.ui.skirmish_view import SkirmishView
from tests.unit.test_base import TestBase


class TestSkirmishes(TestBase):

    def _create_skirmish_defend_first(self):
        attacking_troop = self.create_standard_troop(1)
        defending_troop = self.create_standard_troop(2)
        attack_manoeuvre = self.attack_with(attacking_troop)
        defend_manoeuvre = self.defend_first_with(defending_troop, attack_manoeuvre)
        return Skirmish(attack_manoeuvre[0], defend_manoeuvre)

    def test_width_of_skrimish(self):
        # Arrange
        skirmish = self._create_skirmish_defend_first()

        # Act
        skirmish_view = SkirmishView(skirmish, padding_str="+")

        # Assert
        assert skirmish_view.width == 7

    def test_defender_string(self):
        # Arrange
        skirmish = self._create_skirmish_defend_first()

        # Act
        skirmish_view = SkirmishView(skirmish, padding_str="+")

        # Assert
        assert skirmish_view.defender_string == "2/2 2/2"

    def test_attacker_string(self):
        # Arrange
        skirmish = self._create_skirmish_defend_first()

        # Act
        skirmish_view = SkirmishView(skirmish, padding_str="+")

        # Assert
        assert skirmish_view.attacker_string == "2/2++++"

    def test_attack_arrow_string(self):
        # Arrange
        skirmish = self._create_skirmish_defend_first()

        # Act
        skirmish_view = SkirmishView(skirmish, padding_str="+")

        # Assert
        assert skirmish_view.attack_arrows_string == "{}++++++".format(SkirmishView.UPWARD_ARROW)

