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
