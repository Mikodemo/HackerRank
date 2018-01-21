"""
	Name: Python Loops
	Author: Nicolas Gomez
	Challenge: Python
	Subdomain: Introduction
	Hacker Rank Link: https://www.hackerrank.com/challenges/python-loops/problem
"""

if __name__ == '__main__':
    n = int(raw_input())
	
	#For all non-negative integers i < N , print i^2. Constrains 1 <= N <= 20.
    if ( n >= 1 and n <= 20 and n >= 0 ):
	
        # Print N lines, one corresponding to each i. 
		for i in range(0, n):
            x = i ** 2
            print x