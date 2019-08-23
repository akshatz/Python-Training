# Question 1:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
# Hints:
# If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
# In case of input data being supplied to the question, it should be assumed to be a console input. 

"""	Computation of Q = Square root of [(2* C * D)/H] """

import re
import math
import sys
c = 50
h = 30
while True:
	try:
		d = input("Enter numbers seperated by comma: ").split(', ')
		for i in range(len(d)):
			if (re.search('\D', d[i])):
				raise ValueError(d)
			else:
				continue
	except ValueError as NumberException:
	        print("Invalid Input:'{}' is not a number".format(NumberException))
	        sys.exit(0)
	else :
		for i in d:
			q=round(math.sqrt((2*c*float(i))/h))
			print(q)
		sys.exit(0)
