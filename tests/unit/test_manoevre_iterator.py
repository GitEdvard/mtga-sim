import pytest
from mtga_sim.troop import Troop, Creature
from mtga_sim.manoeuvre_iterator import ManoeuvreIterator


class TestManoeuvreIterator(object):
    def test_troop_of_1__number_permutations_is_2(self):
        creature = Creature(2, 2)
        troop = Troop([creature])
        m = ManoeuvreIterator(troop)
        assert len(m) == 2

    @pytest.mark.now
    def test_troop_of_2__number_permutations_is_4(self):
        creature1 = Creature(2, 2)
        creature2 = Creature(2, 2)
        troop = Troop([creature1, creature2])
        strats = ManoeuvreIterator(troop)
        # from pprint import pprint
        # pprint([s for s in strats])
        assert len(strats) == 4

    def test_troop_of_3__number_permutations_is_8(self):
        creature1 = Creature(2, 2)
        creature2 = Creature(2, 2)
        creature3 = Creature(2, 2)
        troop = Troop([creature1, creature2, creature3])
        m = ManoeuvreIterator(troop)
        assert len(m) == 8
