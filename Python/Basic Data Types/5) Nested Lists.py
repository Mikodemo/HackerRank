"""
	Name: Nested Lists
	Author: Nicolas Gomez
	Challenge: Python
	Subdomain: Basic Data Types
	Hacker Rank Link: https://www.hackerrank.com/challenges/nested-list
"""

# Will save the variables from the input.
li = []
# Will only save the scores from the input.
scores = []

for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    
	# Temporary list that will put the variables together.
    tmp = [ name, score ]
	# Appends the temporary list to the li list.
    li.append(tmp)
	# Appends the score to the scores list.
    scores.append(score)

# Remove duplicate scores.
uniqueScores = list(set(scores))
# Sorts the scores from low to high.
uniqueScores.sort()
# Saves the second lowest score into a variables.
# Since there are no duplicates, the second lowest grade should be
# the second item in the list.
secondLowest = uniqueScores[1]

# Sorts the li list in alphabetical order.
li.sort()

# This loop  goes through all of the items.
for i in li:
	# If the score is the same as the second lowest, we print the name.
    if( i[1] == secondLowest ):
        print( i[0] )