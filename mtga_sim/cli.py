import click
from mtga_sim.app import start as start_sim


@click.command("mtga-sim")
@click.argument("cards_a")
@click.argument("cards_b")
def start(cards_a, cards_b):
    """
    cards_a: Player A cards on battlefield, in the form "2/3;2/2"
    cards_b: Player B cards on battlefield, in the form "4/3"
    """
    start_sim(cards_a, cards_b)
