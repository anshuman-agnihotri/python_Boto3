#Suggest an activity based on the weather(e.g., sunny- Go for a walk, Rainy - Read a book, Snowy - Build a snowman).
weather = input("Enter the weather : ").lower()
if weather == "sunny":
    print("Go for a walk")
elif weather == "rainy":
    print("Read a book")
elif weather == "snowy":
    print("Build a snowman")
else:
    print("Invalid input, Enter the weather name")