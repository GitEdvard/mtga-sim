from mtga_sim.attack_actions import AttackAction


class TestActions(object):
    def test_number_of_actions_is_3(self):
        assert AttackAction.number_actions() == 3
