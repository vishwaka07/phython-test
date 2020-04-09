# AND & OR operator
# AND : all the condition should be true
# OR :  atleast one condition should be true
# Excersie WATCH MOVIE
# Ask user name and age
# if user name starts with 'a' or 'A' and age is above 10 then
# print u can  watch movie
# else print u cannot watch movie

name = input("Enter your name: ")
age = input("Enter your age: ")
age = int(age)
if age >= 10 and (name[0]=='a' or name[0]=='A'):
    print("You can watch movie")
else:
    print("You are not allowed")
        



