#Write a program using a while loop to find the factorial of a user-inputted number.
Number = int(input("Enter a number: "))
factorial = 1

#use of while loop
while Number > 0:
    factorial *= Number
    Number -= 1
    print("Factorial:", factorial)