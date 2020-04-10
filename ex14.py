#create function for odd even 
# print output as [[1,3,5],[2,4,6]]

def odd_even(l):
    odd_list = []
    even_list =[]
    for i in l:
        if i%2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    output = [odd_list,even_list]
    return output

number = [1,2,3,4,5,6,7,8]
print(odd_even(number))