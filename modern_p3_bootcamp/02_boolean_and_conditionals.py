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

# # Logical NOT
# age = 21
# if not ((age >= 2 and age <= 8) or age >= 65):
#   print("You are not a child or senior! You pay 10$!")
# else:
#   print("You are a child or senior!")

# # Bouncer Code-Along
# age = input("How old are you: ")
# if age:
#   age = int(age)
#   if age >= 18 and age < 21:
#     print("You can enter, but you need a wristband!")
#   elif age >= 21:
#     print('You are good to enter and can drink!')
#   else:
#     print("You are too young, can't come in, sorry!")
# else:
#   print('Please enter an age!')

# age = input("How old are you: ")
# if age:
#   age = int(age)
#   if age >= 21:
#     print('You are good to enter and can drink!')
#   elif age >= 18:
#     print("You can enter, but you need a wristband!")
#   else:
#     print("You are too young, can't come in, sorry!")
# else:
#   print('Please enter an age!')

# # Coding Excercise 11: Positive or Negative Checking
# from random import randint
# x = randint(-100, 100)
# while x == 0:
#     x = randint(-100, 100)
# y = randint(-100, 100)
# while y == 0:
#     y = randint(-100, 100)
# if x > 0 and y > 0:
#     print("both positive")
# elif x < 0 and y < 0:
#     print("both negative")
# elif x > 0 and y < 0:
#     print("x is positive and y is negative")
# else:
#     print("y is positive and x is negative")

# # Coding Excercise 12: Calling in Sick
# from random import choice, randint
# actually_sick = choice([True, False])
# kinda_sick = choice([True, False])
# hate_your_job = choice([True, False])
# sick_days = randint(0, 10)
# calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!
# if actually_sick and sick_days != 0:
#     calling_in_sick = True
# elif kinda_sick and hate_your_job and sick_days != 0:
#     calling_in_sick = True
# else:
#     calling_in_sick = False

