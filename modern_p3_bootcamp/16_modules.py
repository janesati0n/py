# # Working with Built-in Modules
# import random as rand
# print(rand.choice(["apple", "banana", "cherry", "durian"]))
# rand.shuffle(["apple", "banana", "cherry", "durian"])

# from random import choice, randint
# print(randint(1,100))
# print(shuffle(["apple", "banana", "cherry", "durian"])) # NameError

# from random import choice as gimme_one, shuffle as mix_up_fruits
# gimme_one(["apple", "banana", "cherry", "durian"])
# mix_up_fruits(["apple", "banana", "cherry", "durian"])

# # Coding Excercise 73: Built in Modules
# import math
# answer = math.sqrt(15129)

# # Coding Excercise 74: Slightly Tougher
# import keyword
# def contains_keyword(*args):
#   for item in args:
#     if keyword.iskeyword(item): return True
#   return False

# # Custom modules
### bananas.py ###
# def peel():
#   return "Here's a delicious banana!"
# def dip_in_chocolate():
#   return "Here's a delicious banana, dipped in chocolate!"
# def sell():
#   return "There's always money in the banana stand."

### apples.py ###
# def offer():
#   return "Hey, do you like apples?"
# def bake():
#   return "Mmmm, pie..."

### fruits.py ###
# import bananas
# import apples
# print(bananas.dip_in_chocolate())
# print(apples.offer())

### alternative take ###
# from bananas import dip_in_chocolate as dip
# print(dip())

# # Coding Excercise 75: Custom Module
### helpers.py ###
# def lucky_number():
#   return 37

### excercise.py ###
# import helpers
# num = helpers.lucky_number()

# # Installing External Modules and TermColor
# from termcolor import colored
# from colorama import init # use it to make termcolor work on Windows
# init()
# print(colored('Hello, World!', 'green', 'on_red'))

# print(dir(termcolor)) # show attributes in module
# help(termcolor) # show overview of functions in module

# from termcolor import colored
# text = colored('hi there!', color="magenta", on_color="on_cyan", attrs=["blink"])
# print(text)
