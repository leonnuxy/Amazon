#!/bin/python3

from os import environ
from re import compile
from re import match


# Given a list of strings made up the characters 'a' and 'b',
# create a regular expression that will match strings that begin
# and end with the same letter
#
# Write the regular expression in the blank space below
#

# Example:
# 'a', 'aa' and 'bababbb' match
# 'ab' and 'baba' do not match

regularExpression = compile(r'^(a|b)*$')
pattern = compile(regularExpression)

query = int(input())
result = ['False'] * query

for i in range(query):
    someString = input()
    
    if pattern.match(someString):
        result[i] = 'True'

with open(environ['OUTPUT_PATH'], 'w') as fileOut:
    fileOut.write('\n'.join(result))