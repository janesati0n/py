# # Looping
# numbers = [1, 2, 3, 4, 5]
# doubled_numbers = []
# for num in numbers:
#   doubled_number = num * 2
#   doubled_numbers.append(doubled_number)
# print(doubled_numbers) # [2, 4, 6, 8, 10]

# # List Comprehension
# numbers = [1, 2, 3, 4, 5]
# doubled_numbers = [num * 2 for num in numbers]
# print(doubled_numbers) # [2, 4, 6, 8, 10]

# # Use with conditional logic
# numbers = [1, 2, 3, 4, 5, 6]
# evens = [num for num in numbers if num % 2 == 0]
# odds = [num for num in numbers if num % 2 != 0]
# print(f'odds: {odds}, evens: {evens}')
# [num*2 if num % 2 == 0 else num/2 for num in numbers]

# # Coding Excercise 20
# Create list of first letters for each name in given list
# answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
# Create list of all even values in given list
# answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]

# # Coding Excercise 21
# Create list that is the intersection of two
# answer = [num for num in [1,2,3,4] if num in [3, 4, 5, 6]]
# Create list with each word reversed and in lower case
# answer2 = [name[::-1].lower() for name in ['Elie', 'Tim', 'Matt']]

# # Coding Excercise 22
# Create list with all numbers divisible by 12 between 1 and 100
# answer =  [num for num in range(1,101) if num % 12 == 0]

# # Coding Excercise 23
# Create list containing letters from amazing but not the vowels
# answer = [val for val in 'amazing' if val not in 'aeiou']
