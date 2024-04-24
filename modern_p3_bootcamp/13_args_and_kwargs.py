# # Introduction to *args
# def sum_all_nums(*args):
#   total = 0
#   for num in args:
#     total += num
#   return total

# print(sum_all_nums(4,6,9,4,10))
# print(sum_all_nums(4,6))

# def ensure_correct_info(*args):
#   if "Colt" in args and "Steele" in args:
#     return "Welcome back Colt!"
#   return "Not sure who you are"

# print(ensure_correct_info("hello", False, 78)) # Not sure who you are
# print(ensure_correct_info(1, True, "Steele", "Colt")) # Welcome back Colt!

# # Coding Excercise 57: The Purple Test
# def contains_purple(*args):
#   if "purple" in args:
#     return True
#   return False

# # Introduction to **kwargs
# def fav_colors(**kwargs):
#   for person, color in kwargs.items():  # key, value = person, color
#     print(f"{person}'s favorite color is {color}")
# fav_colors(colt='purple', ruby='red', ethel='teal')

# def special_greeting(**kwargs):
#   if "David" in kwargs and kwargs ["David"] == "special":
#     return "You get a special greeting David!"
#   elif "David" in kwargs:
#     return f"{kwargs ['David']} David!"
#   return "Not sure who this is..."

# print(special_greeting(David='Hello')) # Hello David!
# print(special_greeting(Bob='hello')) # Not sure who this is...
# print(special_greeting(David='special')) # You get a special greeting David!

# # Coding Excercise 58: Kwargs
# def combine_words(word, **kwargs):
#   if 'prefix' in kwargs:
#     return kwargs['prefix'] + word
#   elif 'suffix' in kwargs:
#     return word + kwargs['suffix']
#   return word

# combine_words("child")  #'child'
# combine_words("child", prefix="man")  #'manchild'
# combine_words("child", suffix="ish")  #'childish'
# combine_words("work", suffix="er")  #'worker'
# combine_words("work", prefix="home")  #'homework'

# # Ordering Parameters
# def display_info(a, b, *args, instructor="Colt", **kwargs):
#   return [a,b,args,instructor,kwargs]
# print(display_info(1, 2, 3, last_name='Steele', job='Instructor'))
# a - 1
# b - 2
# args (3) # type - tuple
# instructor - "Colt"
# kwargs - {'last_name': "Steele", "job: Instructor"} # type - dictionary
# [1, 2, (3,), 'Colt', {'last_name': 'Steele', 'job': 'Instructor'}]

# # Tuple Unpacking
# def sum_all_values(*args):
#   total = 0
#   for num in args:
#     total += num
#   print(total)
# sum_all_values(4,8,6)
# nums = (1,2,3,4,5,6)
# sum_all_values(*nums) # # List/Tuple unpacking

# # Coding Excercise 59: Unpacking
# def count_sevens(*args):
#   return args.count(7)
# nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
# result1 = count_sevens(1,4,7)
# result2 = count_sevens(*nums)

# # Dictionary Unpacking
# def display_names(first, second):
#   print(f"{first} says hello to {second}")
# names = {"first": "Colt", "second": "Rusty"}
# display_names(first="Charlie", second="Sue")
# display_names(**names)

# def add_and_multiply_numbers(a,b,c,**kwargs):
#   print(a + b * c)
#   print("OTHER STUFF...")
#   print(kwargs)
# data = dict(a=1,b=2,c=3,d=55,name="Tony")
# add_and_multiply_numbers(**data, cat="Blue")

# # Coding Excercise 60: Calculate

