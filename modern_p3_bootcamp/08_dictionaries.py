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

# # Coding Excercise 26
# user_info = {
#     'username': 'nbusr',
#     'password': 'nbusr123',
#     'date_created': 2024-4-8
# }

# # Accessing Data in Dictionaries
# instructor['name'] # 'Colt'
# instructor['thing'] # KeyError

# # Coding Excercise 27
# artist = {
#     "first": "Neil",
#     "last": "Young",
# }

# full_name = artist['first'] + ' ' + artist['last'] # Solution 1: Concat method
# full_name = f"{artist['first']} {artist['last']}"  # Solution 2: F-string method
# full_name = "{} {}".format(artist["first"], artist["last"]) # Solution 3: Format method
