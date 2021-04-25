import pytest
from tests.unit.test_base import TestBase
from mtga_sim.manoeuvres.manoeuvre_iterator import AttackManoeuvreSpace
from mtga_sim.troop import Troop, Creature


class TestAttackManoeuvreSpace(TestBase):
    def test_number_attack_actions_for_1_creature(self):
        creatures = self.create_standard_creatues(1)
        troop = Troop(creatures)
        manoeuvre_space = AttackManoeuvreSpace(troop)
        manoeuvre_space.build()
        assert manoeuvre_space.number_actions_for(creatures[0]) == 2

    def test_number_attack_actions_for_3_creatures(self):
        creatures = self.create_standard_creatues(3)
        troop = Troop(creatures)
        manoeuvre_space = AttackManoeuvreSpace(troop)
        manoeuvre_space.build()
        assert manoeuvre_space.number_nodes() == 6
