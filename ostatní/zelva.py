from turtle import *

shape("turtle")
speed(2)

recursion = 1

def fractal__square():
    global recursion
    forward(200/recursion)
    left(90)
    recursion += 0.25
    fractal__square()

def triangle():
    forward(100)
    left(120)
    triangle()

def star():
    forward(100)
    left(144)
    star()

def octagon():
    forward(100)
    left(45)
    octagon()

def circle():
    forward(2)
    left(2)
    circle()

def outer_star():
    forward(100)
    left(144+18)
    forward(100)
    right(144)
    outer_star()

outer_star()