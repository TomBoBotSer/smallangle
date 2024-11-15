import click
import numpy as np
from numpy import pi
import pandas as pd

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def geef_2_plz():
    """This script calculates either the sin or the tan of given x-values.
    """
    pass

@geef_2_plz.command()
@click.option(
    "-n",
    "--number",
    help = "The number (int) represents the amount of even parts into which you want the interval to be divided.",

    default=10,
)
def sin(number):
    """Calculates the sin of the given x-value.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@geef_2_plz.command()
@click.option(
    "-n",
    "--number",
    help = "The number (int) represents the amount of even parts into which you want the interval to be divided.",
    
    default=10,
)
def tan(number):
    """Calculates the tan of the given x-value.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    geef_2_plz()