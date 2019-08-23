# Question 6:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

""" Calculate number of Upper case letters and lower case letters"""

string = input("Enter string:")
count1 = 0
count2 = 0
for i in string:
      if(i.isupper()):
        count1=count1+1
      elif(i.islower()):
      	count2=count2+1
print("The number of upper case characters are:")
print(count1)
print("The number of lower case characters are:")
print(count2)