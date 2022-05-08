#!/bin/python3

import math
import os
import random
import re
import sys

# Given an array of integers, create a 2-dimensional array where 
# the first element is a distinct value from the array and
# the second element is the number of times that value appears in the array.

# Sort the resulting array decending by frequency.
# If multiple values have the same frequency then sort in ascending order.

# Example:
# arr = [3,3, 1, 2, 1]
# result = [[1, 2], [3, 2], [2, 1]]

# Complete the 'groupSort' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
# 

def groupSort(arr):
    # Write your code here
    result = []
    dic = {}
    for i in arr:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    for i in sorted(dic.keys(), key=lambda x: (-dic[x], x)):
        result.append([i, dic[i]])
    return result