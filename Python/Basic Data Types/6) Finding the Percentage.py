"""
	Name: Finding the Percentage
	Author: Nicolas Gomez
	Challenge: Python
	Subdomain: Basic Data Types
	Hacker Rank Link: https://www.hackerrank.com/challenges/finding-the-percentage
"""

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()

	# Saves the scores for the student as a list.
    scoresForName = student_marks[query_name]
	# Calculates the average
    average = sum(scoresForName) / len(scoresForName)
	# Prints the average with 2 decimal places.
    print( "%.2f" % average )