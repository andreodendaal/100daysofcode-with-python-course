
from player import Player
#import roll 
from call import Rock, Scissors, Paper
import random

def main():
    print_header()
    roll_options = ["rock", "paper", "scissors"]

    roll_options = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("Computer")

    game_loop(player1, player2, roll_options)

def game_loop(player1, player2, roll_options):
    
    count = 1
    while count <= 3:

        # display throws
        p2_roll = random.choice(roll_options)
        p1_roll = player_choices(roll_options)
        print('{0} rolled {1} & {2} rolled {3} '.format(player2.name, p2_roll.roll_type, player1.name, p1_roll.roll_type))
        
        if p1_roll != p2_roll:
            if p1_roll.can_defeat(p2_roll.roll_type): 
                player1.score_total(1)
                round_winner = player1.name
            else:
                player2.score_total(1)
                round_winner = player2.name
        
            # display winner for this round        
            print('{0} won this round!'.format(round_winner))
            count += 1
        else:
            print('Draw, go again!')

    # Compute who won
    if player1.score > player2.score:
        winner = player1.name
    else:
        winner = player2.name

    print(winner + " won the tournement!")


def build_the_three_rolls():
    options = []
    rock = Rock()    
    options.append(rock)
    
    paper = Paper()
    options.append(paper)

    scissors = Scissors()
    options.append(scissors)

    return options

def player_choices(options):
    
    choice = ''
    choice = input('Chose: [R]ock, [P]aper, [S]cissors,  [Q]uit: ')
    if choice == 'R' or choice == 'r':
        player_choice = options[0]
    elif choice == 'P' or choice == 'p':
        player_choice = options[1]
    elif choice == 'S' or choice == 's':
        player_choice = options[2]
    else:            
        player_choice = 'quit' 
        print("Ending game")

    return player_choice


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
