#determine if a fruit is ripe, overripe or unripe based on its color (e.g. banana:green - unripe, yellow - ripe, brown -overripe)
fruit = "banana"
color = "yellow"
if fruit == "banana":
    if color == "yellow":
        print("ripe")
    elif color == "green":
        print("unripe")
    elif color == "brown":
        print("overripe")
else:
    print("invalid input")