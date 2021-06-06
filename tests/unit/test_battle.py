import pytest
from mtga_sim.battle import Battle
from tests.unit.test_base import TestBase


class TestBattle(TestBase):

    def _create_battle(self, creature_count):
        # Arrange defensive manoeuvre
        attacking_creatures = self.create_standard_creatues(creature_count)
        defending_creatures = self.create_standard_creatues(creature_count)
        offensive_manoeuvre = self.attack_with(attacking_creatures)
        defensive_manoeuvre = self.defend_first_with(defending_creatures, offensive_manoeuvre)
        return Battle(offensive_manoeuvre, defensive_manoeuvre)

    def test_1_attacking_1_defending__skirmish_with_1_defending(self):
        # Arrange defensive manoeuvre
        battle = self._create_battle(creature_count=1)

        # Act
        skirmishes = battle.create_skirmishes()

        # Assert
        assert len(skirmishes) == 1

    def test_2_attacking_2_defending__2_skirmishes(self):
        # Arrange defensive manoeuvre
        battle = self._create_battle(creature_count=2)

        # Act
        skirmishes = battle.create_skirmishes()

        # Assert
        assert len(skirmishes) == 2
