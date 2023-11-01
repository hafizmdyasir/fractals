"""

GOLDEN RATIO
============
This file holds an interesting visual proof of how some constans are irrational.
"""

from math import sqrt, cos, sin, radians, pi

PHI = (1 + sqrt(5)) / 2
PI = pi

def irrationalProof(maximum, constant = PHI):
    """
    Visual proof of constant's irrationality. Over a large enough number of iterations, an interesting pattern appears.
    """

    # Initial positions and angles
    x1, y1 = 0, 0  # First arm starting at the origin
    theta1 = 0     # Initial angle of the first arm
    theta2 = 0     # Initial angle of the second arm

    # Lists to store (x, y) coordinates
    xPoints = []
    yPoints = []

    for _ in range(maximum):
        # Update angles
        theta1 += 1  # First arm rotates at a constant speed
        theta2 += constant  # Second arm rotates at constant times the speed of the first arm

        # Calculate new positions
        x1_new = cos(radians(theta1))
        y1_new = sin(radians(theta1))
        x2 = cos(radians(theta2))
        y2 = sin(radians(theta2))

        # Calculate the endpoint of the second arm relative to the endpoint of the first arm
        x2 += x1_new
        y2 += y1_new

        xPoints.append(x2)
        yPoints.append(y2)

    return (xPoints, yPoints)


goldenRatio = lambda maximum: irrationalProof(maximum, PHI)
mathPi = lambda maximum: irrationalProof(maximum, PI)