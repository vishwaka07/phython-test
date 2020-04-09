#check whether string contains character or letter
# how to use "in" with if statement
STRING ,KEY = input("Enter the string with key to search: ").split(" ")
if KEY in STRING:
    print(f"{KEY} present")
else:
    print(f"{KEY} is not present")
