# TIC TAC TOE
# It's a Tic Tac Toe Game where  you play against the computer

# Library:
from random import randint

# Globals
UserSymbol = PCSymbol = ''
positions = ['7', '8', '9', '4', '5', '6', '1', '2', '3']
order = 3
round = 0


# I don't understand how a class works (yet)
class STOP(Exception): pass


# Functions:
# Print the board:
def PrintBoard():
    global positions
    print()
    k = 0
    for i in range(3):
        for l in range(3):
            print(f'    |{positions[k]}|', end='')
            k += 1
        print()
    print('\n   ====================')

# Choose your symbol
def ChooseSymbol():
    global UserSymbol, PCSymbol
    while True:
        UserSymbol = input('Select "X" or "O":  ')
        if UserSymbol == 'X':
            PCSymbol = 'O'
            break
        elif UserSymbol == 'O':
            PCSymbol = 'X'
            break
    print('You choose: ' + UserSymbol + '\n PC choose: ' + PCSymbol)

# Check winner
def CheckWinner(User):
    global positions, round
    if round == 9:
        print('\nTie!')
        quit()
    elif round > 4:
        if         ((positions[0] == positions[1] == positions[2] == User)
                or (positions[3] == positions[4] == positions[5] == User)
                or (positions[6] == positions[7] == positions[8] == User)
                or (positions[0] == positions[3] == positions[6] == User)
                or (positions[1] == positions[4] == positions[7] == User)
                or (positions[2] == positions[5] == positions[8] == User)
                or (positions[0] == positions[4] == positions[8] == User)
                or (positions[2] == positions[4] == positions[6] == User)):
            print()
            print('Winner: ' + User)
            exit()

# Make your move
def Play(User, pos):
    global positions, round
    for index, value in enumerate(positions):
        if value == pos:
            positions[index] = User
            PrintBoard()
            round += 1
            raise STOP

# Main
def main():
    global order
    ChooseSymbol()
    PrintBoard()
    order = randint(0,1)

    # Gameplay
    while True:
        if order == 1:
            while True:
                try:
                    Play(PCSymbol, str(randint(1, 9)))
                except STOP:
                    break
            CheckWinner(PCSymbol)
            order = 0

        if order == 0:
            while True:
                try:
                    pos = input('Select a number:  ')
                    Play(UserSymbol, pos)
                except STOP:
                    break
            CheckWinner(UserSymbol)
            order = 1

if __name__ == '__main__':
    main()
