"""
	Name: Tuples
	Author: Nicolas Gomez
	Challenge: Python
	Subdomain: Basic Data Types
	Hacker Rank Link: https://www.hackerrank.com/challenges/python-tuples
"""

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())

	# The tuple() function converts a list to a tuple.
    t = tuple(integer_list)
            
	# Prints the result of the hash function with parameter t.
    print( hash(t) )