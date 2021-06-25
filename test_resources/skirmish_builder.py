from mtga_sim.actions.attack_actions import Attack
from mtga_sim.actions.defend_actions import Defend
from mtga_sim.skirmish import Skirmish
from test_resources.builder_base import BuilderBase


class SkirmishBuilder(BuilderBase):
    def __init__(self):
        self.attacker = None
        self.defenders = list()

    def with_attacking(self, creature_repr):
        creature = self.parse_creature_string(creature_repr)
        self.attacker = Attack(creature)
        return self

    def with_defending(self, creature_repr):
        creature = self.parse_creature_string(creature_repr)
        if self.attacker is None:
            raise AssertionError("defend_with must be chained called after with_attacking()")
        defend = Defend(creature, referenced_id=self.attacker.id)
        self.defenders.append(defend)
        return self

    def build(self):
        return Skirmish(self.attacker, self.defenders)
