# # Tuple Looping and Methods
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

# for month in months:
#   print(month)

# i = len(months) -1
# while i >= 0:
#   print(months[i])
#   i -= 1

# x = (1,2,3,3,3)
# x.count(1) # 1
# x.count(3) # 3

# t = (1,2,3,3,3)
# t.index(1) # 0
# t.index(5) # ValueError
# t.index(3) # 2 (first matching index)

# # Introduction to Sets
# s = set({1,4,5}) # syntax
# s = {1,4,5} # syntax

# cities = {'Los Angeles', 'Boulder', 'Kyoto', 'Florence', 'Santiago', 'Los Angeles', 'Shanghai', 'Kyoto', 'Oslo', 'Tokyo', 'San Francisco'}
# print(list(set(cities)))
# print(len(set(cities)))

# # Set Methods and Set Math
# s = set([1,2,3])
# s.add(4) # {1,2,3,4}
# set1 = {1,2,3,4,5,6}
# s.remove(3) # {1,2,4,5,6}
# another_s = s.copy() # {1,2,3}
# s.clear() # set()

# math_students = {'Matthew', 'Helen', 'Prashant', 'James', 'Aparna'}
# biology_students = {'Jane', 'Matthew', 'Charlotte', 'Mesut', 'Oliver', 'James'}
# math_students | biology_students # UNION (combine both sets)
# {'Charlotte', 'Prashant', 'Jane', 'James', 'Oliver', 'Mesut', 'Helen', 'Aparna', 'Matthew'}

# math_students & biology_students # SET INTERSECTIONS
# {'James', 'Matthew'}

# # Coding Excercise 36: Tuples and Sets Excercise
# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
# numbers = (1,2,3,4)
# 2 - Create a variable called value which is a tuple with the the value 1 inside.
# value = (1,)
# 3 - Given the following variable:
# values = [10,20,30]
# Create a variable called static_values which is the result of the values variable converted to a tuple
# static_values = tuple(values)
# 4 - Given the following variable
# stuff = [1,3,1,5,2,5,1,2,5]
# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
# unique_stuff = set(stuff)

# # Set Comprehension
# {x**2 for x in range(10)}
# {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
# {x:x**2 for x in range(10)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# {char.upper() for char in 'hello'}
# {'O', 'L', 'H', 'E'}

# string = 'sequoia'
# len({char for char in string if char in 'aeiou'}) == 5 # check if string has all 5 vowels
# True
