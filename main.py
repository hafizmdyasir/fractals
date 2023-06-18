"""

MAIN
====
Main module to interact with user and perform all necessary actions.
"""

import matplotlib.pyplot as plotter
from os import system, name

from affine_transform import *
from chaos_game import *


class Fractal:
    """
    A class to hold information about different fractal generating methods. It also includes information about the plotting size, color, title, etc.
    """

    def __init__(self, fractalName, markerSize, markerColor, function):
        self.name = fractalName
        # Fractals render better at different sizes.
        self.markerSize = markerSize        
        self.markerColor = markerColor

        # To generate this particular fractal, we must call function()
        self.function = function


def plot(xPoints, yPoints, fractalName, markerSize, markerColor, nPoints, dpi = 600):
    
    print("Starting plotting.")
    plotter.scatter(xPoints, yPoints, s = markerSize, color = markerColor)
    plotter.title(f"{fractalName} with {nPoints} points")
    plotter.axis("off")

    plotter.savefig(f"screenshots//{fractalName} {nPoints}.png", dpi = dpi)
    print("Plotting complete")


def cls():
    # Clear screen function.
    system("cls" if name in ('nt', 'dos') else "clear")


FRACTALS = (
    Fractal("Barnsley Fern", 0.1, "green", affineTransformation),
    Fractal("Sierpinski Triangle", 1, "red", sierpinski)
)


def main():
    """
    The heart of the program.
    """
    cls()
    print("NUMERICAL FRACTAL GENERATION\nBy Mohammad Yasir\nM. Sc. Physics\nIIT (ISM)")

    index = 0
    chosen = FRACTALS[0]

    print("Choose out of the following: ")
    print("\t0. Exit.")
    while index < len(FRACTALS):
        print(f"\t{index+1}. {FRACTALS[index].name}")
        index += 1

    choice = int(input("Awaiting input: "))
    if choice == 0:
        return False
    chosen = FRACTALS[choice-1]

    maximum = int(input("Enter the maximum number of iterations: "))
    (x, y) = chosen.function(maximum)
    print("Calculations complete.")
    plot(x, y, chosen.name, chosen.markerSize, chosen.markerColor, maximum)
    delay = input("Press Enter to continue or 'E' to exit: ")
    return delay != 'E'

while main():
    pass
