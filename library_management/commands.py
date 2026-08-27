import click


@click.command()
def hello():
    """Print a hello message."""
    click.echo("Hello from the custom Bench CLI!")


commands = [hello]