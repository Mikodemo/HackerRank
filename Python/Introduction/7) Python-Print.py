"""
	Name: Python Print
	Author: Nicolas Gomez
	Challenge: Python
	Subdomain: Introduction
	Hacker Rank Link: https://www.hackerrank.com/challenges/python-print/problem
"""

from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())
    
    # What this print line is doing is printing the range of numbers
    # as an array and the separator ( sep ) argument is changing the 
    # in between characters of each print to "" which is empty space
    # making them all print in 1 line back to back.
    print( *range( 1, n + 1 ), sep="" )