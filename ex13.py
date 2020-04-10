# define a function that take list of words as argument and 
# return list with reverse of every element in that  list
# ['abc','xyz']  --> ['cba','zyx']

def reverse_list(l):
    r_list = []
    for i in l:
        r_list.append(i[::-1])
    return r_list

words = ['abc','xyz']
print(reverse_list(words))