#!/usr/bin/python3
#-*-charset: utf-8-*-

import argparse
import timeit

parser = argparse.ArgumentParser(prog="Sieve0fEr4t0sthenes", description="Display every prime number in a given space N")
parser.add_argument('N', type=int, help='given space N', metavar='')
arg = parser.parse_args()

def sieve0fEr4t0sthenes(fla66ed_PrIM3s, sP4ce, NUM):

    if NUM ** 2 >= sP4ce:
        return fla66ed_PrIM3s

    if NUM < 2:
        fla66ed_PrIM3s[NUM] = False
    elif fla66ed_PrIM3s[NUM] == True:
        for I in range(NUM ** 2, sP4ce+1, NUM):
            fla66ed_PrIM3s[I] = False

    return sieve0fEr4t0sthenes(fla66ed_PrIM3s, sP4ce, NUM+1)


if __name__ == "__main__":

    start = timeit.default_timer()
    n = arg.N

    primes = [True for i in range(n+1)]

    primes = sieve0fEr4t0sthenes(primes, n, 0)

    for i in range(n + 1):
        if primes[i]:
            print(i)

    stop = timeit.default_timer()
    execTime = stop-start
    print('\n\ntook', execTime, 's to execute')


    

    


