from multiprocessing import Pool, TimeoutError, Process, freeze_support
import time
import os

def f(x):
    time.sleep(0)
    return x*x

if __name__ == '__main__':
    pool = Pool(processes=16)              # start 4 worker processes

    # evaluate "f(20)" asynchronously
    res1 = pool.apply_async(f, (20,))      # runs in *only* one process
    res2 = pool.apply_async(f, (10,))      # runs in *only* one process
    res3 = pool.apply_async(f, (5,))      # runs in *only* one process
    #print res.get(timeout=1)              # prints "400"
    
    
    erg1 = ""
    erg2 = ""
    erg3 = ""

    try:
        erg1 = res1.get(timeout=10)
    except TimeoutError:
        print "We lacked patience and got a multiprocessing.TimeoutError"
        
    try:
        erg2 = res2.get(timeout=0)
    except TimeoutError:
        print "We lacked patience and got a multiprocessing.TimeoutError"
        
    try:
        erg3 = res3.get(timeout=0)
    except TimeoutError:
        print "We lacked patience and got a multiprocessing.TimeoutError"
        
    print erg1
    print erg2
    print erg3