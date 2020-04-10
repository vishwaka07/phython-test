#define a function which will take list as an argument and 
# this function will reutrn reverse of list
#[1,2,3,4] --> [4,3,2,1]

def reverse_list(l):
    l.reverse()
    return l

numbers = list(range(1,5))
print(reverse_list(numbers))

## best way

def reverse_list1(l):
    return l[::-1]

numbers1 = list(range(1,5))
print(reverse_list1(numbers1))

## using append and pop method
def reverse_list2(l):
    r_list=[]
    for k in range(len(l)):
        popped_item = l.pop()
        r_list.append(popped_item)
    return r_list

numbers2 = list(range(1,5))
print(reverse_list2(numbers2))
