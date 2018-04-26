"""
	Name: Find the Runner-Up Score!
	Author: Nicolas Gomez
	Challenge: Python
	Subdomain: Basic Data Types
	Hacker Rank Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
"""

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
	# Checks if n is in between 2 and 10.
    if( 2 <= n <= 10  ):
		# Removes all the duplicates in the list.
        tmp = list( set( arr ) )
        
		# Removes the highest number
        tmp.remove( max( tmp ) )
		
		# Prints the next highest number.
        print( max( tmp ) )