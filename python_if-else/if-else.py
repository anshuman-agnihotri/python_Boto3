# Write a Python program to check if a given number is positive, negative, or zero.
number = input("enter the valid number : ")
try:
    number=float(number)
    if number == 0:
        print("number is zero.")
    elif number > 0:
        print("number is positive")
    else:
        print("number is negative.")
except ValueError:
    print("provided value found wrong!")


# Write a program that asks the user for their age and prints whether they are eligible to vote (age ≥ 18).

age = input("Please enter your age : ")
try:
    age=int(age)
    if age >= 18:
        print("your are eligible for vote.")
    else:
        print("You are under aged")
except ValueError:
    print("Provided value are wrong! please enter the age in digits.")


# Write a program to check if a given number is even or odd.

number = input("Please enter the valid number : ")
try:
    number = int(number)
    if number % 2 == 0 :
        print("Number is even.")
    else:
        print("Number is odd.")
except ValueError:
    print("found wrong input")

# Create a program that takes a temperature in Celsius and prints whether it's cold (<20°C), moderate (20-30°C), or hot (>30°C).
tem = input ("Please enter the current tem. : ")
try: 
    tem = float(tem)
    if tem > 30:
        print ("weather is hot.")
    elif tem >= 20:
        print ("weather is moderate.")
    else:
        print ("weather is cold.")

except:
    print("Found wrong input, please enter the valid numeric temperature.")


# Write a program to find the largest of two numbers entered by the user.
a = input ("Please enter the first value : ")
b = input ("Please enter the second value : ")
try:
    a = float(a)
    b = float(b)
    if a > b:
        print(f"{a} is greater than {b}")
    elif b > a:
        print(f"{b} is greater than {a}")
    else:
        print(f"{b} and {a} both are equal.")
except:
    print("entered input wrong! Please enter the numeric value")

# Create a Python program that calculates a discount:
# If the total bill amount is more than $100, apply a 10% discount.
# Otherwise, no discount is applied.

ammount = input ("Please enter the ammount for discount : ")
try:
    ammount = float (ammount)
    if ammount >= 100:
        discount = ammount*0.1
        final_payable_ammount = ammount-discount
        print(f"{final_payable_ammount} is the final ammount for paid")
    else:
        print("no discount is applied.")
except ValueError:
    print("Invalid input! please enter valid ammount.")