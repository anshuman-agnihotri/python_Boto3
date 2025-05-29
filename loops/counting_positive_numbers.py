#Counting positive numbers: Given list of numbers, count how many are positive.
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9 ,10]

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9 ,10]
positive_number_count = 0
for num in numbers:
    if num > 0:
        positive_number_count = positive_number_count+1
    #   print(num)
print("Total number of count : ", positive_number_count )
