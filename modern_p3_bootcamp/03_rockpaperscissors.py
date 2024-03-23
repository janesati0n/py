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
# player = input("Player, make your move: ").lower()
# rand_num = randint(0,2)
# if rand_num == 0:
#   computer = 'rock'
# elif rand_num == 1:
#   computer = 'paper'
# else:
#   computer = 'scissors'
# print(f'Computer plays {computer}')
# if player == computer:
#   print("It's a tie!")
# elif player == 'rock':
#   if computer == 'scissors':
#     print('Player wins!')
#   else:
#     print('Computer wins!')
# elif player == 'scissors':
#   if computer == 'paper':
#     print('Player wins!')
#   else:
#     print('Computer wins!')
# elif player == 'paper':
#   if computer == 'rock':
#     print('Player wins!')
#   else:
#     print('Computer wins!')
# else:
#   print('Please, enter a valid move!')

# # Improved after Loops Section
# from random import randint
# player_wins = 0
# computer_wins = 0
# winning_score = 1
# while player_wins < winning_score and computer_wins < winning_score:
#   print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
#   print('...rock...')
#   print('...paper...')
#   print('...scissors...')
#   player = input("Player, make your move: ").lower()
#   if player == 'quit' or player == 'q':
#     break
#   rand_num = randint(0,2)
#   if rand_num == 0:
#     computer = 'rock'
#   elif rand_num == 1:
#     computer = 'paper'
#   else:
#     computer = 'scissors'
#   print(f'Computer plays {computer}')
#   if player == computer:
#     print("It's a tie!")
#   elif player == 'rock':
#     if computer == 'scissors':
#       print('Player wins!')
#       player_wins += 1
#     else:
#       print('Computer wins!')
#       computer_wins += 1
#   elif player == 'scissors':
#     if computer == 'paper':
#       print('Player wins!')
#       player_wins += 1
#     else:
#       print('Computer wins!')
#       computer_wins += 1
#   elif player == 'paper':
#     if computer == 'rock':
#       print('Player wins!')
#       player_wins += 1
#     else:
#       print('Computer wins!')
#       computer_wins += 1
#   else:
#     print('Please, enter a valid move!')
# if player_wins > computer_wins:
#   print("CONGRATS, YOU WON!")
# elif player_wins == computer_wins:
#   print("IT'S A TIE")
# else:
#   print("OH NO :( THE COMPUTER WON!")
# print(f"FINAL SCORES... Player: {player_wins} Computer: {computer_wins}")
