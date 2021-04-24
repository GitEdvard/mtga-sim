import pytest
from mtga_sim.manoeuvres.manoeuvre_iterator import DefendManoeuvreSpace
from mtga_sim.troop import Troop
from tests.unit.test_base import TestBase


class TestManoeuvreSpace(TestBase):
    def test_number_defend_actions_for_1_attacking(self):
        creatures = self.create_standard_creatues(1)
        attacking_manoeuvre = self.attack_with(creatures)
        troop = Troop(creatures)
        manoeuvre_space = DefendManoeuvreSpace(troop, attacking_manoeuvre)
        manoeuvre_space.build()
        assert manoeuvre_space.number_actions_for(creatures[0]) == 3
