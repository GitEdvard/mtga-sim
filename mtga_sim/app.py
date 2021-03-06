from mtga_sim.battle import Battle
from mtga_sim.troop import Creature, Troop
from mtga_sim.manoeuvres.manoeuvre_iterator import CombinedManoeuvreIterator
from mtga_sim.ui.battle_controller import BattleController
from mtga_sim.ui.battle_view import BattleView
from mtga_sim.ui.battle_model import BattleModel


class App(object):
    def __init__(self):
        pass

    def start(self, cards_a, cards_b):
        print('player B: {}'.format(cards_b))
        print('player A: {}'.format(cards_a))
        self.validate(cards_a)
        self.validate(cards_b)
        troop = self.parse_single_player(cards_a)
        print(troop)

    def show_first_battle(self, cards_a, cards_b):
        """
        working now
        """
        troop_attacking, troop_defending = self.parse_input(cards_a, cards_b)
        iterator = CombinedManoeuvreIterator(troop_attacking, troop_defending)
        iter(iterator)
        attack, defend = next(iterator)
        battle = Battle(attack, defend)
        battle.build()
        battle_controller = BattleController()
        battle_controller.render(battle)

    def show_all_manoeuvre_actions(self, cards_a, cards_b):
        troop_attacking, troop_defending = self.parse_input(cards_a, cards_b)
        iterator = CombinedManoeuvreIterator(troop_attacking, troop_defending)
        battle_controller = BattleController()
        for offensive, defensive in iterator:
            battle = Battle(offensive, defensive)
            battle.build()
            battle_controller.render(battle)
            input("hit enter")

    def loop_strategies(self, cards_a, cards_b):
        self.validate(cards_a)
        self.validate(cards_b)
        troop_a = self.parse_single_player(cards_a)
        troop_b = self.parse_single_player(cards_b)
        iterator = CombinedManoeuvreIterator(troop_a, troop_b)
        for attack, defend in iterator:
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

    def parse_input(self, cards_attacking, cards_defending):
        self.validate(cards_attacking)
        self.validate(cards_defending)
        troop_attacking = self.parse_single_player(cards_attacking)
        troop_defending = self.parse_single_player(cards_defending)
        return troop_attacking, troop_defending

    def parse_single_player(self, cards_str):
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
