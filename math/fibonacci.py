#!/usr/bin/env python3
import argparse
import timeit


def fibonacci(N: int) -> int:
    if N <= 2:
        return 1 
    return fibonacci(N - 2) + fibonacci(N - 1)

def main():
    parser: object = argparse.ArgumentParser(prog="Fibonacci", description="Return the fibonacci number for a number N passed in as program argument.") 
    parser.add_argument('N', type=int, default=-1, help="Return the fibonacci number for a passed positive integer N.")
    arg: object = parser.parse_args()

    if arg.N > 0:
        start: float = timeit.default_timer()
        ans:     int = fibonacci(arg.N)
        end:   float = timeit.default_timer()
        total: float = end - start
        
        print(f"{ans} in {total} seconds.")
    else:
        print(f"The passed argument {arg.N} is invalid. Remember to pass in a positive integer value.")


if __name__ == '__main__':
    main()

