# 🔺 Sierpinski Triangle
The Sierpinski Triangle, also known as a gasket or a sieve is a fractal that was described by Waclaw Sierpinski in 1915. This fractal carries the apperance of an equilateral triangle that has been recursively subdivided into smaller equilateral triangles.

## 🕐 History
As mentioned, the fractal was described by Waclaw Sierpinski, a Polish mathematician in 1915. However, similar patterns have graced the faces of stoneworks laid during the 13th century. The pattern was a common component of the Cosmatesque style of inlay stonework that was prevalent in medieval Italy, especially Rome.

## 🏗️ Construction
There are a plethora of ways to graphically generate Sierpiński triangle, with the most common one being the one of [Removing Triangles](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle#Removing_triangles). A detailed description of these methods is beyond the scope of this readme file. But one can consult the Wikipedia page [here](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle). However, I will take the liberty of describing the chaos game approach that I've used in this repository.

#### 🕹️ The Chaos Game
The Chaos Game approach is perhaps the simplest one to implement mathematically. Here is how it works:
1. Take an equilateral triangle.
2. Pick a random point **P** and assume you are standing here.
3. Select a random vertex **V** of the triangle.
4. Move one-half the distance from your position to the vertex **V**.
5. Repeat from step 3 for as long as required. 

Typically, an outline of the triangle starts to take shape at around a 100 points.