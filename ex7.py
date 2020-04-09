# ask user to enter the number with more than one digit
# example 12345 and get them added as 1+2+3+4+5 and prin the total

number = input("Enter the number: " )
total = 0
i = 0
while i < len(number):
    total = total + int(number[i])
    i = i + 1
print(f"sum is {total}")
