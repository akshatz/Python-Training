# Question 2:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
# Hints:
# Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.


""" No of both row elements and column elements to be taken as input """

import sys
import re

try:
    rows, cols=input("Enter number of rows and columns: ").split(", ")
    result=[]
    if(re.search("\D",rows)):
            raise ValueError(rows)
    for i in range(int(rows)):
            if(re.search("\D",cols)):
                raise ValueError(cols)
    r=[]
    for j in range(int(cols)):
        mul=i*j
        r.append(mul)
        result.append(r)
    print("Total number of rows and columns: ",result)
except ValueError as Expection:
    print("Invalid Value".format(Expection))