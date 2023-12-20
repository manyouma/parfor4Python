import numpy as np
import multiprocessing as mp
import time

def isitPrime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False

    return True

if __name__ == "__main__":  
    print(f'Total num CPUs: {mp.cpu_count()+1}')
    for num_core in np.arange(mp.cpu_count()):
        p = mp.Pool(num_core+1)
        m = 10000000
        tic = time.time()
        isPrimes = p.map(isitPrime, range(2, m+1)) # we want to check all integers starting from 2
        nPrimes = sum(isPrimes)
        toc = time.time() - tic
        p.close()
        p.join()
        print(f'Num CPUs: {num_core+1}, number of primes is {nPrimes}, time taken: {toc}')

        