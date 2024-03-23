# # First Attempt
# from random import randint
# number = randint(1,10)
# guess = 0
# play_again = 'y'
# while play_again != 'n':
#   while guess != number:
#     guess = input("Guess a number between 1 and 10: ")
#     guess = int(guess)
#     if guess > number:
#       hint = 'Too high'
#     elif guess < number:
#       hint = 'Too low'
#     print(f"{hint}, try again!")
#   print("You guessed it! You won!")
#   play_again = input("Do you want to keep playing? (y/n) ")

# # Solution
# from random import randint
# random_number = randint(1,10)
# guess = None
# while True:
#   guess = input("Guess a number between 1 and 10: ")
#   guess = int(guess)
#   if guess < random_number:
#     print("Too low, try again!")
#   elif guess > random_number:
#     print("Too high, try again!")
#   else:
#     print("You guessed it! You won!")
#     play_again = input("Do you want to keep playing? (y/n) ")
#     if play_again == 'y':
#       random_number = randint(1,10)
#       guess = None
#     else:
#       print('Thanks for playing. Bye!')
#       break
