# # Defining Functions
# def sing_happy_birthday():
#   print('Happy Birthday To You')
#   print('Happy Birthday To You')
#   print('Happy Birthday Dear You')
#   print('Happy Birthday To You')
# sing_happy_birthday()

# # Coding Excercise 37: Your first function
# def make_noise():
#     print('THE CROWD GOES WILD')
# make_noise()

# # The Magical Return Keyword
# def square_of_7():
#   return 7**2
# result = square_of_7()
# print(result)

# # Writing a coin_flip Function Using Random
# from random import random

# def flip_coin():
#   if random() > 0.5:
#     return "Heads"
#   else:
#     return "Tails"
# print(flip_coin())

# # Coding Excercise 38: Super Quick Return Excercise
# def speak_pig():
#     return 'oink'
# speak_pig()

# # Coding Excercise 39: Generating Evens Excercise
# def generate_evens():
#   return [num for num in range(1,50) if num % 2 == 0] # using list comprehension

# def generate_evens():
#   result = []
#   for x in range(1,50):   # using a loop
#     if x % 2 == 0:
#       result.append(x)
#   return result

# # Parameters
# def square(num):
#   return num * num
# print(square(4))
# print(square(8))

# def sing_happy_birthday(name):
#   print('Happy Birthday To You')
#   print('Happy Birthday To You')
#   print(f'Happy Birthday Dear {name}')
#   print('Happy Birthday To You')
# sing_happy_birthday('Rashida')
# sing_happy_birthday('Nicolas')

# # Parameters vs Arguments
# def divide(num1, num2):
#   return num1/num2
# print(divide(2,5))
# print(divide(5,2))

# # Coding Excercise 40: Yell Function Excercise
# def yell(string):
#     return string.upper() + "!"     # variant A: string concatenation
#     return "{}!".format(word.upper())   # variant B: format method
#     return f"{word.upper()}!"       # variant C: f-string

# # Common Return Mistakes
# def sum_odd_numbers(numbers):
#   total = 0
#   for num in numbers:
#     if num % 2 != 0:
#       total += num
#   return total      # mind the indentation

# print(sum_odd_numbers([1,2,3,4,5,6,7]))

# def is_odd_number(num):
#   if num % 2 != 0:
#     return True
#   return False    # avoid unnecessary "else"
# print(is_odd_number(4))
# print(is_odd_number(9))

# # Coding Excercise 41: Fix this function!
# def count_dollar_signs(word):
#     count = 0
#     for char in word:
#         if char == '$':
#             count += 1
#     return count

# # Default Parameters
