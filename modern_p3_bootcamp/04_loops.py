# # For Loops
# for number in range(1, 8):
#   print(number)

# for char in 'coffee':
#   print(char)

# # Ranges
# range(7)      # 0,1,2,3,4,5,6
# range(1,8)    # 1,2,3,4,5,6,7
# range(1,10,2) # 0,2,4,6,8,10
# range(7,0,-1) # 7,6,5,4,3,2,1

# # Coding Excercise 13: For Loop and Range
# x = 0
# for i in range(11,21,2):
#   x += i
#   print(i)

# # Excercise: Screaming Repeating
# times = input('How many times do I have to tell you? ')
# times = int(times)
# for i in range(times):
#   print('CLEAN UP YOUR ROOM!')

# # Excercise: Unlucky numbers
# for num in range(1,21):
#   if num == 4 or num == 13:
#      state = 'unlucky'
#   elif num % 2 == 0:
#     state = 'even'
#   else:
#     state = 'odd'
#   print(f'{num} is {state}')

# # WHILE LOOPS
# msg = input("Ake je carovne slovicko? ")
# while msg != 'prosim':
#   print('NESPRAVNE')
#   msg = input("Ake je carovne slovicko? ")
# print('No vidis ze vies')

# num = 0
# while num <= 10:
#   num += 1
#   print(num)

# # Excercise: Emoji Art
# for num in range(1,11):
#   print("*" * num)

# times = 1
# while times <= 10:
#   print("*" * times)
#   times += 1

# for num in range(1,11):
#   count = 1
#   stars = ''
#   while count <= num:
#     stars += '*'
#     count += 1
#     print(stars)
