# # Spotify Playlist Example
# playlist = {
#   'title': 'Patagonia Bus',
#   'author': 'Colt Steele',
#   'songs': [
#     {'title': 'Turn it Off',
#      'artist': ['Culture Abuse'],
#      'duration': 3.37},
#     {'title': 'Eating Hooks - Siriusmo Remix - Solomun Edit',
#      'artist': ['Moderat', 'Siriusmo', 'Solomun'],
#      'duration': 7.02},
#      {'title': 'Nights Off',
#      'artist': ['Siriusmo'],
#      'duration': 4.08},
#      {'title': 'Tilted - Paradis Remix',
#      'artist': ['Christine and the Queens', 'Paradis'],
#      'duration': 5.50},
#      {'title': "Dont't Stop",
#      'artist': ['Knightlife'],
#      'duration': 6.13},
#      {'title': 'Each Moment Like The First',
#      'artist': ['James Holden', 'The Animal Spirits'],
#      'duration': 4.57},
#      {'title': 'Renata',
#      'artist': ['James Holden'],
#      'duration': 5.57},
#      {'title': 'Sad Saturdays',
#      'artist': ['JOBA'],
#      'duration': 4.27},
#      {'title': 'Give It To Me (Like You Mean It)',
#      'artist': ['Cub Sport'],
#      'duration': 2.50},
#      {'title': 'Wasted Days',
#      'artist': ['Cloud Nothings'],
#      'duration': 8.54}
#   ]
# }

# for song in playlist['songs']:
#   print(song['title'])

# # Dictionary Comprehension
# str1 = "ABC"
# str2 = "123"
# combo = {str1[i]: str2[i] for i in range(0, len(str1))}
# print(combo) # # {'A': '1', 'B': '2', 'C': '3'}

# instructor = {'name': 'Colt', 'city': 'San Francisco', 'color': 'purple'}
# yelling_instructor = {k.upper():v.upper() for k, v in instructor.items()}
# print(yelling_instructor) # {'NAME': 'COLT', 'CITY': 'SAN FRANCISCO', 'COLOR': 'PURPLE'}

# yelling_instructor = {(k.upper() if k is 'color' else k):v.upper() for k, v in instructor.items()}
# print(yelling_instructor) # {'name': 'COLT', 'city': 'SAN FRANCISCO', 'COLOR': 'PURPLE'}

# num_list = [1, 2, 3, 4]
# num_is_odd = {num: ('even' if num % 2 == 0 else 'odd') for num in num_list}
# print(num_is_odd) # {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}

# # Coding Excercise 32: State Abbreviations Excercise
# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]
# answer = {list1[i]: list2[i] for i in range(0, len(list1))}
# print(answer)

# dict(zip(list1,list2)) # zip method /not covered yet/

# # Coding Excercise 33: List to Dictionary Excercise
# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# answer = {thing[0]: thing[1] for thing in person} # Solution 1: Dictionary comprehension
# answer = {k:v for k,v in person} # Solution 2: Without references to list indexes
# answer = dict(person) # Solution 3: Simple and elegant (if you have list of pairs)

# # Coding Excercise 34: Vowels Dict Excercise

