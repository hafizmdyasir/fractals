"""

CHAOS GAME
==========
The chaos game method can be used to generate a large number of interesting fractals. This module defines various functions that can create a list of points for these shapes.
"""



from random import randint, uniform
from math import sqrt

def sierpinski(maximum):
    #Lists to hold the coordinates with vertices of a 2x2x2 units triangle pre-inserted.
    xPoints = [0,2,1]
    yPoints = [0,0,sqrt(3)]

    #Define a 2x2x2 units equilateral triangle
    triangle = ((0,0), (2,0), (1,sqrt(3)))

    #sides of the triangle as lambda functions
    base = lambda x: 0
    left = lambda x: (sqrt(3)) * x
    right = lambda x: (-sqrt(3) * x) + (2 * sqrt(3))
    sides = (base, left, right)

    #Pick a random point on any side
    x0 = 0
    y0 = 0
    sidePicked = randint(0, 2)
    if sidePicked == 0:
        x0 = uniform(0, 2) #The base goes all the way to 2 units.
    elif sidePicked == 1:
        x0 = uniform(0, 1) #The left leg only extends till x = 1.
    elif sidePicked == 2:
        x0 = uniform(1, 2) #The right leg only extends between 1 <= x <= 2.

    y0 = sides[sidePicked](x0)
    xPoints.append(x0)
    yPoints.append(y0)

    count = 0

    print("Starting calculations...")
    while count < maximum:

        #Pick a random vertex
        vertex = triangle[randint(0, 2)]
        
        #Pick a point at the midpoint of the line joining this random vertex and the previous point.
        x1 = (vertex[0] + x0) / 2
        y1 = (vertex[1] + y0) / 2
        
        #Add this point to the list to be drawn
        xPoints.append(x1)
        yPoints.append(y1)

        #Update points and iterator
        x0 = x1
        y0 = y1
        count += 1

    return (xPoints, yPoints)
