# Fractal Generation
> By Mohammad Yasir

This repository is a collection of interesting algorithms I have and will come across over time related to generating fractal patterns.

Fractals are shapes or patterns that carry the nature of self-similarity, i.e., a magnified or rescaled version appears identical to the original. The concept is not just limited to the realm of digital art and instead, fractals play a major role in computational physics, statistical mechanics, and a plethora of other fields.


### Sierpiński Triangles
The Sierpiński triangle is an interesting example of fractal geometry. While it is named after the Polish mathematician Wacław Sierpiński, the pattern is historically found in decorative applications centuries before him.

There are a plethora of ways to graphically generate Sierpiński triangle, with the most common one being the one of [Removing Triangles](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle#Removing_triangles). A detailed description of these methods is beyond the scope of this readme file. But one can consult the Wikipedia page [here](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle).

#### 1. Chaos Game
The Chaos Game approach is perhaps the simplest one to implement mathematically. Here is how it works:
1. Take an equilateral triangle.
2. Pick a random point **P** and assume you are standing here.
3. Select a random vertex **V** of the triangle.
4. Move one-half the distance from your position to the vertex **V**.
5. Repeat from step 3 for as long as required. 

Typically, an outline of the triangle starts to take shape at around a 100 points.


### Barnsley Fern
The Barnsley Fern is another interesting fractal that can be generated via affine transformations after starting from a random point in 2D space. Variations in the transformations lead to variations in the final output and with careful manipulation, one can create a variety of patterns, each carrying a self-similar nature.

#### Affine Transformations
These are special types of transformations in Euclidean geometry that preserve lines and parallelism, but not necessarily Euclidean distances and angles. To generate the Barnsley fern via this approach, the following steps are taken:
1. Start from a given point, say `(x,y)`
2. Apply the affine transformations listed below with their corresponding probabilities:
    Transformation | Probability
    -------------- | -----------
    `(0, 0.16*y)` | 0.01
    `(0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6)` | 0.85
    `(0.20*x - 0.26*y, 0.23*x + 0.22*y + 1.6)` | 0.07
    `(-0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44)` | 0.07

3. The result from step 2 is then taken as the new input for the next transformation and the iterative process continues till a desired number of points have been selected. When all these points are plotted in a scatter plot, the resulting pattern converges to the Barnsley fern.