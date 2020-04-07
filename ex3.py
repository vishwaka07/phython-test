#Take 2 inputs from user , one as username and another as a single character

# In output print 2 lines
#1. username length
#2. count of the character

NAME , CHAR = input("Enter the username and character :").split( )
print(f"Length of the username is {len(NAME)}")
print(f"No. of times character used in username is : {NAME.count(CHAR)}")
#now count should be case insenstive
# NAME.lower() CHAR.lower()
# NAME.lower().count(CHAR.lower())
print(f"No. of times character used in username is : {NAME.lower().count(CHAR.lower())}")
