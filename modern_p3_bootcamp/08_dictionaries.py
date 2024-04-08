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

# # Coding Excercise 30: Fromkeys Excercise
# game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"]
# initial_game_state = dict.fromkeys(game_properties, 0)

# # Dictionary Methods: Pop, Popitems and Update
# d = dict('a'=1, 'b'=2, 'c'=3)
# d.pop() # TypeError: pop expected at least 1 arguments, got 0
# d.pop('a') # 1 # Takes argument and removes key-value pair
# d # {'c': 3, 'b': 2}
# d.pop('e') # KeyError

# d = dict('a'=1, 'b'=2, 'c'=3, 'd'=4, 'e'=5)
# d.popitem() # ('d', 4) # Removes random key in a dictionary
# d.popitem('a') # TypeError: popitem() takes no argument (1 given)

# first = dict('a'=1, 'b'=2, 'c'=3, 'd'=4, 'e'=5)
# second = {}
# second.update(first)
# second # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# second['a'] = "AMAZING" # overwrites an existing key
# second.update(first) # the update overrides our values
# second # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# # Coding Exercise 31: Dictionary Methods Excercise
# inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}
# stock_list = inventory.copy() # Make a copy of inventory and save it to a variable called stock_list
# stock_list['cookie'] = 18 # Add the value 18 to stock_list under the key "cookie"
# stock_list.pop('cake') # Remove 'cake' from stock_list
