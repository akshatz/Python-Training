# Question 4:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

""" Enter comma seperated 4 bit binary numbers and output as numbers that are divisible by 5 """

import re
import sys
items = []
while True:
	try:
		inputs = input("Enter a sequence of comma separated 4 bit binary numbers(only 0 and 1's): ").split(', ')
		num = [x for x in inputs]
		for i in range(len(num)):
			if not (re.search("^[0|1]+$",num[i])):
				raise ValueError(num)
			else: 
				continue
	except ValueError as Error:
		print("Error! Please enter only 0's and 1's separated by comma.".format(Error))
		sys.exit(0)
	else:
		for p in num:
		    x = int(p, 2)
		    if not x%5:
		        items.append(p)
		    y=','.join(items)
		print("No of 4 bit numbers divisible by 5: ", y)
		sys.exit(0)