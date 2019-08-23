# Question 5:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

"""	Enter an alphanumeric string It  excludes white space characters """

string = input("Enter an alphanumeric string:")
count1 = 0
count2 = 0
for i in string:
      if(i.isdigit()):
        count1=count1+1
      elif(i.isupper() or i.islower()):
      	count2=count2+1
print("The number of digits are: ", count1)
print("The number of characters are: ", count2)