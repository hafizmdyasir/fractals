# ➕ Vicsek Fractal
The Vicsek fractal appears pretty banal at first glance but it finds applications as compact antennas in cellular phones. It is also known as a **vicsek snowflake** or a **box fractal**, though the latter term may also be an umbrella term for various fractals generated via iterative removal of boxes from a square or rectangular grid.

## 🏗️ Construction
The basic idea behind constructing the Vicsek fractal is to take a square and apply the following operations:
1. Divide the square into nine smaller squares using a `3×3` grid.
2. Keep the middle and the corner squares and remove the remaining ones.
3. Repeat recursively for each of the squares till you reach the desired accuracy.

The version of the fractal thus achieved looks like a plus (➕) sign, while an alternative construction where the middle and corner squares are removed leads to a fractal rotated by 45 degrees.

## 🕹️ Chaos Game Implementation
For a chaos game implementation of the rotated form of the Vicsek fractal, we start with a square and take a point at its centre. We then pick a vertex or the centre of the square at random and jump 2/3 the distance to it from our previous point. This soon leads us to the Vicsek Fractal.

## 📷 Screengrab
![Vicsek Fractal 20000 iterations](/screenshots/Vicsek%20Fractal%2020000.png)

