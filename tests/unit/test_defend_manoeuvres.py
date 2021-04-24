import pytest
from mtga_sim.utils import single
from mtga_sim.troop import Troop, Creature
from mtga_sim.manoeuvre_iterator import DefendManoeuvreIterator as ManoeuvreIterator
from mtga_sim.actions.attack_actions import AttackAction, Attack
from mtga_sim.actions.defend_actions import DefendAction, Defend


class TestDefendManoeuvres(object):
    def test_troop_of_1__number_permutations_is_2(self):
        creature = Creature(2, 2)
        troop = Troop([creature])
        m = ManoeuvreIterator(troop, [])
        assert len(m) == 2

    @pytest.mark.skip('wip')
    def test_response_to_1_attacking__defend_action_references_the_attacker(self):
        creature = Creature(2, 2)
        attack_action = AttackAction.instantiate(Attack.action_index(), creature)
        attack_manoeuvre = [attack_action]
        troop = Troop([creature])
        it = ManoeuvreIterator(troop, attack_manoeuvre)
        defend_strat = single([m for m in it if m[0].action_index() == Defend.action_index()])
        defend_action = single(defend_strat)
        assert defend_action.target_id == attack_action.id

    def test_response_to_1_attacking__number_actions_is_3(self):
        creature = Creature(2, 2)
        attack_action = AttackAction.instantiate(Attack.action_index(), creature)
        attack_manoeuvre = [attack_action]
        troop = Troop([creature])
        it = ManoeuvreIterator(troop, attack_manoeuvre)
        assert it.number_actions() == 3

    @pytest.mark.skip('wip')
    def test_response_to_2_attacking__number_actions_is_4(self):
        # (same creatures attack and defend)
        creatures = self.create_standard_creatues(count=2)
        attack_manoeuvre = self.attack_with(creatures)
        troop = Troop(creatures)
        it = ManoeuvreIterator(troop, attack_manoeuvre)
        # Number of actions for each defending creature
        assert it.number_actions() == 4

    def create_standard_creatues(self, count):
        creatures = list()
        for i in range(count):
            creatures.append(Creature(2, 2))

        return creatures

    def attack_with(self, creatures):
        actions = list()
        for c in creatures:
            actions.append(AttackAction.instantiate(Attack.action_index(), c))

        return actions
