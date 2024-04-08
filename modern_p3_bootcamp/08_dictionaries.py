# # Creating Dictionaries
# instructor = {
#   "name": "Colt",
#   "owns_dog": True,
#   "num_courses": 4,
#   "favorite_language": "Python",
#   "is_hilarious": False,
#   44: "my favorite number!"
# }

# cat = dict(name ='kitty')
# cat = dict(name ='kitty', age=0.5)

# # Coding Excercise 26: Dictionary Creation Excercise
# user_info = {
#     'username': 'nbusr',
#     'password': 'nbusr123',
#     'date_created': 2024-4-8
# }

# # Accessing Data in Dictionaries
# instructor['name'] # 'Colt'
# instructor['thing'] # KeyError

# # Coding Excercise 27: Access Data in Dictionary Excercise
# artist = {
#     "first": "Neil",
#     "last": "Young",
# }

# full_name = artist['first'] + ' ' + artist['last'] # Solution 1: Concat method
# full_name = f"{artist['first']} {artist['last']}"  # Solution 2: F-string method
# full_name = "{} {}".format(artist["first"], artist["last"]) # Solution 3: Format method

# # Iterating Dictionaries
# for value in instructor.values():
#   print(value)

# for key in instructor.keys():
#   print(key)

# for key, value in instructor.items(): # items = keys + values
#   print(key, value)

# # Coding Excercise 28: Totaling Donations Excercise
# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# total_donations = 0
# for value in donations.values():
#     total_donations += value

# total_donations = sum(donations.values()) # Better method, not covered yet

# # Using In With Dictionaries
# "name" in instructor # True
# "awesome" in instructor # False

# # Dictionary Methods: Clear, Copy, Fromkeys and Get
# d = dict(a=1, b=2, c=3)
# d.clear() # Clears all the keys and values in a dictionary
# d # {}

# c = d.copy() # Makes a copy of a dictionary
# c # {'a': 1, 'b': 2, 'c': 3}
# c is d # False

# {}.fromkeys("a", "b") # {'a': 'b'}
# {}.fromkeys("email", "unknown") # {'email': 'unknown'}
# {}.fromkeys("a", "[1,2,3,4,5]") # {'a': '[1, 2, 3, 4, 5]'}

# d[a] # 1
# d.get('a') # 1
# d['jibberish'] # KeyError
# d.get('jibberish') # None

# # Coding Excercise 29: Dictionary Access
# from random import choice
# food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"])

# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }

# if bakery_stock.get(food):
#     print(f"{bakery_stock.get(food)} left")
# else:
#     print("We don't make that")
