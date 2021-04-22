from mtga_sim.troop import Creature, Troop


class App(object):
    def __init__(self):
        pass

    def start(self, cards_a, cards_b):
        print('player B: {}'.format(cards_b))
        print('player A: {}'.format(cards_a))
        self.validate(cards_a)
        self.validate(cards_b)
        self.loop_strategies(cards_a, cards_b)

    def loop_strategies(self, cards_a, cards_b):
        troop = self.parse(cards_a)
        print(troop)

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
