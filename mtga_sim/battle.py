from collections import defaultdict
from mtga_sim.skirmish import Skirmish


class Battle:
    """
    Represents a single battle of offending and defensive troops.
    The defensive manoeuvre is created with respect to the already existing
    offencive manoeuvre. A battle instance is typically created within a loop of
    all possible combination of offensive and defensive manoeuvres.
    """
    def __init__(self, offensive_manoeuvre, defensive_manoeuvre):
        self.offensive_manoeuvre = offensive_manoeuvre
        self.defensive_manoeuvre = defensive_manoeuvre
        self.skirmishes = None

    def create_skirmishes(self):
        # Group by attacking creature
        ids = [(d.id, d.referenced_id) for d in self.defensive_manoeuvre]
        defenders_by_attacking_id = defaultdict(list)
        for d, a in ids:
            defenders_by_attacking_id[a].append(d)

        skirmishes = list()
        for attack_id, defend_ids in defenders_by_attacking_id.items():
            attacker = self.offensive_manoeuvre.get_by(attack_id)
            defenders = [
                self.defensive_manoeuvre.get_by(id)
                for id in defend_ids
            ]
            skirmishes.append(Skirmish(attacker, defenders))

        return skirmishes
