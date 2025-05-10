#!/usr/bin/python3
"""minimum_perations"""
import math


def minOperations(number):
    """minimum_perations_function"""
    if number <= 1:
        return 0

    operations = 0
    for i in range(2, int(math.sqrt(abs(number))) + 1):
        while number % i == 0:
            operations += i
            number //= i

    if number > 1:
        operations += number

    return operations
