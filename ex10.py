#palindrome

def user_input(name):
    reverse = name[::-1]
    if reverse == name:
        #return True
        print("Entered name is Palindrom")
    else:
        #return False
        print("Entered name is not Palindrom")
        
name = input("Enter the name: ")

print(user_input(name))