#!/bin/python3

import math
import os
import random
import re
import sys



# Amazon prime gamesis designing a gamethe player needs to pass N rounds 
# sequentially in this game rules of the player as follows
#   1. The player loses power[i] health to complete round i
#   2. The player's health must be greater than zero at all times.
#   3. The player can choose to use armor in any one round.
#      The armor will prevent damage of min(armor, power[i]).

#   Determine the minimum starting health for a player to win the game.



# No lower atarting health will allow a win.

# Complete the 'findMinHealth' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY power
#  2. INTEGER armor

# Calculate the minimum starting health for a player to win the game.

def findMinHealth(power, armor):
    # Write your code here
    power_len = len(power)    
    health = 0
    

