"""
	Name: Lists
	Author: Nicolas Gomez
	Challenge: Python
	Subdomain: Basic Data Types
	Hacker Rank Link: https://www.hackerrank.com/challenges/python-lists/
"""

if __name__ == '__main__':
    N = int(raw_input())
    
	# Initializes the list.
    list = []
	
	# Loop will run for the number of commands entered.
    for i in range(N):
		# Reads the line from input and splits it by spaces.
        command = raw_input().split()
        
		# If the command was insert then the number is inserted
		# in the proper position.
        if( command[0] == "insert" ):
			# int() is necessary to convert the input to an int.
            list.insert( int(command[1]), int(command[2]) )
        # Prints the list.
		elif( command[0] == "print" ):
            print list
        # Deletes the first occurrence of the integer passed on the parameter.
		elif( command[0] == "remove" ):
            list.remove( int(command[1]) )
        # Inserts the integer at the end of the list.
		elif( command[0] == "append" ):
            list.append( int(command[1]) )
		# Sorts the list
        elif( command[0] == "sort" ):
            list.sort()
		# Removes the last element of the list
        elif( command[0] == "pop" ):
            list.pop()
		# Reverses the list.
        elif( command[0] == "reverse" ):
            list.reverse()   