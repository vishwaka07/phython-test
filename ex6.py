# sum of n natural numbers
# ask user for natural number (n)
# print total from 1 to n

natural_number = input("Enter the natural number: ")
natural_number = int(natural_number)
total = 0
i = 1
while i<=natural_number:
    total = total + i
    i = i + 1
print(f"Sum of natural number is : {total}")
    