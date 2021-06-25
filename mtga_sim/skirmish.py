from mtga_sim.troop import Troop


class Skirmish:
    def __init__(self, attacker, defenders):
        self.attacker = attacker
        self.defenders = Troop(defenders)

    def combat(self):
        self.attacker.reduce_damage(self.defenders.power)
        next_power = self.attacker.power
        for d in self.defenders:
            next_power = d.reduce_damage(next_power)
            if next_power <= 0:
                break

    @property
    def died(self):
        died_list = [
            d for d in self.defenders if d.toughness <= 0
        ] + [self.attacker if self.attacker.toughness <= 0 else None]
        return died_list
