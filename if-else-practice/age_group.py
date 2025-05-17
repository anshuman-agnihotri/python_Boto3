age = float(input("Please enter your age : "))
if age <= 13:
    print("Your are child")
elif age >= 14 and age <= 19:
    print("You are teenager")
elif age >=20 and age <= 59:
    print("You are adult")
elif age >= 60:
    print("you are senior citizen")

else:
    print("Invalid input!")