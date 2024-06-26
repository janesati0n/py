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
# len('awesome') # 7
# len((1,2,3,4)) # 4
# len([1,2,3,4]) # 4
# len(range(1,10)) # 10
# len({1,2,3,4}) #
# len({'a':1, 'b':2, 'c':2}) # 3

# # Abs(), Sum() and Round()
# abs(-5) # 5 # absolutna hodnota
# abs(5) # 5
# abs(float('20')) # 20.0

# import math
# math.fabs(-4) # 4.0

# sum([1,2,3]) # 6
# sum([1,2,3], 10) # 16
# sum((1.5,2,3.7)) # 7.2

# round(10.2) # 10
# round(1.212121, 2) # 1.21

# # Coding Excercise 66: Greatest Magnitude Excercise
# def max_magnitude(nums):
#   return max(abs(num) for num in nums)

# # Coding Excercise 67: Sum Even Values
# def sum_even_values(*args):
#   return sum(arg for arg in args if arg % 2 == 0)

# # Coding Excercise 68: Sum Floats
# def sum_floats(*args):
#   return sum(arg for arg in args if type(arg) == float)

# # Zip Basics
# first_zip = zip([1,2,3], [4,5,6])
# list(first_zip) # [(1,4), (2,5), (3,6)]
# dict(first_zip) # {1: 4, 2: 5, 3: 6}

# five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
# list(zip(*five_by_two)) # [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]

# # More Complex Zip Examples
midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

# v1
# final_grades = [pair for pair in zip(midterms, finals)]
# print(final_grades) # [(80, 98), (91, 89), (78, 53)]

# v2
# final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}
# print(final_grades) # {'dan': 98, 'ang': 91, 'kate': 78}

# v3
# scores = map(
#   lambda pair: max(pair),
#   zip(midterms, finals)
# )
# print(list(scores))

# v4
# final_grades = dict(
#   zip(
#     students,
#     map(
#       lambda pair: max(pair),
#       zip(midterms, finals)
#     )
#   )
# )
# print(final_grades)

# v5
# avg_grades = dict(
#   zip(
#     students,
#     map(
#       lambda pair: ((pair[0] + pair[1])/2),
#       zip(midterms, finals)
#     )
#   )
# )
# print(avg_grades)

# # Coding Excercise 69: Interleaving String
# def interleave(str1,str2):
#   return ''.join(''.join(x) for x in (zip(str1,str2)))
# interleave('hi', 'ha') # hhia
# interleave('aaa', 'zzz') # azazaz
# interleave('lzr', 'iad') # lizard

# # Coding Excercise 70: triple_and_filter
# def triple_and_filter(lst):
#   return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))

# triple_and_filter([1,2,3,4]) # [12]
# triple_and_filter([6,8,10,12]) # [24,36]

# # Coding Excercise 71: extract_full_name
# def extract_full_name(l):
#   return list(map(lambda val: f"{val['first']} {val['last']}", l))

# names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
# extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
