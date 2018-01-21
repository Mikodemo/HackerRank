"""
	Name: Python If-Else
	Author: Nicolas Gomez
	Challenge: Python
	Subdomain: Introduction
	Hacker Rank Link: https://www.hackerrank.com/challenges/py-if-else
"""

if __name__ == '__main__':
    n = int(raw_input())
    
	# If  is odd, print Weird
    if( n % 2 != 0 ):
        print "Weird"
    # If  is even
	elif( n % 2 == 0 ):
		# and in the inclusive range of  to , print Not Weird
        if( n >= 2 and n <= 5 ):
            print "Not Weird"
		# and in the inclusive range of  to , print Weird
        elif( n >= 5 and n <= 20 ):
            print "Weird"
		# greater than , print Not Weird
        elif( n >= 20 ):
            print "Not Weird"