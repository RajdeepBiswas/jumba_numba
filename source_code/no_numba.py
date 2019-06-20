import random
import timeit

start = timeit.default_timer()
def monte_carlo_pi(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples


if __name__ == '__main__':
    for i in range (1,500000):
        monte_carlo_pi (100)
    stop = timeit.default_timer()

    print('Total Time: ', stop - start)     