import click

@click.command()
def hello():
    """print a greeting form a librarymanagement app"""
    click.echo("Hello from the custom bench CLI")

