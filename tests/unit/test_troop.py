import pytest
from mtga_sim.troop import Troop, Creature


class TestTroop(object):
    def test_iterate_troop(self):
        creature = Creature(2, 2)
        troop = Troop([creature])
        llen = len([c for c in troop])
        assert llen == 1

    def test_length_of_troop(self):
        creature = Creature(2, 2)
        troop = Troop([creature])
        llen = len(troop)
        assert llen == 1

    @pytest.mark.now
    def test_can_refer_by_index(self):
        creature = Creature(2, 2)
        troop = Troop([creature])
        c = troop[0]
        assert c is not None
