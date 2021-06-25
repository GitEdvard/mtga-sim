from mtga_sim.actions.attack_actions import AttackAction, Attack, Pass
from mtga_sim.actions.defend_actions import Defend, Pass as DefendPass
from mtga_sim.battle import Battle
from mtga_sim.manoeuvres.manoeuvre import Manoeuvre
from mtga_sim.troop import Troop, Creature


class BattleBuilder(object):
    def __init__(self):
        self.attackers = list()
        self.defenders = list()

    def with_attacking(self, creature_repr):
        creature = self._parse_creature_string(creature_repr)
        self.attackers.append(
            Attack(creature)
        )
        return self

    def with_passive_offensive(self, creature_repr):
        creature = self._parse_creature_string(creature_repr)
        self.attackers.append(
            Pass(creature)
        )

    def defend_with(self, creature_repr):
        creature = self._parse_creature_string(creature_repr)
        latest_attacker = self.attackers[-1]
        if latest_attacker is None:
            raise AssertionError("defend_with must be chained called after with_attacking()")
        defend = Defend(creature, referenced_id=latest_attacker.id)
        self.defenders.append(defend)
        return self

    def with_passive_defending(self, creature_repr):
        creature = self._parse_creature_string(creature_repr)
        self.defenders.append(
            DefendPass(creature)
        )

    def build(self):
        offensive_maneouvre = Manoeuvre(self.attackers)
        defensive_maneouvre = Manoeuvre(self.defenders)
        battle = Battle(offensive_maneouvre, defensive_maneouvre)
        battle.build()
        return battle

    def _parse_creature_string(self, creature_str):
        """
        :param cards_str: like "2/4;2/3"
        :return: A Troop
        """
        creature_str = creature_str.strip()
        tmp_split = creature_str.split("/")
        if len(tmp_split) != 2:
            raise AssertionError("Input string is wrong: {}".format(creature_str))
        power, toughness = creature_str.split("/")
        return Creature(power, toughness)
