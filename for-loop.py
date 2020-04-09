# 'range' in for loop

for i in range(10):
    print("Hello World")

## Adding 1 to 10
total=0
for i in range(1,11):
    total = total + i
print(total)


## ask user input like 123456
## calculate sum of digits
num = input("Enter the digit: ")
total = 0
for i in range(0, len(num)):
    total = total + int(num[i])

print(total)


## ask username and count each character
## Krishna kumar
name = input("Enter username: ")
temp = ""
for i in range(0, len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        
