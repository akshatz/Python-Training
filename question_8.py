# Question 8:

# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

import re
import sys
class iterator:
	"""
	Generator generates numbers from 0 to n 
	Returns:
		Numbers divisible by 7
	"""
	def __init__(self, n):

		"""
			Initialize the constructor				
		"""
		super(iterator, self).__init__()
		self.n = n
		
	def divBySeven(self):

		"""
			Generates numbers divisible by 7 within given range n
			Returns:
				Numbers divisible by 7
		"""

		for i in range(0, self.n):
			if i % 7 == 0:
				yield i
try:
    n = input("Enter the number(0-9): ")
    if (re.search("\D",n)):
        raise ValueError(n)
except ValueError as Error:
    print("Invalid Value Please enter between 0-9".format(Error))
    sys.exit(0)
else:
    for num in iterator(int(n)).divBySeven():
        print ("Numbers divisible by seven is: ",num)
    sys.exit(0)
