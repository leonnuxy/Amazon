#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minimumGroups' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY awards
#  2. INTEGER k

# Amazon Prime Video is a subscription video on demand over the top 
# streaming and rental service. The team at Prime Video is developing 
# a method to divide movies into groups based on the number of awards 
# they have won. The group can consist of any number of movies.
# Difference in the number of awards won by any two movies in the group
# must not exceed K.

# Example
# The numbers of awards per movie are awards = [1, 5, 4, 6, 8, 9, 2],
# and the maximum allowed difference is k=3.
# One way to divide the movies into the minimum number of groups
# is:
# The first group can contain [2, 1]. The maximum difference
# between awards of any two movies is 1 which does not exceed k.
# The second group can contain [5, 4, 6]. The maximum difference
# between awards of any two movies is 2 which does not exceed k.
# The third group can contain [8, 9]. The maximum difference
# between awards of any two movies is 1 which does not exceed k

# The movies can be divided into a minimum of 3 groups.
# Function Description


# The movies can be grouped together irrespective of their initial order.
# Determine the minimum number of groups that can be formed such that 
# each movie is in exactly one group.

# minimumGroups has the following parameters:
#   int awards: Number of awards each movie has end.
#   int k: The maximum difference in a word counts.

def minimumGroups(awards, k):
    # Write your code here
    awards_len = len(awards)
    awards_sorted = sorted(awards)
    awards_sorted_len = len(awards_sorted)
    group_count = 1
    group_min = awards_sorted[0]
    group_max = awards_sorted[0]
    for i in range(1, awards_sorted_len):
        if awards_sorted[i] - group_max <= k:
            group_max = awards_sorted[i]
            group_count += 1
        else:
            group_min = awards_sorted[i]
            group_max = awards_sorted[i]
            group_count += 1
    return group_count