"""

AFFINE TRANSFORM
================

Affine transformations can be used to generate a number of fractals. This module defines a funciton affineTransformation, along with certain transforms and corresponding probabilities that can be used to generate fractals. 
"""

from random import choices


B_FERN_TRANSFORMS = (
    lambda x,y: (0, 0.16*y),
    lambda x,y: (0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6),
    lambda x,y: (0.20*x - 0.26*y, 0.23*x + 0.22*y + 1.6),
    lambda x,y: (-0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44)
)

B_FERN_PROBS = (0.01, 0.85, 0.07, 0.07)


def affineTransformation(maximum, transforms = B_FERN_TRANSFORMS, probabilities = B_FERN_PROBS):
    """
    Call this function to calculate the x- and y-values corresponding to the transforms and probabilities passed as arguments.

    Parameters:
        maximum (int): The number of iterations to use.
        transforms (tuple): A tuple of lambda functions, each representing a transformation equation.
        probabilities (tuple): A tuple of floats, each providing the probability associated with the corresponding transform equation.

    Returns:
        A tuple where the first entry is x-values and the second entry is y-values.
    """
    
    # Lists to hold the coordinates with the initial points pre-inserted.
    xPoints = [0]
    yPoints = [0]


    # The initial points
    x0 = 0.0
    y0 = 0.0

    count = 0

    print("Starting calculations...")
    while count < maximum:

        # Pick a transformation and calculate the next value
        chosenTransform = choices(transforms, probabilities)[0]
        nextValue = chosenTransform(x0, y0)

        # Append to list
        xPoints.append(nextValue[0])
        yPoints.append(nextValue[1])

        # Update values
        x0 = nextValue[0]
        y0 = nextValue[1]
        count += 1

    return (xPoints, yPoints)
