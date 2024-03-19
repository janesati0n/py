# # Getting User Input
# print("What's your favorite color: ")
# data = input()
# print("You said " + data)

# # Intro to Conditionals
# print("What is your name?")
# name = input()
# if name == "Arya Stark":
#   print("Valar Morghulis")
# elif name == "Jon Snow":
#   print("You know nothing")
# else:
#   print("Carry on")

# # Coding Excercise 8: Lucky Number 7
# from random import randint
# choice = randint(1,10)
# if choice == 7:
#     print("lucky")
# else:
#     print("unlucky")

# # Coding Excercise 9: Number is Odd
# from random import randint
# num = randint(1, 1000) #picks random number from 1-1000
# if num % 2 == 1:
#     print("odd")
# else:
#     print("even")

# # Multiple Elifs
# color = input("What's your favorite color?")
# if color == 'purple':
#   print("Excellent choice!")
# elif color == 'teal':
#   print("Not bad!")
# elif color == 'seafoam':
#   print("Mediocre")
# elif color == 'pure darkness':
#   print("I like how you think")
# else:
#   print("YOU MONSTER!")

# # A Word on Truthiness
# print("Enter your favorite animal")
# animal = input()
# if animal:
#   print(animal + " is my favorite too!")
# else:
#   print("You didn't say anything!")

# # Logical AND & OR
# city = input("Where do you live? ")
# if city == "los angeles" or city == "san francisco":
#   print("YOU LIVE IN CALIFORNIA!")
# else:
#   print("YOU LIVE SOMEWHERE ELSE!")

# # Coding Excercise 10: Food Classifying Excercise
# from random import choice
# food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])
# if food == 'apple' or 'grape':
#     print('fruit')
# elif food == 'bacon' or 'steak':
#     print('meat')
# else:
#     print('yuck')

# Logical NOT
