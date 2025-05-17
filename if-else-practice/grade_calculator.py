#Assign a letter grade based on a student's score: A(90-100), B(80-89), C(70-79), D(60-69), F(below60)
try:
    percentage = float(input("Enter your percentage: "))
    if percentage <= 100 and percentage >= 90:
        print("Grade A")
    elif percentage <= 89 and percentage >= 80:
        print("Grade B")
    elif percentage <= 79 and percentage >= 70:
        print("Grade C")
    elif percentage <= 69 and percentage >= 60:
        print("Grade D")
    elif percentage < 60:
        print("Grade F")
    else:
        print("Invalid input!")
except ValueError:
    print("Invalid Input, Please enter the neumeric value")