from mtga_sim.actions.attack_actions import AttackAction, Attack
from mtga_sim.troop import Creature, Troop


class TestBase:
    def create_standard_creatues(self, count):
        creatures = list()
        for i in range(count):
            creatures.append(Creature(2, 2))

        return creatures

    def create_standard_troop(self, count):
        creatures = self.create_standard_creatues(count)
        return Troop(creatures)

    def attack_with(self, creatures):
        actions = list()
        for c in creatures:
            actions.append(AttackAction.instantiate(Attack.action_index(), c))

        return actions
