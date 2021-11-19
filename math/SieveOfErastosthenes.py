#!/usr/bin/python3
#-*-charset: utf-8-*-

import argparse
import timeit

parser = argparse.ArgumentParser(prog="Sieve0fEr4t0sthenes", description="Display every prime number in a given space N")
parser.add_argument('N', type=int, help='given space N', metavar='')
arg = parser.parse_args()

def sieveOfEratosthenes(flagged_primes, space, num):

    if num ** 2 >= space:
        return flagged_primes

    if num < 2:
        flagged_primes[num] = False
    elif flagged_primes[num] == True:
        for i in range(num ** 2, space+1, num):
            flagged_primes[i] = False

    return sieveOfEratosthenes(flagged_primes, space, num+1)


if __name__ == "__main__":

    start = timeit.default_timer()
    n = arg.N

    primes = [True for i in range(n+1)]

    primes = sieveOfEratosthenes(primes, n, 0)

    for i in range(n + 1):
        if primes[i]:
            print(i)

    stop = timeit.default_timer()
    execTime = stop-start
    print('\n\ntook', execTime, 's to execute')


    

    


