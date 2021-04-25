import pytest
from mtga_sim.troop import Troop
from mtga_sim.manoeuvres.manoeuvre_iterator import ManoeuvreIterator
from mtga_sim.manoeuvres.manoeuvre_iterator import DefendManoeuvreSpace
from mtga_sim.manoeuvres.manoeuvre import Manoeuvre
from mtga_sim.actions.attack_actions import AttackAction, Attack
from tests.unit.test_base import TestBase


class TestDefendManoeuvres(TestBase):
    def test_troop_of_1__number_permutations_is_1(self):
        creatures = self.create_standard_creatues(1)
        troop = Troop(creatures)
        manoeuvre_space = DefendManoeuvreSpace(troop, [])
        m = ManoeuvreIterator(manoeuvre_space)
        assert len(m) == 1

    def test_response_to_1_attacking__number_actions_is_2(self):
        creatures = self.create_standard_creatues(1)
        troop = Troop(creatures)
        attack_action = AttackAction.instantiate(Attack.action_index(), creatures[0])
        attack_manoeuvre = Manoeuvre([attack_action])
        manoeuvre_space = DefendManoeuvreSpace(troop, attack_manoeuvre)
        m = ManoeuvreIterator(manoeuvre_space)
        assert len(m) == 2

    @pytest.mark.now
    def test_response_to_2_attacking__number_actions_is_9(self):
        # (same creatures attack and defend)
        creatures = self.create_standard_creatues(2)
        troop = Troop(creatures)
        attack_manoeuvre = self.attack_with(creatures)
        manoeuvre_space = DefendManoeuvreSpace(troop, attack_manoeuvre)
        m = ManoeuvreIterator(manoeuvre_space)
        assert len(m) == 9
