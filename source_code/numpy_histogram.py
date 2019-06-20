import numpy as np
import timeit


start = timeit.default_timer()

def numpy_histogram(a, bins):
    return np.histogram(a, bins)

if __name__ == '__main__':
    numpy_histogram (1000000,10000)
    stop = timeit.default_timer()

    print('Total Time: ', stop - start)         