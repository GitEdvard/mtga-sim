import pytest
from mtga_sim.troop import Troop
from mtga_sim.manoeuvres.manoeuvre_iterator import ManoeuvreIterator
from mtga_sim.manoeuvres.manoeuvre_iterator import AttackManoeuvreSpace
from mtga_sim.actions.attack_actions import Attack, Pass
from tests.unit.test_base import TestBase


class TestManoeuvreIterator(TestBase):
    def test_troop_of_1__number_permutations_is_2(self):
        creatures = self.create_standard_creatues(1)
        troop = Troop(creatures)
        manoeuvre_space = AttackManoeuvreSpace(troop)
        manoeuvre_iterator = ManoeuvreIterator(manoeuvre_space)
        assert len(manoeuvre_iterator) == 2

    def test_troop_of_2__with_first_action_illegal__number_permutations_is_4(self):
        creatures = self.create_standard_creatues(2)
        troop = Troop(creatures)
        manoeuvre_space = AttackManoeuvreSpace(troop)
        strats = ManoeuvreIterator(manoeuvre_space)
        assert len(strats) == 4

    def test_troop_of_3__number_permutations_is_8(self):
        creatures = self.create_standard_creatues(3)
        troop = Troop(creatures)
        manoeuvre_space = AttackManoeuvreSpace(troop)
        m = ManoeuvreIterator(manoeuvre_space)
        assert len(m) == 8

    def test_convert_first_iteration(self):
        creatures = self.create_standard_creatues(1)
        troop = Troop(creatures)
        manoeuvre_space = AttackManoeuvreSpace(troop)
        m = ManoeuvreIterator(manoeuvre_space)
        # start iteration and stop at first value
        iter(m)
        manoeuvre = next(m)
        assert isinstance(manoeuvre[0], Attack)

    @pytest.mark.now
    def test_convert_second_iteration(self):
        creatures = self.create_standard_creatues(1)
        troop = Troop(creatures)
        manoeuvre_space = AttackManoeuvreSpace(troop)
        m = ManoeuvreIterator(manoeuvre_space)
        # stop iteration at second value
        iter(m)
        next(m)
        manoeuvre = next(m)
        print(manoeuvre)
        assert isinstance(manoeuvre[0], Pass)
