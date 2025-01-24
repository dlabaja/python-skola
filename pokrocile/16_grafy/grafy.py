import pylab as pl
import numpy as np

class Graph:
    def __init__(self, label, title, axis):
        self.label = label
        self.title = title
        self.axis = axis

    def draw(self, x, y):
        pl.plot(x, y, label=self.label)
        pl.title(self.title)

        pl.xlabel(self.axis[0])
        pl.ylabel(self.axis[1])
        pl.legend()

        pl.show()

    
def draw_sinus(axis, x):
    Graph(label="sin(x)", title="Graph of sin(x)", axis=axis).draw(x, np.sin(x))

def draw_cosinus(axis, x):
    Graph(label="cos(x)", title="Graph of cos(x)", axis=axis).draw(x, np.cos(x))

def draw_logarithm(axis, x):
    Graph(label="log(x)", title="Graph of log(x)", axis=axis).draw(x, np.log10(x))

def draw_exponential(axis, x):
    Graph(label="exp(x)", title="Graph of exp(x)", axis=axis).draw(x, np.exp(x))

def draw_custom_graph(axis, x, y):
    Graph(label="Custom graph", title="Custom graph", axis=axis).draw(x, y)