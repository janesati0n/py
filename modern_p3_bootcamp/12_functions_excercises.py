# # Coding Excercise 43: Product
# def product(num1, num2):
#     return num1 * num2
# product(2,2) # 4
# product(2,-2) # -4

# # Coding Excercise 44: Return Day
# def return_day(x):
#     days = {1:'Sunday', 2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday', 7:'Saturday'}
#     return days.get(x)

# return_day(1) # "Sunday"
# return_day(7) # "Saturday"
# return_day(41) # None

# # Coding Excercise 45: Last Element
# def last_element(l):
#     if l:
#         return l[-1]
#     else:
#         return None
# last_element([1,2,3]) # 3
# last_element([]) # None

# # Coding Excercise 46: Compare numbers
# def number_compare(a,b):
#     if a > b:
#         return 'First is greater'
#     elif a < b:
#         return 'Second is greater'
#     return 'Numbers are equal'
# number_compare(1,1) # "Numbers are equal"
# number_compare(1,0) # "First is greater"
# number_compare(2,4) # "Second is greater"

# # Coding Excercise 47: Single Letter Count
# def single_letter_count(string,letter):
#   return string.lower().count(letter.lower())
# single_letter_count("Hello World", "h") # 1
# single_letter_count("Hello World", "z") # 0
# single_letter_count("HelLo World", "l") # 3

# # Coding Excercise 48: Multiple Letter Count
# def multiple_letter_count(string):
#     return {char:string.count(char) for char in string}
# multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}

# # Coding Excercise 49: List Manipulation
# def list_manipulation(collection, command, location, value=None):
#     if(command == "remove" and location == "end"):
#         return collection.pop()
#     elif(command == "remove" and location == "beginning"):
#         return collection.pop(0)
#     elif(command == "add" and location == "beginning"):
#         collection.insert(0,value)
#         return collection
#     elif(command == "add" and location == "end"):
#         collection.append(value)
#         return collection
# list_manipulation([1,2,3], "remove", "end") # 3
# list_manipulation([1,2,3], "remove", "beginning") #  1
# list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
# list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]

# # Coding Excercise 50: Palindrome
# def is_palindrome(string):
#     stripped = string.replace(" ", "").lower()
#     return stripped == stripped[::-1]
# is_palindrome('testing') # False
# is_palindrome('tacocat') # True
# is_palindrome('amanaplanacanalpanama') # True
# is_palindrome('a man a plan a canal panama') # True

# # Coding Excercise 51: Frequency
# def frequency(collection, search_term):
#     return collection.count(search_term)
# frequency([1,2,3,4,4,4], 4) # 3
# frequency([True, False, True, True], False) # 1

