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
        self.offensive_passives = None
        self.defensive_passives = None

    def build(self):
        self.create_passives()
        self.create_skirmishes()

    def create_passives(self):
        self.offensive_passives = [a for a in self.offensive_manoeuvre if not a.is_active()]
        self.defensive_passives = [d for d in self.defensive_manoeuvre if not d.is_active()]

    def create_skirmishes(self):
        # Group by attacking creature
        active_defense = [d for d in self.defensive_manoeuvre if d.is_active()]
        ids = [(d.id, d.referenced_id) for d in active_defense]
        active_offense = [a for a in self.offensive_manoeuvre if a.is_active()]
        defenders_by_attacking_id = {a.id: list() for a in active_offense}
        for d, a in ids:
            defenders_by_attacking_id[a].append(d)

        self.skirmishes = list()
        for attack_id, defend_ids in defenders_by_attacking_id.items():
            attacker = self.offensive_manoeuvre.get_by(attack_id)
            defenders = [
                self.defensive_manoeuvre.get_by(id)
                for id in defend_ids
            ]
            self.skirmishes.append(Skirmish(attacker, defenders))

        return self.skirmishes
