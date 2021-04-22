from mtga_sim.troop import Troop, Creature


class TestActionPermutations(object):
    def test_troup_of_1__number_permutations_is_2(self):
        creature = Creature(2, 2)
        troup = Troop([creature])
