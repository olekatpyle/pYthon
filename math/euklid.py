#!/usr/bin/env python3

import argparse


def euklid(a: int, b: int) -> int:
    if(b == 0):
        return a
    tmp: int = b
    b        = a % b
    a        = tmp

    return euklid(a,b)


def main() -> None:
    parser: object = argparse.ArgumentParser(prog="Euklids algorithm", description="Find the greatest common devisor of two passed in natural numbers.") 
    parser.add_argument("a", default=-1, type=int, help="First number.")
    parser.add_argument("b", default=-1, type=int, help="Second number.")

    args: object = parser.parse_args()

    ans: int = euklid(args.a, args.b)
    print(f"The greatest common devisor of {args.a} and {args.b} is {abs(ans)}")


if(__name__ == "__main__"):
    main()
