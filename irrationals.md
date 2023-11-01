# 🔢 Irrational Numbers
The simplest definition of rational numbers is:
> Numbers that can be represented in the form p/q, where p and q are integers and q is not zero are called rational numbers.

There are a number of mathematical constants which are irrational in nature, the most famous examples being pi, and phi (the golden ratio). This is a visual proof of the same

## 🏗️ How it works
The idea is that if two rods of equal length, attached end-to-end, are rotating with rotation speeds in a given ratio **a/b**, then they will completely overlap each other over the course of their rotations. However, if we set the speed of the first one to be **1 units** and that of the other to be **pi** units, something magical happens. A beautiful pattern emerges as the rods never overlap and the endpoint of the second rod traces out a pretty pattern (take a look at the screenshots)

#### 🕹️ The Process
Coding this in Python is immensely easy. We work with polar coordinates **(r, θ)**. Keeping **r** constant for both, we continuously increment **θ** for one in increments of 1 unit and for the other in increments of pi units. This allows us to find the trajectory of the end point of the second rod and we end up with the required pattern.