#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer using recursion.

    Parameters:
        n (int): A non-negative integer for which the factorial is to be computed.

    Returns:
        int: The factorial of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Read the first command-line argument, convert to int, and compute factorial
f = factorial(int(sys.argv[1]))
print(f)
