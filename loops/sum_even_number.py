# Calculate the sum of even numbers up to a given number n.
# n = int(input("Enter the number : "))
# sum = 0
# for num in range(1, n + 1):
#     if num % 2 == 0:
#         sum = sum + num
# print("Sum of even numbers:", sum)

n = 10
sum = 0
for num in range(1, n+1):
    if num % 2 == 0:
        sum = sum + num
print(sum)
