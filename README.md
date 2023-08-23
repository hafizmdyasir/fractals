# Fractal Generation
> By Mohammad Yasir

This repository is a collection of interesting algorithms I have and will come across over time related to generating fractal patterns.

Fractals are shapes or patterns that carry the nature of self-similarity, i.e., a magnified or rescaled version appears identical to the original. The concept is not just limited to the realm of digital art and instead, fractals play a major role in computational physics, statistical mechanics, and a plethora of other fields.

## Fractals Included
While there is perhaps an infinity of fractals in this universe, only a few have crossed paths with me so far. Out of those, only some I have been able to implement programmatically, owing to lack of time. 

Either way, you can learn about these using the following links: 
* [Sierpinski Triangle](https://github.com/hafizmdyasir/fractals/blob/3b946a4bdef508bc28c140f86fed522e9c3a05c6/sierpinski.md)
* [Barnsley Fern](https://github.com/hafizmdyasir/fractals/blob/3b946a4bdef508bc28c140f86fed522e9c3a05c6/barnsley.md)
* [Vicsek Fractal](https://github.com/hafizmdyasir/fractals/blob/master/vicsek.md)

## Code Structure
If you simply want to run the program and generate fractals on your own, the `main.py` is the place to start. With Python installed on your system, just run this file and follow the onscreen prompts.

Individually, affine transformations and chaos game implementations are defined in separate files. The class `Fractal`, defined in `main.py` is used to store a reference to the functions for the fractals as well as a few necessary parameters like marker size and color. Do note that each fractal renders best at a specific marker size, which I have chosen via hit and trial.