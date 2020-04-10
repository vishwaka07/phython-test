# list vs array
#array defines ordered data either in the form of int or string
#list defined ordered data any type

# strings are immutable
# lists are mutable

# list in list is call 2d list
# L = [[1,2,3],[4,5,6],[7,8,9]]
# if you want to print 5 then u have use L[1][1] (second sublist second sublist item)

#use "type" to check data type
s = 'string'
i = 24
print(type(s))
print(type(i))

#generate list with range function

numbers = list(range(1,11))
print(numbers)