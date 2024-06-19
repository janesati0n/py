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
