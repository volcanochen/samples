from multiprocessing import Pool
from math import hypot
from random import random
import time

def test(tries):
    print "runing ..."
    return sum(hypot(random(), random()) < 1 for _ in range(tries))

def calcPi(nbFutures, tries):
    ts = time.time()
    p = Pool(1)
    result = p.map(test, [tries] * nbFutures)
    ret = 4. * sum(result) / float(nbFutures * tries)
    span = time.time() - ts
    print "time spend ", span
    return ret
if __name__ == '__main__':
    print("pi = {}".format(calcPi(3000, 4000)))
