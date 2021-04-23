import pytest
from mtga_sim.troop import Troop, Creature
from mtga_sim.manoeuvre_iterator import DefendManoeuvreIterator as ManoeuvreIterator
from mtga_sim.defend_actions import Defend, Pass


class TestDefendManoeuvres(object):
    def test_troop_of_1__number_permutations_is_2(self):
        creature = Creature(2, 2)
        troop = Troop([creature])
        m = ManoeuvreIterator(troop)
        assert len(m) == 2
