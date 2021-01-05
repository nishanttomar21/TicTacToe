#############################################
# Tic Tac Toe using Magic Square Algorithm
# Nishant Tomar - 2020PMD4210
# M.Tech. IT
#############################################

# Importing libraries
from random import choice                                                                                                                                                       # To randomly select a position from an array (positions_left)
from itertools import combinations                                                                                                                                          # To generate combinations from a list

# Global variables for the game (Initialization)
playing_board = ["-","-","-","-","-","-","-","-","-"]
fixed_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
human_moves = []*5
computer_moves = []*4
positions_left = [1, 2, 3, 4, 5, 6, 7, 8, 9]                                                                                                                                  # Has positions left in array
magic_positions_left = [1, 2, 3, 4, 5, 6, 7, 8, 9]                                                                                                                     # Has magic values in array 
magic_square_board = [8, 3, 4, 1, 5, 9, 6, 7, 2]                                                                                                                    # Has magic values at a position
player = "human"
turn = 1                                                                                                                                                                                        # Odd -> Human, Even -> Computer
won = False
new_position = 0                                                                                                                                                                        # To set new calculated position      

# To add switch case to Python
class switch:
    def __init__(self, value):
        self.value = value
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        return False
    def __call__(self, *values):
        return self.value in values

# To display the board
def displayBoard(arr):
        print("\t" + str(arr[0]) + " | " + str(arr[1]) + " | " + str(arr[2]))                                                                                   # Only strings can be concatenated
        print("\t--------")
        print("\t" + str(arr[3]) + " | " + str(arr[4]) + " | " + str(arr[5]))
        print("\t--------")
        print("\t" + str(arr[6]) + " | " + str(arr[7]) + " | " + str(arr[8]))

# To display the initialization of the game
def initializeGame():
    print("\n\n############################################")
    print("\tGame - Tic Tac Toe(Magic Square)!")
    print("############################################\n\n")
    print("Board positions:\n")
    displayBoard(fixed_positions)
    print("\n\nInitial Board:\n")
    displayBoard(playing_board)
    print("\n-------------------------------------------------------------------")

# To set the current player
def setPlayer():
    global player                                                                                                                                                                    # To reference global variable, as assignment will make it refer to local variable
    player = "human" if (turn % 2) else "computer"                                                                                                         # Ternary Operator  (To set the player)

# To generate a random value from the array inputs
def generateRandomPosition():
    return choice(positions_left)

# To update the playing board and dependent values of variables
def addPositionToBoard(position):
    magic_square_value = magic_square_board[int(position)-1]
    playing_board[int(position)-1] = "X" if (player == "human") else "O"                                                                                                # Ternary Operator (To add O or X to the player position)
    positions_left.remove(int(position))                                                                                                                                                         # To remove the occupied position magic value from array
    magic_positions_left.remove(magic_square_value)                                                                                                                              # To remove the occupied position from array
    human_moves.append(magic_square_value) if (player == "human") else computer_moves.append(magic_square_value)     # Ternary Operator (To add the move's magic value to player_moves array)
    increamentTurn()                                                                                                                                                                                         # Increament the turn

# To increament the turn value
def increamentTurn():
    global turn                                                                                                                                                                       # To reference global variable, as assignment will make it refer to local variable
    turn += 1

# To check if player added a valid input position (within range, empty position and is digit)
def checkInput(value):
    return 1 if (value.isdigit() and int(value) > 0 and int(value) < 10 and int(value) in positions_left) else 0

# Take input from the player
def takeInput():
    human_input = input()                                                                                                                                                   # Take input from the player
    input_passed = checkInput(human_input)                                                                                                                 # Checking the entered input

    # If input is valid, return that input
    if (input_passed):
        return human_input

    # if input is invaid, return false
    else:
        print("Please enter a valid position!")
        return 0

# To display and input current chance information
def displayChanceInformation():
    # Human
    if(player == "human"):
        # Loop till the input value is not valid
        while (True):
            print("\n\nTurn " + str(turn) + " -> " + "You (Enter any position from " + str(positions_left) + "): ", end = ' ')                                               # (end = ' ') -> To remove new-line
            human_input = takeInput()

            if human_input:
                break

            else:
                continue
        print()
        return human_input
    #Computer

    else:
        print("\n\nTurn " + str(turn) + " -> " + "Computer\n")

# To display the winning statement 
def displayWinningStatement():
    print("\n\n#############################\n")
    print("\t   You Won!" if (player == "human") else "\tComputer Won!")
    print("\n#############################\n\n")

# To display the game draw statement
def displayDrawStatement():
    print("\n\n###########################\n")
    print("\tGame draw!")
    print("\n###########################\n\n")

# To check if a player has won or not
def checkIfWon(arr):
    # Checking if co-linearity exists
    for combination in combinations(human_moves if (player == "human") else computer_moves, 3):                        # Generating all unique combinations of length 3 from list
        if (sum(combination) == 15):                                                                                                                                          # Checking if sum of 3 moves is 15
            global won
            won = True
            break

# Human chance to play
def humanChance():
    human_input = displayChanceInformation()                                                                                                                     # Printing and inputing turn information
    addPositionToBoard(human_input)                                                                                                                                   # Adding the input position to playing board                                                                                                                        

    # If more than 3 chances are played, then check if won after playing the chance
    if (turn  > 3):
        checkIfWon(human_moves)

# Basic computer chance (Select random position and play)
def computerChance():
    displayChanceInformation()                                                                                                                                               # Printing information 
    new_random_position = generateRandomPosition()                                                                                                      # Genarte a valid random position from the board
    addPositionToBoard(new_random_position)                                                                                                                  # Adding the random position to playing board

# Check for winning position
def checkWinningPosition(player):
    winning_position_exists = False

    # Checking if co-linearity exists
    for combination in combinations(human_moves if (player == "human") else computer_moves, 2):                                                                      # Generating all unique combinations of length 3 from list
        colinear_condition_variable = 15 - sum(combination)                                                                                                                                              # Conditions -> 1) 15 - (Sum of 2 positions) <= 9; 2) Winning position >= 1

        if (colinear_condition_variable < 10 and colinear_condition_variable > 0 and  colinear_condition_variable in magic_positions_left):          # Checking colinear condition exists          
            global new_position
            new_position = magic_square_board.index(colinear_condition_variable) + 1                                                                                                    # Getting index of magic value (winning position)
            winning_position_exists = True
            
            if (player == "computer"):
                global won
                won = True
            break

    return winning_position_exists
    
# To start playing the game (Tic Tac Toe)
def startGame():
    while (turn != 10):                                                                                                                                                                 # Loop till 9 chances (turns)
        setPlayer()                                                                                                                                                                         # Set player at each iteration

        # Switch case with condition of turn
        with switch(turn) as case:                                                                                                                                                # Custom switch condition
            # Initial random chances
            if case(1, 2, 3):
                # Chance of computer
                if (player == "computer"):
                    computerChance()
                    
                # Chance of human   
                else:
                    humanChance()       
                    
                displayBoard(playing_board)                                                                                                                                  # Display the game board
                
            # Checking magic square for each chance       
            elif case(4, 5, 6, 7, 8, 9):
                # Chance of computer
                if (player == "human"):
                    humanChance()
                    
                # Chance of Compter (Main crux of magic square algorithm)
                else:
                    displayChanceInformation()
                    
                    # First check if computer is winning or not
                    if (checkWinningPosition('computer')):
                        addPositionToBoard(new_position)
                        
                    # If computer not winning, then check if user might win in another chance or not
                    elif (checkWinningPosition('human')):
                        addPositionToBoard(new_position)
                        
                    # If none conditions true, then choose a random valid position and play
                    else:
                        computerChance()

                displayBoard(playing_board)                                                                                                                                 # Display the game board

            # Default case       
            else:
                print("Please enter a valid position!\n\n")

            # If any player won, break the loop 
            if (won):
                displayWinningStatement()                                                                                                                                   # Display winning statement
                break

    # If no one wins, then game draw
    if (not won):
        displayDrawStatement()                                                                                                                                                  # Display draw statement

# So that this function doesn't run when some other file imports this file
if __name__ == "__main__":
    initializeGame()
    startGame()
