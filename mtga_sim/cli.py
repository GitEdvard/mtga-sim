import click
from mtga_sim.app import start as start_sim
from mtga_sim.app import App

@click.group()
def cli():
    pass


@cli.command("first")
@click.argument("cards_a")
@click.argument("cards_b")
def first(cards_a, cards_b):
    """
    cards_a: Player A cards on battlefield, in the form "2/3;2/2"
    cards_b: Player B cards on battlefield, in the form "4/3"
    """
    start_sim(cards_a, cards_b)


@cli.command("show-first-battle")
@click.argument("cards_a")
@click.argument("cards_b")
def show_first_battle(cards_a, cards_b):
    """
    cards_a: Player A cards on battlefield, in the form "2/3;2/2"
    cards_b: Player B cards on battlefield, in the form "4/3"
    """
    app = App()
    app.show_first_battle(cards_a, cards_b)


@cli.command("show-all")
@click.argument("cards_a")
@click.argument("cards_b")
def show_all(cards_a, cards_b):
    """
    cards_a: Player A cards on battlefield, in the form "2/3;2/2"
    cards_b: Player B cards on battlefield, in the form "4/3"
    """
    app = App()
    app.show_all_manoeuvre_actions(cards_a, cards_b)
