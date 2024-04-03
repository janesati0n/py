# # Shopping List
# shopping_list = ['applesauce', 'house plant', 'printer paper', 'protein powder', 'zebra print rug (faux)']
# arana = None
# while arana != 'q':
#   arana = input("Add something to the cart? Type q to quit: ")
#   shopping_list.append(arana)
# print("YOUR FINAL GROCERY LIST")
# for i in shopping_list:
#   print(i)

# # Iterating Over Lists
# colors = ['purple', 'teal', 'magenta']
# for color in colors:
#   print(color)

# numbers = [1, 2, 3, 4]
# i = 0
# while i < len(numbers):
#   print(numbers[i])
#   i += 1

# # List Methods: Append, Insert and Extend
# data = [1, 2, 3]
# data.append(4) # adds value to the end [1, 2, 3, 4]
# data.extend([5,6]) # adds multiple values to the end [1, 2, 3, 4, 5, 6]
# data.insert(2, 'Hi!') # [1, 2, 'Hi!', 3, 4, 5 ,6]

# # List Methods: Clear, Pop and Remove
# first_list = [1, 2, 3, 4]
# first_list.clear() # remove all []
# first_list.pop() # remove by index (default=last) [1, 2, 3]
# first_list.pop(1) # remove by index [1, 3, 4]
# first_list.remove(2) # remove by value (first to match) [1, 3, 4]

# # List Methods: Index, Count, Sort, Reverse, Join
# numbers = [5, 5, 6, 7, 5, 8, 8, 9, 10]
# numbers.index(6) # 2 //returns index of specified item
# numbers.index(5, 2) # 4 //specify starting point (from position 2)
# names = ['colt', 'blue', 'arya', 'lena', 'colt', 'selena', 'pablo']
# names.count('colt') # 2
# names.count('jared') # 0
# names.reverse() # names = ['pablo', 'selena'...]
# another_list = [6,4,1,2,5]
# another_list.sort()
# print(another_list) # [1,2,4,5,6]
# names.append('ARYA')
# names.sort() # ['ARYA', 'arya', 'blue'...]

# words = ['Coding', 'Is', 'Fun!']
# ' '.join(words) # 'Coding is Fun!'

# name = ['Mr', 'Steele']
# '. '.join(name) # 'Mr. Steele'
