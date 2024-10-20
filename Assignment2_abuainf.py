'''COMPSCI 1MD3 Assignment 2: Games room with 3 different simple text-based games.

Allows user to play 'n' games, choosing from 3 game options.
Depending on game, user input is taken in and the game's function is called.
Calculates points won in each game, which is then returned as a final score.

Faris Abuain, McMaster, May 2024.'''

import random

## Coin Flip Game Function

def play_coin():
    ''' Coin Flips: Flips a coin 10 times and awards points for either heads or tails (depending on first flip).
    
    Parameters: *none*
    
    Returns: points (points gained by the player)
    
    Outputs: name of game, the coin flips, points gained by player
    
    '''
    points = 0     # initialize points variable
    flips = []     # store each flips value
    first_flip = random.randint(0,1)
    if first_flip == 0:    # heads = 0
        flips.append('H')  
    elif first_flip == 1:  # tails = 1
        flips.append('T')
    for _ in range(9):     # remainder of 10 total flips
        coin_flip = random.randint(0,1)
        if first_flip == 1 and coin_flip == 0: # if first flip was tails, subsequent heads worth 2 points
            points += 2
            flips.append('H')
        elif first_flip == 0 and coin_flip == 1: # if first flip was heads, subsequent tails worth 2 points
            points += 2
            flips.append('T')
        elif first_flip == 0 and coin_flip == 0: # no points, but still append heads value
            flips.append('H')
        elif first_flip == 1 and coin_flip == 1: # no points, but still append tails value
            flips.append('T')
    print("Coin Flips: ", end="")
    print(*flips, end="") # '*list' prints each individual element of a list on a single line
    print(f" = {points}")
    return points  # return the value so we can add to total score in games_room(n)      
        

## Number Guess Game function

def play_number_guess(guess):
    ''' Number Guess: Player guesses a number and recieves points depending on how close it is to number from two 6 sided die.

    Parameters: guess (player's guess as to what the result from the dice is)
    
    Returns: points (points gained by the player)
    
    Outputs: name of game, result of dice, player's guess, points gained by player

    '''
    points = 0     # initialize points variable
    result_1 = random.randint(1,6)   # roll first die
    result = result_1 + random.randint(1,6)  # roll second die
    if result == guess: 
        points += 10 
    elif (result - 2) <= guess <= (result+2): # determines whether user guess is within 2 of the actual result
        points += 5
    print(f"Number Guess: {result}, {guess} = {points}")
    return points # return the value so we can add to total score in games_room(n)


## Name assignment function for RPSLS Game

def name_assign(move_):
    ''' Name Assignment: helper function for assigning computer and player moves a specific name (i.e. string).

    Parameters: move_ (can either be player move or computer move)
    
    Returns: char (specific name represented by the numerical move)
    
    Outputs: *none*

    '''
    if move_ == 1:
        char = 'Rock'
    elif move_ == 2:
        char = 'Paper'
    elif move_ == 3:
        char = 'Scissors'
    elif move_ == 4:
        char = 'Lizard'
    elif move_ == 5:
        char = 'Spock'
    return char

## RPSLS Game Function

def play_rpsls(move):
    ''' Rock, Paper, Scissors, Lizard, Spock: Player chooses a move and faces against computer generated move.

    Parameters: move (player's chosen move)
    
    Returns: points (points gained by the player)
    
    Outputs: name of game, players move, computers move, points gained by player

    '''
    points = 0 # intialize points variable
    comp_move = random.randint(1,5) # chose random computer move
    ## Call name_assign function to assign proper name to player and computer's respective moves
    player = name_assign(move) 
    computer = name_assign(comp_move)
    if comp_move == move:
        points += 5 # a tie results in 5 points
    ## Checks if player beats computer and, if so, rewards 10 points for winning
    elif move == 1 and (comp_move == 3 or comp_move == 4):
        points += 10
    elif move == 2 and (comp_move == 1 or comp_move == 5):
        points += 10
    elif move == 3 and (comp_move == 2 or comp_move == 4):
        points += 10
    elif move == 4 and (comp_move == 2 or comp_move == 5):
        points += 10
    elif move == 5 and (comp_move == 1 or comp_move == 3):
        points += 10
    print(f"RPSLS: {player}, {computer} = {points}")
    return points # return the value so we can add to total score in games_room(n)



## GAME ROOM Function

def games_room(n):
    '''Games Room: Users can choose to play a game from a menu of 3 options.
    
    Parameters: n (number of games played)
    
    Returns: score (final score of player)
    
    Outputs: the game menu, text based on the specific game chosen
    
    ''' 
    ## Print the Menu of Game Options
    print("1. Coin Flips")
    print(" ")
    print("2. Number Guess")
    print(" ")
    print("3. RPSLS")
    print(" ")
    print(" ")
    score = 0 # intialize score variable for the players final score
    for _ in range(n):
        game = int(input("Choose a game from the menu above: ")) # choose number from 1 to 5, or help
        ## Call game function depending on users input
        if game == 1: 
            score += play_coin()
        elif game == 2:
            guess_user = int(input("What is your guess? ")) # user guess input
            score += play_number_guess(guess_user)
        elif game == 3:
            move_user = int(input("What is your move? ")) # user move input
            score += play_rpsls(move_user)
        print(" ") # space out each game (and the final score) for cleaner formatting
    return score # returns final score of the player!

            
## Call Game Room function! (here we have 3 games)

print(games_room(3)) # print in order for score to be displayed    

