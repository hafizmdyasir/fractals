# Sierpiński Triangle
The Sierpiński triangle is an interesting example of fractal geometry. Fractals carry the property of being self-similar in nature, which means that a magnified or rescaled version appears identical to the original. While it is named after the Polish mathematician Wacław Sierpiński, the pattern is historically found in decorative applications centuries before him.

### Creating Sierpiński Triangles
There are a plethora of ways to graphically generate Sierpiński triangle, with the most common one being the one of [Removing Triangles](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle#Removing_triangles). A detailed description of these methods is beyond the scope of this readme file. But one can consult the Wikipedia page [here](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle).

#### 1. Chaos Game
The Chaos Game approach is perhaps the simplest one to implement mathematically. Here is how it works:
1. Take an equilateral triangle.
2. Pick a random point **P** and assume you are standing here.
3. Select a random vertex **V** of the triangle.
4. Move one-half the distance from your position to the vertex **V**.
5. Repeat from step 3 for as long as required. 

Typically, an outline of the triangle starts to take shape at around a 100 points.

### Output
