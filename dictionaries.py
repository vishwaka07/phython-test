#why we use dictionaries?
#  because of list limitation, list are not enough to represent real  data

#what are dictionaries?
#unordered collection of data in key:value pair

#how to create dictionaries?
user = {'name':'shlok','age': 2}
print(user)

#second method 
user1 = dict(name = 'shlok', age = 3)
print(user1)

#how add data in empty dictionaries
user_info2 = {}
user_info2['name'] = 'Shlok'
print(user_info2)


# looping and in keyword
#for i in user_info:
#    print(i)

#only values
#for i in user_info.values():
#    print(i)


# how to add,delete data in dictionaries

user_info = {
  'name':'Shlok',
  'age': 2,
  'fav_movie':['kk','bb','aa'],
  'fav_tunes':['tt','yy'],
}

#how to add data
user_info['fav_song'] = ['song1','song2']
print(user_info)
#pop method
#user_info.pop('fav_tunes')
popped_item = user_info.pop('fav_tunes')
print(user_info)

#popitem method : when you want to remove random item
