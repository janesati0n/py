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
