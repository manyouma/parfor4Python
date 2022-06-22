import numpy as np
import multiprocessing as mp
import time
from PrimeNumber import isitPrime


for num_core in np.arange(mp.cpu_count()):
    p = mp.Pool(num_core+1)
    m = 10000000
    tic = time.time()
    isPrimes = p.map(isitPrime, range(2, m+1))
    nPrimes = sum(isPrimes)
    toc = time.time() - tic
    p.close()
    p.join()
    print(f'Num CPUs: {num_core+1}, number of primes is {nPrimes}, time taken: {toc}')