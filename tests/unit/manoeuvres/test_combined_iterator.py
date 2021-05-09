import pytest
from mtga_sim.manoeuvres.manoeuvre_iterator import CombinedManoeuvreIterator
from tests.unit.test_base import TestBase


class TestCombinedIterator(TestBase):
    def test_combined_manoeuvre_space__with_1_attacking_1_defending__is_3(self):
        troop_a = self.create_standard_troop(1)
        troop_b = self.create_standard_troop(1)
        it = CombinedManoeuvreIterator(troop_a, troop_b)
        assert len([pair for pair in it]) == 3

    def test_combined_manoeuvre_space__with_2_attacking_1_defending__is_8(self):
        troop_attacking = self.create_standard_troop(2)
        troop_defending = self.create_standard_troop(1)
        it = CombinedManoeuvreIterator(troop_attacking, troop_defending)
        assert len([pair for pair in it]) == 8

    @pytest.mark.skip('')
    def test_all_iterations_are_unique(self):
        troop_attacking = self.create_standard_troop(2)
        troop_defending = self.create_standard_troop(1)
        it = CombinedManoeuvreIterator(troop_attacking, troop_defending)
        pairs = [pair for pair in it]
        for p in pairs:
            print(type(p))
        hashes = [hash(m for m in p) for p in pairs]
        print(type(pairs[0]))
        unique_pairs = list(set(hashes))
        assert len(pairs) == len(unique_pairs)
