#Movie tickets based are priced based on the age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on wednesday.
# 1.Price whould be based on age.
# 2.If day is wednesday, discount will be add $2. 

age = float(input("Enter the age: "))
day = input("Enter the day: ").lower()
if age >= 18 and day == "wednesday":
    print("tkt is available only on $16")
elif age >= 18:
    print("tkt is available on $18")

elif age <= 17 and day == "wednesday":
    print("tkt is available only on $6")
elif age < 17:
    print("tkt is available on $8")
else:
    print("invalid input")