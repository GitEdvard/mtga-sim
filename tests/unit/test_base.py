from mtga_sim.actions.attack_actions import AttackAction, Attack, Pass as OffensivePass
from mtga_sim.actions.defend_actions import Defend, Pass as DefensivePass, DefendAction
from mtga_sim.troop import Creature, Troop
from mtga_sim.manoeuvres.manoeuvre import Manoeuvre


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

        return Manoeuvre(actions)

    def passive_attackers_with(self, creatures):
        actions = list()
        for c in creatures:
            actions.append(AttackAction.instantiate(OffensivePass.action_index(), c))

        return Manoeuvre(actions)

    def passive_defenders_with(self, creatures):
        actions = list()
        for c in creatures:
            actions.append(DefendAction.instantiate(DefensivePass.action_index(), c))

        return Manoeuvre(actions)

    def defend_first_with(self, creatures, offensive_manoeuvre):
        """
        All creatures defend from the first creature in the offensive troop
        """
        defend_actions = list()
        for c in creatures:
            defend_actions.append(Defend(
                c, referenced_id=offensive_manoeuvre[0].id
            ))
        return Manoeuvre(defend_actions)
