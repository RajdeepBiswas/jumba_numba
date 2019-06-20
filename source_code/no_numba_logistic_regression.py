import numpy as np
import numba
from numba import jit
import timeit
print(numba.__version__)
start = timeit.default_timer()

def logistic_regression(Y, X, w, iterations):
    for i in range(iterations):
        w -= np.dot(((1.0 / (1.0 + np.exp(-Y * np.dot(X, w))) - 1.0) * Y), X)
    return w

if __name__ == '__main__':
    print (logistic_regression (10,10,5,100))
    stop = timeit.default_timer()

    print('Total Time: ', stop - start)         