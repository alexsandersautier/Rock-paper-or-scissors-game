import random

game = ['rock','paper','scissors']
play=True

user_name = input('Type your name.: ')

while play:
    bot = random.choice(game)

    user_move = input('Choose a option: "rock" | "paper" | "scissors" .: ')


    if user_move == 'rock' and bot == 'scissors':
        print(f'You won, you {user_name} {user_move} and bot {bot}')

    elif user_move == 'rock' and bot == 'paper':
        print(f'You lost, you {user_name} {user_move} and bot {bot}')
        
    elif user_move == 'rock' and bot == 'rock':
        print(f'A tie, you {user_name} {user_move} and bot {bot}')


    elif user_move == 'scissors' and bot == 'paper':
        print(f'You won, you {user_name} {user_move} and bot {bot}')

    elif user_move == 'scissors' and bot == 'rock':
        print(f'You lost, you {user_name} {user_move} and bot {bot}')

    elif user_move == 'scissors' and bot == 'scissors':
        print(f'A tie, you {user_name} {user_move} and bot {bot}')



    elif user_move == 'paper' and bot == 'rock':
        print(f'You won, you {user_name} {user_move} and bot {bot}')

    elif user_move == 'paper' and bot == 'scissors':
        print(f'You lost, you {user_name} {user_move} and bot {bot}')

    elif user_move == 'paper' and bot == 'paper':
        print(f'A tie, you {user_name} {user_move} and bot {bot}')

    else:
        print('invalid move!')
        continue

    play_again = input('Would like to play again? (y/n) ')
    if play_again == 'n':
        ('Thanks for play my game! By Sautier Alexsander')
        play = False    