# 7. Write a Python program that takes three numbers as command line
# arguments.
# The program should print the largest of the three numbers. 

import sys

# Check if three argument are privided
if len(sys.argv) != 4:
    print("Usage: python largest_of_three.py <num1> <num2> <num3>")
    sys.exit(1)  #Exit if the required argument are not provided
   
    #Convert command-line argument to number
try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    num3 = float(sys.argv[3])

except ValueError:
    print("Please provide valid numbers.")
    sys.exit(1) #Exit if the input is not valid numbers

#Find the largest number
largest = max(num1, num2, num3)

# print the result
print(f"The largest of the three numbers is: {largest}")

