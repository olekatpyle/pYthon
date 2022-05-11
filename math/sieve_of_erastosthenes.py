#!/usr/bin/python3

import argparse
import timeit


def sieve_of_eratosthenes(flagged_primes: list, space: int, num: int):

    if num ** 2 >= space:
        return flagged_primes

    if num < 2:
        flagged_primes[num] = False
    elif flagged_primes[num] == True:
        for i in range(num ** 2, space+1, num):
            flagged_primes[i] = False

    return sieve_of_eratosthenes(flagged_primes, space, num+1)


def main():    
    parser: object = argparse.ArgumentParser(prog="Sieve of Eratosthenes", description="Display every prime number in a given space N")
    parser.add_argument('N', type=int, default=-1, help='The number space to find all primes in.')
    arg: object = parser.parse_args()

    if arg.N > 0:
        start: float = timeit.default_timer()
        n: int = arg.N

        primes: list = [True for _ in range(n+1)]

        primes = sieve_of_eratosthenes(primes, n, 0)

        stop: float = timeit.default_timer()
        for i in range(n + 1):
            if primes[i]:
                print(i)

        exec_time: float = stop - start

        print('\n\ntook', exec_time, 's to execute')

    else:
        print("The number space passed in at program call must be positive.")


if __name__ == "__main__":
    main()
