# # Lambdas
# def square(num): return num * num
# square2 = lambda num: num * num
# add = lambda a,b: a + b

# # Coding Excercise 61: Lambda
# cube = lambda num: num ** 3

# # Map
# nums = [2,4,6,8,10]
# doubles = list(map(lambda x: x*2,nums))
# doubles # [4, 8, 12, 16, 20]

# people = ['Darcy', 'Christina', 'Dana', 'Annabel']
# peeps = list(map(lambda name: name.upper(), people))
# peeps # ['DARCY', 'CHRISTINA', 'DANA', 'ANNABEL']

# names = [
#   {'first':'Rusty', 'last':'Steele'},
#   {'first':'Colt', 'last':'Steele'},
#   {'first':'Blue', 'last':'Steele'}
# ]
# first_names = list(map(lambda x: x['first'], names))
# first_names # ['Rusty', 'Colt', 'Blue']

# def double(x): return x*2
# doubles = map(double, nums)
# list(doubles) # [4, 8, 12, 16, 20]

# # Coding Excercise 62: Map Time Excercise
# def decrement_list(arana):
#   return list(map(lambda x: x-1, arana))

# # Filter
# l = [1,2,3,4]
# evens = list(filter(lambda x: x % 2 == 0, l))
# print(evens) # [2,4]

# names = ['austin', 'penny', 'anthony', 'angel', 'billy']
# a_names = filter(lambda n: n[0]=='a', names)
# print(list(a_names))

# users = [
#   {'username': 'samuel', 'tweets': ['I love cake', 'I love pie']},
#   {'username': 'katie', 'tweets': ['I love my cat']},
#   {'username': 'jeff', 'tweets': []},
#   {'username': 'bob123', 'tweets': []},
#   {'username': 'doggo_luvr', 'tweets': ['dogs are the best']},
#   {'username': 'guitar_gal', 'tweets': []}
# ]
# inactive_users = [user for user in users if not user['tweets']] # using list comprehension
# inactive_users = list(map(lambda user: user['username'].upper(),
#     filter(lambda u: not u['tweets'], users)))
# print(inactive_users)

# # Coding Excercise 63: Filter Excercise
# def remove_negatives(nums):
#   return list(filter(lambda n: n >= 0, nums))

# # Any and All
# people = ['Charlie', 'Casey', 'Cody', 'Carly', 'Cristina']
# print (all([name[0] == 'C' for name in people])) # True
# print ([name[0] == 'C' for name in people]) # [True, True, True, True, True]

# # Generator Expressions and Using sys.getsizeof
# import sys
# list_comp = sys.getsizeof([x * 10 for x in range(1000)])
# gen_exp = sys.getsizeof(x * 10 for x in range(1000))
# print('To do the same thing, it takes...')
# print(f"List Comprehension: {list_comp} bytes")
# print(f"Generator Expression: {gen_exp} bytes")

# # Coding Excercise 64: Any/All Excercise
# def is_all_strings(lst):
#   return all(type(l) == str for l in lst)

# # Sorted
# more_numbers = [6,1,8,2]
# sorted(more_numbers) # [1,2,6,8]
# print(more_numbers) # [6,1,8,2]

# more_numbers.sort() # LIST SPECIFIC METHOD !!!
# print(more_numbers) # [1,2,6,8]

# sorted(more_numbers, reverse=True) # [8,6,2,1]

# sorted((4,6,1,30,55,23)) # [1,2,23,45,99] # WORKS ON TUPLES ASWELL !!!

# users = [
#   {'username': 'samuel', 'tweets': ['I love cake', 'I love pie']},
#   {'username': 'katie', 'tweets': ['I love my cat']},
#   {'username': 'jeff', 'tweets': []},
#   {'username': 'bob123', 'tweets': []},
#   {'username': 'doggo_luvr', 'tweets': ['dogs are the best']},
#   {'username': 'guitar_gal', 'tweets': []}
# ]
# print(sorted(users,key=lambda user: user['username']))
# print(sorted(users,key=lambda user: user['username'], reverse=True))

# songs = [
#   {'title':'happy birthday', 'playcount':1},
#   {'title':'Survive', 'playcount':6},
#   {'title':'YMCA', 'playcount':99},
#   {'title':'Toxic', 'playcount':31}
# ]
# print(sorted(songs, key=lambda song: song['playcount'], reverse=True))

# # Min and Max
# max(3,67,99) # 99
# max('c','d','a') # d
# max('awesome') # 'w'
# max({1:'a',3:'c',2:'b'}) # 3
# max((3,5,23,65)) # 65


# nums = [40,32,6,5,10]
# max(nums) # 40
# min(nums) # 5

# names = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
# min(names) # 'Arya'
# max(names) # 'Tim'
# min(len(name) for name in names) # 3
# max(names, key=lambda n:len(n)) # 'Ollivander'

# songs = [
#   {'title':'happy birthday', 'playcount':1},
#   {'title':'Survive', 'playcount':6},
#   {'title':'YMCA', 'playcount':99},
#   {'title':'Toxic', 'playcount':31}
# ]
# print(min(songs, key=lambda s: s['playcount'])) # {'title': 'happy birthday', 'playcount': 1}
# print(max(songs, key=lambda s: s['playcount'])['title']) # YMCA

# # Excercise 65: Extremes Excercise (Using min and max)
# def extremes(nums):
#   return (min(nums), max(nums))

# # Reversed
# nums = [1,2,3,4]
# nums.reverse()
# print(nums) # [4,3,2,1]
# print(list(reversed(nums))) # [1,2,3,4]

# for x in reversed(range(0,10)):
#   print(x)
# 9
# 8 (...) 0

# # Len() and a Special Sneak Peak of OOP!
