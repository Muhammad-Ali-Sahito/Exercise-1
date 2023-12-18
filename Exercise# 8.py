# Get user input for the string
input_string = input("Enter a string: ")

# Initialize the count of vowels
vowel_count = 0

# Iterate through the string using a for loop
for char in input_string:
    # Check if the character is a vowel
    if char.lower() in "aeiou":
        vowel_count += 1

# Print the result
print("Number of vowels:", vowel_count)
