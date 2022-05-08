# Amazon Prime Air is developing a system that divides shipping routes using flight
# optimization routing systems to a cluster of aircrafts that can fulfill these routes. Each
# shipping route is identified by a unique integer identifier, requires a fixed non-zero amoun
# of travel distance between airports, and is defined to be either a forward shipping route or
# a return shipping route, Identifiers are guaranteed to be unique within their own route
# type, but not across route types.
# Each aircraft should be assigned two shipping routes at once: one forward route and one
# return route. Due to the complex scheduling of flight plans, all aircraft have a fixed
# maximum operating travel distance, and cannot be scheduled to fly a shipping route that
# requires more travel distance than the prescribed maximum operating travel distance. The
# goal of the system is to optimize the total operating travel distance of a given aircraft. A
# forward/return shipping route pair is considered to be "optimal" if there does not exist
# another pair that has a higher operating travel distance than this pair, and also has a total
# less than or equal to the maximum operating travel distance of the aircraft,
# For example, if the aircraft has a maximum operating travel distance of 3000 miles, a
# forward/return shipping route pair using a total of 2900 miles would be optimal if there
# does not exist a pair that uses a total operating travel distance of 3000 miles, but would
# not be considered optimal if such a pair did exist,
# Your task is to write an algorithm to optimize the sets of forward/return shipping route
# pairs that allow the aircraft to be optimally utilized, given a list of forward shipping routes
# and a list of return shipping routes.
# Input
# The input to the function/ method consists of three arguments:
# maxTravelDist, an integer representing the maximum operating travel distance of the given
# aircraft,
# forwardRouteList, a list of pairs of integers where the first integer represents the unique
# identifier of a forward shipping route and the second integer represents the amount of
# travel distance required by this shipping route;
# returnRouteList, a list of pairs of integers where the first integer represents the unique
# identifier of a return shipping route and the second integer represents the amount of travel
# distance required by this shipping route,
# Output
# Return a list of pairs of integers representing the pairs of IDs of forward and return
# shipping routes that optimally utilize the given aircraft, If no route is possible, return a list
# with empty pair.
# Examples
# Example 1:
# Input.
# maxTravelDist=7000
# forwardRouteList=(I1,2000],[2,4000],[3,6000]]
# returnRouteList=([1,2000]]
# Output:
# [211
# Explanation:
# There are only three combinations, [1,1], [2,1], and [3,11, which have a total of 4000, 6000,
# and 8000 miles, respectively. Since 6000 is the largest use that does not exceed 7000, [2,1]
# is the only optimal pair.
# Example 2:
# Input;
# maxTrave|Dist=10000
# forwardRouteList = (I1, 3000], [2, 5000], [3, 7000], [4, 10000]]
# returnRouteList = II1, 2000], [2, 30001. E£ 4000], [4, 5000]]
# Output:
# L2, 4], [3, 27
# Explanation:
# There are two pairs of forward and return shipping routes possible that optimally utilizes
# the given aircraft,
# Shipping Route ID#/2 from the forwardShippingRouteList requires 5000 miles travelled, and
# Shipping Route ID#4 from returnShippingRouteList also requires 5000 miles travelled.
# Combined, they add up to 10000 miles travelled,
# Similarly, Shipping Route ID#3 from forwardShippingRouteList requires 7000 miles
# travelled, and Shipping Route ID#2 from returnShippingRouteList requires 3000 miles
# travelled. These also add up to 10000 miles travelled.
# Therefore, the pairs of forward and return shipping routes that optimally utilize the aircraft
# are [2, 4] and [3, 2].
# Test Results



def routePairs(maxTravelDist, forwardRouteList, returnRouteList):
    # Write your code here
    result = []
    max_distance = 0
    n = len(forwardRouteList)
    m = len(returnRouteList)
    for i in range(n):
        for j in range(m):
            if forwardRouteList[i][1] + returnRouteList[j][1] == max_distance:
                result.append((forwardRouteList[i][0], returnRouteList[j][0]))
            if forwardRouteList[i][1] + returnRouteList[j][1] <= maxTravelDist and forwardRouteList[i][1] + returnRouteList[j][1] > max_distance:
                max_distance = forwardRouteList[i][1] + returnRouteList[j][1]
                result = [(forwardRouteList[i][0], returnRouteList[j][0])]
    return result


# Code Analysis
# Time Complexity: O(n*m) where n is the number of forward routes and m is the number of return routes
# Space Complexity: O(1)

# First, we need to find the maximum distance that can be traveled by the aircraft.
# Then, we need to find the pairs of forward and return shipping routes that optimally utilize the aircraft.
# We can do this by iterating through the forward shipping routes and return shipping routes,
# and checking if the total distance of the two routes is less than or equal to the maximum distance.
# If it is, we add the pair to the result list, otherwise we do not add the pair to the result list.
