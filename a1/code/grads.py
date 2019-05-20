import numpy as np

def example(x):
    return np.sum(x**2)


def example_grad(x):
    return 2*x

def foo(x):
    result = 1
    λ = 4 # this is here to make sure you're using Python 3
    for x_i in x:
        result += x_i**λ
    return result

def foo_grad(x):
    return 4*(x**3) # TODO

def bar(x):
    return np.prod(x)

def bar_grad(x):
    # raise NotImplementedError # TODO
    aux = x.shape
    result = np.zeros(aux)
    result += bar(x)
    for x_i in x:
        i = np.argwhere(x==x_i)
        result[i] /= x_i
    return result
