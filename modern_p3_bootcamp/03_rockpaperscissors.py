# # Rock, Paper, Scissors
# # Basic Version
# print('...rock...')
# print('...paper...')
# print('...scissors...')
# player1 = input("enter Player 1's choice: ")
# player2 = input("enter Player 2's choice: ")
# if player1 and player2:
#   print('SHOOT!')
#   if player1 == 'rock' and player2 == 'scissors' or player1 == 'scissors' and player2 == 'paper' or player1 == 'paper' and player2 == 'rock':
#     print('player1 wins')
#   elif player1 == player2:
#     print('draw')
#   else:
#     print('player2 wins')
# else:
#   print('wrong input!')

# # Refactoring
# print('...rock...')
# print('...paper...')
# print('...scissors...')
# player1 = input("enter Player 1's choice: ")
# print('***NO CHEATING***\n' * 50)
# player2 = input("enter Player 2's choice: ")
# if player1 == player2:
#   print('draw')
# elif player1 == 'rock':
#   if player2 == 'scissors':
#     print('player1 wins')
#   elif player2 == 'paper':
#     print('player2 wins')
# elif player1 == 'scissors':
#   if player2 == 'paper':
#     print('player1 wins')
#   elif player2 == 'rock':
#     print('player2 wins')
# elif player1 == 'paper':
#   if player2 == 'rock':
#     print('player1 wins')
#   elif player2 == 'scissors':
#     print('player2 wins')
# else:
#   print('something went wrong')

# # Playing against computer
# from random import randint
# print('...rock...')
# print('...paper...')
# print('...scissors...')
# player = input("enter Player's choice: ")
# rand_num = randint(0,2)
# if rand_num == 0:
#   computer = 'rock'
# elif rand_num == 1:
#   computer = 'paper'
# else:
#   computer = 'scissors'
# print(f'The computer plays {computer}')
# if player == computer:
#   print('draw')
# elif player == 'rock':
#   if computer == 'scissors':
#     print('Player wins')
#   elif computer == 'paper':
#     print('Computer wins')
# elif player == 'scissors':
#   if computer == 'paper':
#     print('Player wins')
#   elif computer == 'rock':
#     print('Computer wins')
# elif player == 'paper':
#   if computer == 'rock':
#     print('Player wins')
#   elif computer == 'scissors':
#     print('Computer wins')
# else:
#   print('Something went wrong')
