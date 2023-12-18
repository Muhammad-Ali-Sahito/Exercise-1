# Get user input for the number
number = int(input("Enter a number: "))

# Initialize variables
reversed_number = 0

# Reverse the number using a while loop
while number > 0:
    digit = number % 10          # Get the last digit of the number
    reversed_number = reversed_number * 10 + digit  # Append the digit to the reversed number
    number //= 10                # Remove the last digit from the original number

# Print the reversed number
print("Reversed Number:", reversed_number)