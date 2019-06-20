import numpy as np
import timeit
import numba
from numba import jit

print(numba.__version__)

start = timeit.default_timer()
@numba.jit(nopython=True)

def numpy_histogram(a, bins):
    return np.histogram(a, bins)

if __name__ == '__main__':
    numpy_histogram (1000000,10000)
    stop = timeit.default_timer()

    print('Total Time: ', stop - start)         