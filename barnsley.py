from random import choices
import matplotlib.pyplot as plotter


originalTransforms = [
    lambda x,y: (0, 0.16*y),
    lambda x,y: (0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6),
    lambda x,y: (0.20*x - 0.26*y, 0.23*x + 0.22*y + 1.6),
    lambda x,y: (-0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44)
]

originalProbabilities = [0.01, 0.85, 0.07, 0.07]


def affineTransformation(transforms = originalTransforms, probabilities = originalProbabilities, fileName = "barnsley.png", dpi = 600):
    # Lists to hold the coordinates with the initial points pre-inserted.
    xPoints = [0]
    yPoints = [0]


    # The initial points
    x0 = 0.0
    y0 = 0.0

    count = 0
    maximum = int(input("Enter maximum number of iterations: "))

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

    print("Calculations complete...\nStarting plotting...")
    plotter.axis("off")
    plotter.scatter(xPoints, yPoints, s = 0.1, color = "green")
    plotter.title("Barnsley Fern Triangle with {0} points".format(maximum))
    plotter.savefig(fileName, dpi = dpi)
    print("Plotting complete")


if __name__  == "__main__":
    affineTransformation()