# # Common Types of Errors
# SyntaxError # typos # incorrect syntax
  #def name(( # SyntaxError

# NameError # var not defined
  # test # NameError

# TypeError # operation or function on wrong type
  # len(5) # TypeError

# IndexError # invalid index (f.e. out of range of list)
  # list = ['hello']
  # list[2] # IndexError

# ValueError # argument has right type but inappropriate value
  # int('foo') # ValueError

# KeyError # dictionary does not have a specific key
  # d = {}
  # d ['foo'] # KeyError

# AttributeError # var does not have an attribute
  # 'awesome'.foo # AttributeError

# # Raising Our Own Errors
# def colorize(text, color):
#   colors = ("cyan", "yellow", "blue", "green", "magenta")
#   if type(color) is not str:
#     raise TypeError("color must be instance of str")
#   if type(text) is not str:
#     raise TypeError("text must be instance of str")
#   if color not in colors:
#     raise ValueError("color is invalid color")
#   print(f"Printed {text} in {color}")
# colorize("hello", "magenta") # Printed hello in magenta
# colorize(34, "magenta") # TypeError: text must be instance of str
# colorize("hello", "red") # ValueError: color is invalid color

# # Try and Except Blocks
# try:
#   foobar
# except:
#   print('PROBLEM!')
# print('after the try')

# def get(d,key):
#   try:
#     return d[key]
#   except KeyError:
#     return None

# d = {'name': 'Ricky'}
# print(get(d, 'name')) # Ricky
# print(get(d, 'city')) # None

# # Try, Except, Else and Finally!
# while True:
#   try:
#     num = int(input('Please enter a number: '))
#   except ValueError:
#     print("That's not a number!")
#   else:
#     print("Good boy, you entered a number!") # if not in except, we will be here
#     break
#   finally:
#     print("I'll run no matter what!")
# print("REST OF GAME LOGIC RUNS!")

# def divide(a,b):
#   try:
#     return a/b
#   except:
#     print("Something went wrong!")
# print(divide(1,2))
# print(divide(1,0))

# def divide(a,b):
#   try:
#     return a/b
#   except ZeroDivisionError:
#     print("Don't divide by zero please!")
#   except TypeError:
#     print("a and b must be ints or floats")
# print(divide(1,2))
# print(divide(1,0))
# print(divide(1,'a'))

# def divide(a,b):
#   try:
#     result = a/b
#   except (ZeroDivisionError, TypeError) as err:
#     print("Something went wrong!")
#     print(err)
#   else:
#     print(f"{a} divided by {b} is {result}")
# print(divide(1,2))
# print(divide(1,0))
# print(divide(1,'a'))

# # Debugging with PDB
# Common PDB commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)

# import pdb
# pdb.set_trace()
# first = "First"
# second = "Second"
# result = first + second
# third = "Third"
# result += third
# print(result)

# def add_numbers(a,b,c,d)
#   import pdb; pdb.set_trace()
#   return a + b + c + d
