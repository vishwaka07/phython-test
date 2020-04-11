#define a function that takes a number(n)
#return a dictionary containing cube of numbers from 1 to n

def cube_finder(n):
    cube_dict={}
    for i in range(1,n+1):
       cube_dict[i] = i**3
    return cube_dict

number = int(input("Enter any no.: "))
print(cube_finder(number))