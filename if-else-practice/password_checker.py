#Check if a len(password) is "weak", "medium" or "strong". Crieria:<6 chars(weak), 6-10 chars (medium), >10 chars (strong)
password = input("Enter the password : ")
if len(password) < 6:
    print("Weak")
elif len(password) >=6 and len(password) <= 10:
    print("Medium")
elif len(password) >= 10:
    print("Strong")

else:
    print("Invalid Input!")