from mtga_sim.creature_action import Action


class TestActions(object):
    def test_number_of_actions_is_3(self):
        assert Action.number_actions() == 3
