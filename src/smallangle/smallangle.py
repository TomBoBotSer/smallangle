import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def geef_2_plz():
    pass

@geef_2_plz.command()
@click.option(
    "-n",
    "--number",
    default=1,
)
def sin(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@geef_2_plz.command()
@click.option(
    "-n",
    "--number",
    default=1,
)
def tan(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    geef_2_plz()