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
