# 6. Write a Python program that accepts a string as a command line
# argument.
# The program should print the reversed string.

import sys

# Check if a string is provided as a command-line argument
if len(sys.argv) > 1:
    input_string = sys.argv[1]

    # Reverse the string
    reversed_string = input_string[::-1]
    print(f"Reversed string: {reversed_string}")
else:
    print("Please provide a string as a command-line argument.")
