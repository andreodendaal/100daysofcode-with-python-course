from player import Player
import roll 
from call import Call
import random

def main():
    print_header()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)

def game_loop(player1, player2, rolls):
    count = 1
    while count < 3:
        p2_roll = None # TODO: get random roll
        p1_roll = None # TODO: have player choose a roll

        outcome = p1_roll.can_defeat(p2_roll)

        # display throws
        # display winner for this round

        count += 1

    # Compute who won

def build_the_three_rolls(type):
    rolls = ["rock", "paper", "scissors"]
    for i in rolls:
        Call(rolls[i])

def build_the_three_rolls2(type):
    rolls = ["rock", "paper", "scissors"]
    choice = ''
    if type == 'random':
        choice = random.choice(rolls)
        player_roll = roll(choice)
        return player_roll
    elif type == 'choose':
        choice = input('Chose: [R]ock, [P]aper, [S]cissors,  [Q]uit: ')
        if choice == 'R' or choice == 'r':
            player_choice = 'rock'
        elif choice == 'S' or choice == 's':
            player_choice = 'scissors'
        elif choice == 'P' or choice == 'p':
            player_choice = 'paper'
        else:            
            player_choice = 'quit' 
            print("Ending game")


def get_players_name():
    input_name = input('What is your name?: ')
    return input_name

def print_header():
    print('---------------------------------')
    print('      ROCK, PAPER, SCISSORS')
    print('---------------------------------')
    print()

if __name__ == '__main__':
    main()
