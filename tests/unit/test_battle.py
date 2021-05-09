import pytest
from mtga_sim.battle import Battle
from tests.unit.test_base import TestBase


class TestBattle(TestBase):
    def test_1_attacking_1_defending__skirmish_with_1_defending(self):
        # Arrange defensive manoeuvre
        attacking_creatures = self.create_standard_creatues(1)
        defending_creatures = self.create_standard_creatues(1)
        offensive_manoeuvre = self.attack_with(attacking_creatures)
        defensive_manoeuvre = self.defend_first_with(defending_creatures, offensive_manoeuvre)
        battle = Battle(offensive_manoeuvre, defensive_manoeuvre)

        # Act
        skirmishes = battle.create_skirmishes()

        # Assert
        assert len(skirmishes) == 1
