# define a function which takes list containing numbers a input
# and return a list containing square of every element
# input list [1,2,3,4]
# return list [1,4,9,16]

def square_list(l):
    square = []
    for i in l:
        square.append(i**2)
    return square

numbers = list(range(1,11))
print(square_list(numbers))