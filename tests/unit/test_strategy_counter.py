import pytest
from mtga_sim.troop import Troop, Creature
from mtga_sim.strategy_counter import StrategyCounter


class TestStrategyCounter(object):
    def test_troup_of_1__number_permutations_is_2(self):
        creature = Creature(2, 2)
        troop = Troop([creature])
        m = StrategyCounter(troop)
        assert len(m) == 2

    def test_troup_of_3__number_permutations_is_8(self):
        creature1 = Creature(2, 2)
        creature2 = Creature(2, 2)
        creature3 = Creature(2, 2)
        troop = Troop([creature1, creature2, creature3])
        m = StrategyCounter(troop)
        assert len(m) == 8
