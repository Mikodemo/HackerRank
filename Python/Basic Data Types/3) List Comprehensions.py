"""
	Name: List Comprehensions
	Author: Nicolas Gomez
	Challenge: Python
	Subdomain: Basic Data Types
	Hacker Rank Link: https://www.hackerrank.com/challenges/list-comprehensions/
"""

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())

	# Will store the list for the cuboid
    cuboid = []
    
	# Various loops that will go through all of the possible
	# coordinates given by x, y, and z.
    for i in range(x+1):
        for j in range(y+1):
                for k in range(z+1):
					# The sum of i, j, and k cannot be equal to n.
                    if( ( i + j + k ) != n ):
						# Creates a temporary list and adds it cuboid list.
                        tmp = [i, j, k]
                        cuboid.append(tmp)
    # Prints the cuboid list.                   
    print( cuboid )