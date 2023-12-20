import numpy as np
import multiprocessing as mp
import time

def toy_product(k):
    # A silly function intended to have a high computational complexity
    k_np = np.array(k)
    for i in np.arange(100):
        k_np = np.sqrt(k_np)
        k_np = np.power(k_np,2)
      
    return k_np.prod() 

if __name__ == "__main__":  
    
    print(f'Total num CPUs: {mp.cpu_count()+1}')
    array2pass = np.random.random((100000,30)).tolist()

    for num_core in np.arange(mp.cpu_count()):
        p = mp.Pool(num_core+1)
        tic = time.time()
        products = p.map(toy_product, array2pass) # we want to check all integers starting from 2
        sum_product = sum(products)
        toc = time.time() - tic
        p.close()
        p.join()
        print(f'Num CPUs: {num_core+1}, sum of product is {sum_product}, time taken: {toc}')

        