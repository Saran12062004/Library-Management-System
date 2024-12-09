# 3. Write a Python program that asks the user to input a temperature in
# Celsius.
# Convert the temperature to Fahrenheit and print the result.
# Fahrenheit=(Celsius×59)+32 

# Get the temperature in celaius
# celsius = float(input("Enter the temperature in celsius:"))

# # convert to Fahrenheit
# fahrenheit = (celsius * (9 / 5)) + 32

# # Display the result
# print(f"{celsius}°C is equal to {fahrenheit:.2f}")

# 4. Write a Python program that asks the user for their weight in kilograms
# and height in meters.
# Calculate and print the BMI using the formula BMI=weightheight2\text{BMI} = weight/
# height2 

# Get the user's weigth in kilograms
# weigth = float(input("Enter Your weight in kilograms:"))

# # Get the user's height in meters
# height = float(input("Enter your height in meters: "))

# # calculate BMI
# bmi = weigth / (height ** 2)

# # Display the result
# print(f"Your BMI is: {bmi:.2f}")

# 5. Write a Python program that asks the user for the principal amount, rate
# of interest, and time (in years).
# Calculate and print the simple interest using the formula
# Simple Interest=Principal×Rate×Time/100 

# Get the principal amount
# principal = float(input("Enter the principal amount:"))

# # Get the rate of interest
# rate = float(input("Enter the rate of interest (% per year): "))

# # Get the time in years
# time = float(input("Enter the time (in years):"))

# # Calculate Simple Interest
# simple_interest = (principal * rate * time) / 100

# # Display the result
# print(f"The Simple Interest is: {simple_interest:.2f}")



                                                                 # Flow Control Part-1


# 1. Write a program that takes an exam score as input and prints the grade
# according to the following rules:
#  90-100: A ,80-89: B, 70-79: C, 60-69: D,0-59: F

# def determine_grade(score):
#     if 90 <= score <= 100:
#         return "A"
#     elif 80 <= score <= 89:
#         return "B"
#     elif 70 <= score <= 79:
#         return "C"
#     elif 60 <= score <= 69:
#         return "D"
#     elif 0 <= score <= 59:
#         return "F"
#     else:
#         return "Invalid score. Please enter a value between 0 and 100."

# # Input from the user
# try:
#     score = int(input("Enter the exam score (0-100): "))
#     grade = determine_grade(score)
#     print(f"The grade is: {grade}")
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")


# 2. Write a program that takes three numbers as input and prints the
# smallest.

# def find_smallest(num1, num2, num3):

#     """
#     Datermine the smallest of three numbers.

#     Parameters:
#     num1 (float):The first number,
#     num2 (float): The second number.
#     num3 (float): The third number,

#     return:
#     float: the smallest number among the three inputs.
#     """

#     return min(num1, num2, num3)

# # Input from the user
# try:
#     num1 = float(input("Enter the first number:"))
#     num2 = float(input("Enter the second number"))
#     num3 = float(input("Enter the third number:"))

#     smallest = find_smallest(num1,num2,num3)
#     print(f"The smallest number is:{smallest}")
# except ValueError:
#     print("Invalid input. Please enter valid numbers.")    

# 3. Write a program that checks whether a given letter is a vowel or a
# consonant.

# def check_letter_type(letter):

#     """
#     Check whether a given letter is a vowel or a consonant

#     Parameters:
#     letter (str): A single letter to check.

#     Returns:
#     strL "Vowel" if the letter is a vowel "Consonant" if it is a consonant,
#     or an error message if the input is invalid.
#     """
#     vowels = "asiouAEIOU"

#     if len(letter) != 1 or not letter.isalpha():
#         return"Invalid input, Please enter a single alphabet letter."
    
#     if letter in vowels:
#         return "Vowels"
#     else:
#         return "Consonant"

# # Input from the user
# letter = input("Enter a single letter:")
# result = check_letter_type(letter)
# print(result)


# 4. Write a program that takes an integer N as input and calculates the sum
# of the first N natural numbers.

# Function to calculate sum of first N natural numbers
# def sum_of_natural_numbers(N):
#     return N * (N + 1) // 2  # Formula for the sum of first N natural numbers

# # Input from the user
# N = int(input("Enter a positive integer N: "))

# # Check if the input is valid
# if N > 0:
#     result = sum_of_natural_numbers(N)
#     print(f"The sum of the first {N} natural numbers is: {result}")
# else:
#     print("Please enter a positive integer.")

# 5.Write a program that prints the multiplication table for a given number
# up to 10

# Function to print the multiplication table

# def multiplication_table(number):
#     for i in range(1, 11):
#         print(f"{number} x {i} = {number * i}")

# # Input from the user
# number = int(input("Enter a number to print its multiplication table:"))

# # call the funtion to display the multiplication table
# multiplication_table(number)

# 6.Write a program that takes an integer input (1-7) and prints the
# corresponding day of the week (1 for Monday, 7 for Sunday). 

# Function to print the day of the week based on the input number
# def day_of_week(day_num):
#     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday", "Sunday"]

#     if 1 <= day_num <= 7:
#         print(f"Your Fav day {day_num} is: {days[day_num - 1]}")

#     else:
#         print("Please Enter a Number between 1 and 7.") 

# # Input from the user
# day_num = int(input("Enter a Number of Your Fav Day:")) 

# # Call the function to display the day of the week
# day_of_week(day_num)

# 7.Write a program that takes a number as input and checks if it is positive,
# negative, or zero

# Function to check if the number is positive, or zero

# def check_number(num):
#     if num > 0:
#         print(f"The number {num} is positive.")
#     elif num < 0:
#         print(f"The number {num} is negative.")

#     else:
#         print("The number is zero.")

# # Input from the user
# num = float(input("Enter a number:"))

# # call the function to check the number
# check_number(num)


# 8.Write a program that calculates the sum of all even numbers between 1
# and 100.

# Function to calculate the sum of all even numbers between 1 and 100
# def sum_of_even_numbers():
#     total = 0
#     for num in range(2, 101, 2):  # Start at 2, go up to 100, step by 2 (even numbers)
#         total += num
#     return total

# # Call the function and print the result
# result = sum_of_even_numbers()
# print(f"The sum of all even numbers between 1 and 100 is: {result}")

# 9.Write a program that counts the number of vowels in a given string.

# Function to count the number of vowels in a string
# def count_vowels(input_string):
#     vowels = "aeiouAEIOU"  # List of vowels (both lowercase and uppercase)
#     count = 0
    
#     # Loop through each character in the string
#     for char in input_string:
#         if char in vowels:
#             count += 1  # Increment count if the character is a vowel
    
#     return count

# # Input from the user
# input_string = input("Enter a string: ")

# # Call the function and display the result
# vowel_count = count_vowels(input_string)
# print(f"The number of vowels in the string is: {vowel_count}")

# 10..Write a program that counts the number of times a specific character
# appears in a given string. 

# Function to count the occurrences of a specific character in a string

# def count_character(input_string, character):
#     count = input_string.count(character) #USing the built-in count() method
#     return count

# # Input from the user
# input_string = input("Enter a string:")
# character = input("Enter the character to count: ")

# # call the function and display the result
# char_count = count_character(input_string, character)
# print(f"The character `{character}` appears {char_count} times in the string.")