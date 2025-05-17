#Choose a mode of transportation based on the distance (e.g., < 3km:walk, 3-15 km:Bike, >15 km:Car).
distance = float(input("Enter the distance in km : "))
if distance < 3:
    print("walk")
elif distance >= 3 and distance < 15:
    print("Bike") 
elif distance >= 15:
    print("Car")

else:
    print("Invalid input, Enter the input in km.")