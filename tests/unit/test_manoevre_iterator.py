import pytest
from mtga_sim.troop import Troop, Creature
from mtga_sim.manoeuvre_iterator import ManoeuvreIterator
from mtga_sim.attack_actions import Attack, Pass


class TestManoeuvreIterator(object):
    def test_troop_of_1__number_permutations_is_2(self):
        creature = Creature(2, 2)
        troop = Troop([creature])
        m = ManoeuvreIterator(troop)
        assert len(m) == 2

    def test_troop_of_2__with_first_action_illegal__number_permutations_is_4(self):
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

    def test_convert_first_iteration(self):
        creature = Creature(2, 2)
        troop = Troop([creature])
        m = ManoeuvreIterator(troop)
        # start iteration and stop at first value
        iter(m)
        next(m)
        actions = m.convert()
        assert isinstance(actions[0], Attack)

    @pytest.mark.now
    def test_convert_second_iteration(self):
        creature = Creature(2, 2)
        troop = Troop([creature])
        m = ManoeuvreIterator(troop)
        # stop iteration at second value
        iter(m)
        next(m)
        next(m)
        actions = m.convert()
        assert isinstance(actions[0], Pass)
