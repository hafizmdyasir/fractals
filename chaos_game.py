"""

CHAOS GAME
==========
The chaos game method can be used to generate a large number of interesting fractals. This module defines various functions that can create a list of points for these shapes.
"""



from random import randint, uniform
from math import sqrt, cos, sin, pi

def sierpinski(maximum):
    """
    Chaos game implementation of the Sierpinski triangle that runs for "maximum" number of times and returns the x-coordinates and y-coordinates packed into a tuple.

    The idea is to create a triangle, pick a random point on its side, then start the chaos game jumps towards randomly chosen vertices.
    """

    #Lists to hold the coordinates with vertices of a 2x2x2 units triangle pre-inserted.
    xPoints = [0,2,1]
    yPoints = [0,0,sqrt(3)]

    #Define a 2x2x2 units equilateral triangle
    triangle = ((0,0), (2,0), (1,sqrt(3)))

    #Equations of the sides of the triangle as lambda functions
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



def vicsek(maximum):
    """
    Chaos game implementation of the Vicsek fractal.

    The idea is to create a square, take its center, then start jumping 2/3 the distance towards any randomly chosen vertex or the midpoint.
    """

    # Once again, we use lists with pre-inserted values for a square.
    xPoints = [-1, 1, -1, 1]
    yPoints = [1, 1, -1, -1]

    # A square
    squarePoints = ((-1,1), (1,1), (-1,-1), (1,-1), (0,0))
    
    # The initially chosen center of the square
    x0 = 0
    y0 = 0

    count = 0
    while count < maximum:

        # Pick a vertex or the center. 4 corresponds to the midpoint.
        choice = randint(0, 4)

        # Create a new point 2/3 the distance towards the randomly chosen point.
        x2 = squarePoints[choice][0]
        y2 = squarePoints[choice][1]
        distance = sqrt((y2 - y0)**2 + (x2-x0)**2)
        
        # Find a point at 2/3 the distance from this to the next point.
        x1 = x0 + (2/3)*(x2-x0)
        y1 = y0 + (2/3)*(y2-y0)

        # Append and update
        xPoints.append(x1)
        yPoints.append(y1)
        x0 = x1
        y0 = y1
        count += 1

    return (xPoints, yPoints)
