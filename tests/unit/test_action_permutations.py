import pytest
from mtga_sim.troop import Troop, Creature
from mtga_sim.manoeuvre_space import ManoeuvreSpace


class TestActionPermutations(object):
    def test_troup_of_1__number_permutations_is_2(self):
        creature = Creature(2, 2)
        troop = Troop([creature])
        m = ManoeuvreSpace(troop)
        assert len(m) == 2
