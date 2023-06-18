# 🌿 Barnsley Fern
The Barnsley fern is a fractal named after the British mathematician Michael Barnsley who first described it in his book Fractals Everywhere. He made it to resemble the black spleenwort, *Asplenium adiantum-nigrum*.

## 🕖 History
*Fractals Everywhere* was a book based on the course Fractal Geometry that the creator of this structure taught at the Georgia Institute of Technology. The Barnsley Fern was first described in this book. The most beautiful part of this fractal is that it can demonstrate the poetry of mathematics and the relation between nature and numbers. That is, fractals can be used to model plant structures.

## 🏗️ Construction
The fastest way to construct the Barnsley Fern is to use Affine Transformations. These are special types of transformations in Euclidean geometry that preserve lines and parallelism, but not necessarily Euclidean distances and angles.

To generate the Barnsley fern via this approach, the following steps are taken:
1. Start from a given point, say `(x,y)`
2. Apply the affine transformations listed below with their corresponding probabilities:
    Transformation | Probability | Portion Generated
    -------------- | ----------- | -----------------
    `(0, 0.16*y)` | 0.01 | Stem
    `(0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6)` | 0.85 | Successively smaller leaflets
    `(0.20*x - 0.26*y, 0.23*x + 0.22*y + 1.6)` | 0.07 | Largest left-hand leaflet
    `(-0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44)` | 0.07 | Largest right-hand leaflet

3. The result from step 2 is then taken as the new input for the next transformation and the iterative process continues till a desired number of points have been selected. When all these points are plotted in a scatter plot, the resulting pattern converges to the Barnsley fern.

## 📚 Further Reading
* The Wikipedia page for [Barnsley Fern](https://en.wikipedia.org/wiki/Barnsley_fern) is the easiest way to read further about this fractal. As a bonus, the page also contains a number of variations that can be generated via a similar method, albeit with different parameters.
* The original [Fractals Everywhere](https://books.google.com/books?id=oh7NoePgmOIC) book by Michael F. Barnsley can be seen Google Books and is definitely worth a read.