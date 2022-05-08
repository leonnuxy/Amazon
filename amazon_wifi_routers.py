# Amazon has installed WiFi routers on the houses along a straight
# street. The city's buildings are arranged linearly, denoted by indices 1
# to n. There are m Amazon routers, and each has a certain range
# associated with it. Router j installed at a certain building location
# i can only provide Internet to the buildings in the range [(i - routerRange[j]), (i + routerRange[j])] inclusive, 
# where routerRange[j] is the range parameter of router j.
# A building is considered to be served if the number of routers
# providing Internet to the building is greater than or equal to the
# number of people living in it. Given a list of the number of people
# living in each building, the locations of the buildings where the
# routers will be installed and each router's range, find the number of
# served buildings in the city.

# Example:
#   buildingCount = [1, 2, 1, 2, 2]
#   routerLocation = [3, 1]
#   routerRange = [1, 2]




#!/bin/python3

import math
import os
import random
import re
import sys
from turtle import right



#
# Complete the 'getServedBuildings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY buildingCount
#  2. INTEGER_ARRAY routerLocation
#  3. INTEGER_ARRAY routerRange
#

def getServedBuildings(buildingCount, routerLocation, routerRange):
    # Write your code here
    
    n = len(buildingCount)
    m = len(routerLocation)

    result = 0

    for i in range(m):
        start_location = routerLocation[i] - 1
        buildingCount[start_location] -= 1
        r_range = routerRange[i]

        for x in range(1, r_range + 1):
            left_start_location = start_location - x
            right_start_location = start_location + x

            if right_start_location > n and left_start_location < 0:
                break

            if left_start_location >= 0:
                buildingCount[left_start_location] -= 1
            if right_start_location < n:
                buildingCount[right_start_location] -= 1


    for i in range(n):
        if buildingCount[i] <= 0:
            result += 1

    return result


# Code Analysis:
# First we need to find the number of buildings that are served by the routers.
# We can do this by iterating through the buildings and checking if the number of people in the building is greater than or equal to the number of routers that are in the range of the building.
# Then we can add the number of buildings that are served to the result.
#
# Time Complexity: O(n^2)
# Space Complexity: O(n)
