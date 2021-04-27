from mtga_sim.troop import Creature, Troop
from mtga_sim.manoeuvres.manoeuvre_iterator import AttackManoeuvreSpace
from mtga_sim.manoeuvres.manoeuvre_iterator import DefendManoeuvreSpace
from mtga_sim.manoeuvres.manoeuvre_iterator import ManoeuvreIterator


class App(object):
    def __init__(self):
        pass

    def start(self, cards_a, cards_b):
        print('player B: {}'.format(cards_b))
        print('player A: {}'.format(cards_a))
        self.validate(cards_a)
        self.validate(cards_b)
        troop = self.parse(cards_a)
        print(troop)

    def loop_strategies(self, cards_a, cards_b):
        self.validate(cards_a)
        self.validate(cards_b)
        troop_a = self.parse(cards_a)
        troop_b = self.parse(cards_b)
        attack_space = AttackManoeuvreSpace(troop_a)
        attack_it = ManoeuvreIterator(attack_space)
        for attack_manoeuvre in attack_it:
            defend_space = DefendManoeuvreSpace(troop_b, attack_manoeuvre)
            defend_it = ManoeuvreIterator(defend_space)
            for defend_manoeuvre in defend_it:
                pass

    def validate(self, cards):
        cards_lst = cards.split(';')
        for c in cards_lst:
            try:
                spl = list(map(lambda x: int(x), c.split('/')))
            except ValueError:
                raise ValueError('Parse error, {}'.format(c))
            if len(spl) != 2:
                raise ValueError('Parse error, should be len 2, {}'.format(c))

    def parse(self, cards_str):
        """
        :param cards_str: like "2/4;2/3"
        :return: A Troop
        """
        lst = cards_str.split(';')
        troop = Troop()
        for c in lst:
            card_lst = list(map(lambda x: int(x), c.split('/')))
            card = Creature(power=card_lst[0], toughness=card_lst[1])
            troop.append(card)
        return troop


def start(cards_a, cards_b):
    app = App()
    app.start(cards_a, cards_b)
