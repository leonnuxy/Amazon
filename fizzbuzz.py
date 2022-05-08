# Given a number n, for each integer i in the range from 1 to n inclusive, print one value per line as follwos:
#   - If i s a multiple of both 3 and 5, print "FizzBuzz"
#   - If i s a multiple of 3, print "Fizz"
#   - If i s a multiple of 5, print "Buzz"
#   - Otherwise, print i



#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    for i in range(1, n+1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
