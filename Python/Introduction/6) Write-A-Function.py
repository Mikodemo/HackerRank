"""
	Name: Write A Function
	Author: Nicolas Gomez
	Challenge: Python
	Subdomain: Introduction
	Hacker Rank Link: https://www.hackerrank.com/challenges/write-a-function/problem
"""

def is_leap(year):
    leap = False
    
    # Write your logic here
	
	# Constrains 1900<= y <= 10^5
    if( year >= 1900 and year <= ( 10 ** 5 ) ):
        #The year can be evenly divided by 4, is a leap year, unless: The year can be evenly divided by 100, it is NOT a leap year, unless:
		if ( year % 4 == 0 and year % 100 != 0 ):
            leap = True
		#The year is also evenly divisible by 400. Then it is a leap year.
        elif( year % 400 == 0 ):
            leap = True
    return leap