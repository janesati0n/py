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
