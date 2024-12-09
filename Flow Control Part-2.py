# 1. Write a program that categorizes a person's age into Child, Teen, Adult,
# or Senior using nested conditions. 

# Get the age from the user

# age = int(input("Enter your age: "))

# # Categorize based on using nested condition
# if age < 13:
#     print("child")
# elif age < 20:
#     print("Teen")
# else:
#     if age < 60:
#         print("Adult")
#     else:
#         print("Senior")       

# 2. Write a program to generate a pyramid pattern using nested loops. 

# Number of rows for the pyramid

# n = int(input("Enter the number of rows for the pyramid: "))

# # Loop through each row
# for i in range(1, n + 1):
#     # print leading space for alignment
#     for j in range(n - i):
#         print(" ", end="")

#         # print the starts
#         for k in range(2 * i - 1):
#             print("*", end="")
#         #Move to the next line after each row
#         print() 

# 3. Write a Python program that loops through numbers from 1 to 20. Skip
# the even numbers using continue. 

# Loop through numbers from 1 to 20
# for i in range(1, 21):
#     # skip the even number
#     if i % 2 == 0:
#         continue
#     print(i)

# 4. Create a program that loops through a list of names. Use pass to ignore
# names shorter than 4 letters. 

# List of names
# names = ["john", "Ana", "Milke", "sue", "Tom", "sarah", "Ray"]

# # Loop through the list of names
# for name in names:
#     # if the name is shorter then 4 letters, skip it
#     if len(name) < 4:
#         pass
#     else:
#         print(name)

# 5. Write a program that prompts the user to enter a password. If the
# password is "exit," break out of the loop and print a goodbye message. 

# Loop to prompt the user for a password

# while True:
#     # Prompt the user to enter a password
#     password = input("Enter your password(type 'exit' to quit): ")

#     # check if the entered password is 'exit'
#     if password == "exit":
#         print("Goodbye!")
#         break  #Break out of the loop if the password is "exit"

# 6. Create a list of 5 numbers. Use the del statement to remove the third
# item from the list. 

# Create a list of 5 numbers
# numbers = [10,20,30,40,50]

# # Remove the third item (index 2) using del
# del numbers[2]

# # print the updated list
# print("Updated list:", numbers)

# 7. Create a program that takes a list of numbers, deletes any number
# greater than 10 using del, and prints the modified list.

# create a list of numbers
# numbers = [3,12,7,15,8,10,22,6]

# # Loop through the list in reverse to avoid skipping element
# for i in range(len(numbers) - 1, -1, -1):
#     if numbers[i] > 10:
#         del numbers[i]  #Deleted the number if it's greated than 10

# #print the modified list
# print("Modified list:", numbers) 

# 8. Write a Python program to determine eligibility for a loan. The program
# should check if the applicant’s age is between 21 and 65, has a monthly
# income above $3000, and a credit score above 700. Use nested
# conditions to ensure all criteria are met. 

# prompt the user for their details
# age = int(input("Enter your age: "))
# monthly_income = float(input("Enter your monthly income: "))
# credit_score = int(input("Enter your credit score: "))

# # check loan eligibility using nested conditions
# if 21 <= age <= 65:
#     if monthly_income > 3000:
#         if credit_score > 700:
#             print("You are eligible for a loan.")
#         else:
#             print("You are not eligible for a loan due to a low credit score.")
#     else:
#         print("You are not eligible for a loan due to insufficient monthly income.")
# else:
#     print("You are not eligible for a loan due to age restrictions.")  

# 9. Create a program to determine the shipping cost for an online store. If
# the purchase amount is over $50, offer free shipping; otherwise,
# calculate the shipping cost based on the delivery location (local,
# interstate, or international) using nested conditions. 

# Prompt the user for purchase amount and delivery location
# purchase_amount = float(input("Enter the purchase amount: "))
# print("Delivery locations: Local, Interstate, International")
# delivery_location = input("Enter the delivery location: ").strip().lower()

# # Determine the shipping cost
# if purchase_amount > 50:
#     print("Free shipping!")
# else:
#     if delivery_location == "local":
#         shipping_cost = 5.0  # Flat rate for local delivery
#     elif delivery_location == "interstate":
#         shipping_cost = 10.0  # Flat rate for interstate delivery
#     elif delivery_location == "international":
#         shipping_cost = 20.0  # Flat rate for international delivery
#     else:
#         print("Invalid delivery location entered!")
#         shipping_cost = None

#     # Display the shipping cost if it was calculated
#     if shipping_cost is not None:
#         print(f"Shipping cost: ${shipping_cost:.2f}")


# 10.Develop a program that categorizes a student's grade based on their
# score. Use nested conditions to determine if the student gets an A, B, C,
# D, or F, and if they qualify for honors (e.g., above 90%). 

# Prompt the user for the student's score
# score = float(input("Enter the student's score (0-100): "))

# # Determine the grade and honors status using nested condition
# if 0 <= score <= 100:  #Ensure the score is valid
#     if score >= 90:
#         grade = "A"
#         if score > 95:
#             honors = "High Honors"
#         else:
#             honors = "Honors"
#     elif score >= 80:
#         grade = "B"
#         honors = None
#     elif score >= 70:
#         grade = "C"
#     elif score >= 60:
#         grade = "D"
#         honors = None
#     else:
#         grade = "F"
#         honors = None

# # Display the grade and honors status
#     print(f"Grade: {grade}")
#     if honors:
#        print(f"Congratulations! You achieved {honors}")

# else:
#     print("Invalid score. please enter a score between 0 and 100.")

# 11.
# Item in the store with stock availability

# grocery_items = {
#     "apple": {"price": 1.0, "stock": 10},
#     "banana": {"price": 0.5, "stock": 0},  # Out of stock
#     "orange": {"price": 0.8, "stock": 5},
#     "milk": {"price": 1.5, "stock": 2},
# }
# # Initialize total cost
# total_cost = 0

# # Checkout process
# print("Welcome to the grocery store! Type 'done' when finished.")
# while True:
#     # Display available items
#     print("\nAvailable items:")
#     for item, details in grocery_items.items():
#         print(f"{item.capitalize()} - ${details['price']} (Stock: {details['stock']})")
    
#     # Prompt the user to select an item
#     selected_item = input("Enter the item you want to purchase: ").strip().lower()
    
#     # Stop the process if the user is done
#     if selected_item == "done":
#         print("Payment completed.")
#         break
    
#     # Check if the item is in the store
#     if selected_item not in grocery_items:
#         print("Item not found. Please choose a valid item.")
#         continue
    
#     # Check if the item is out of stock
#     if grocery_items[selected_item]["stock"] <= 0:
#         print(f"Sorry, {selected_item} is out of stock.")
#         continue
    
#     # Process the purchase
#     quantity = int(input(f"How many {selected_item}s would you like to buy? "))
#     if quantity > grocery_items[selected_item]["stock"]:
#         print(f"Sorry, we only have {grocery_items[selected_item]['stock']} {selected_item}(s) available.")
#         continue
    
#     # Update stock and calculate cost
#     grocery_items[selected_item]["stock"] -= quantity
#     total_cost += grocery_items[selected_item]["price"] * quantity
#     print(f"You added {quantity} {selected_item}(s) to your cart. Total cost: ${total_cost:.2f}")
    
# # Display final amount
# print(f"\nThank you for shopping with us! Your total bill is ${total_cost:.2f}.")

# 12.
# predefined correct password
correct_password = "Saran123"

# Number of allowed attemps
attempts = 3

# Login system
while attempts > 0:
    # prompt the user to enter the password
    entered_password = input("Enter your password: ")

    # check if the entered password is correct
    if entered_password == correct_password:
        print("Login successful!")
        break  # Exit the loop if the password is correct
    else:
        attempts -= 1   #Decrease the number of attempts
        if attempts > 0:
            print(f"Incorrect password. You have {attempts} attempts(S) left.")

        else:
            print("Incorrect password, you have no attempts left. Access denied.")