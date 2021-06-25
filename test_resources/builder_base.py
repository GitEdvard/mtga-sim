from mtga_sim.troop import Creature


class BuilderBase(object):
    def parse_creature_string(self, creature_str):
        """
        :param cards_str: like "2/4;2/3"
        :return: A Troop
        """
        creature_str = creature_str.strip()
        tmp_split = creature_str.split("/")
        if len(tmp_split) != 2:
            raise AssertionError("Input string is wrong: {}".format(creature_str))
        power, toughness = creature_str.split("/")
        return Creature(int(power), int(toughness))
