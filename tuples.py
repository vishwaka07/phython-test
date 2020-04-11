# tuples is also a data structure, can store any type of data
# most important tuple is immutable
# u cannot update data inside the tuple
# no append, no remove, no pop, no insert

example = ( '1','2','3')
#when to use : days , month
#tuples are faster than lists
#methods that can be used in tuples : count,index, len function,slicing

#tuple with one element
num = (1,)
print(type(num))

# tuple without parenthesis "()"
guitar = 'yamaha','base'
print(type(guitar))

#tuple unpacking
guitarist = ('hello1','hello2','hello3')
name1,name2,name3 = (guitarist)
print(name1)

#list inside the tuple

#function returning two values means its gives output in tuple 
#so we have to store data in two variable

def func(int1,int2):
    add = int1 + int2
    multiply = int1*int2
    return add,multiply

add, multiply = func(2,3)
print(add)
print(multiply)

# tuple can be use with range as 
num = tuple(range(1,11))
print(num)

#convert tuple into list
nums = list((1,2,3,4,5,6))
print(nums)

#convert tuple into str
nums1=str((1,2,3,4,5,6))
print(nums1)