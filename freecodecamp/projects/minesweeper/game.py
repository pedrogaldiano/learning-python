import random
import re

class Board:
    def __init__(self, side, bombs):
        self.side = side
        self.bombs = bombs
        
        # Create the board
        self.board = self.make_board()
        self.assign_values_board()
        
        # Keep Track of the locations uncovered
        self.dug = set()

    def make_board(self):
        board = [[' ' for _ in range(self.side)] for _ in range(self.side)]
        
        bombs_planted = 0
        while bombs_planted < self.bombs:
             loc = random.randint(0, self.side**2 - 1)
             row = loc // self.side
             col = loc % self.side
             
             if board[row][col] == ' ':
                 board[row][col] = '*'
                 bombs_planted += 1
        return board

    def assign_values_board(self):
        # Assign 0 - 8 for each spot
        # Do not overwrite the bombs ('*')     
        for r in range(self.side):
            for c in range(self.side):
                
                if self.board[r][c] == ' ':
                    self.board[r][c] = self.get_num_bombs(r, c)
                    
    def get_num_bombs(self, row, col): 
        num_bombs = 0
        for r in range(max(0, row-1), min(self.side-1, row+1)+1):
            for c in range(max(0, col-1), min(self.side-1, col+1)+1):
                if self.board[r][c] == '*':
                    num_bombs += 1
        
        return num_bombs
    
    def dig(self, row, col):
        # Return False if its a bomb, else return True
        
        self.dug.add((row,col))
        
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        # self.board[row][col] == 0
        for r in range(max(0, row-1), min(self.side-1, row+1) +1):
            print(r, end=',  ')
            for c in range(max(0, col-1), min(self.side-1, col+1) +1):
                if (r,c) in self.dug:
                    continue
                self.dig(r,c)
        return True
                
    def __str__(self):
        visible_board = [[None for _ in range(self.side)] for _ in range(self.side)]
        for row in range(self.side):
            for col in range(self.side):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
                    
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.side):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.side)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.side)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep      

def play(side=10, bombs=10):
    board = Board(side, bombs)
    safe = True
    
    while len(board.dug) < (board.side ** 2 - board.bombs):
        print(board)
        input_row = int(input(f'Choose a ROW [0 ~ {board.side}]:  '))
        input_col = int(input(f'Choose a COL [0 ~ {board.side}]:  '))
        
        if input_row < 0 or input_row > board.side or input_col < 0 or input_col > board.side:
            print("Invalid location. Try again.")
            continue
        
        safe = board.dig(input_row, input_col)
        
        if not safe:
            break
    if safe:
        print('\nYOU WON! :D\n')
    else:
        print('\nYOU LOST! D:\n')
        board.dug = [(r,c) for r in range(board.side) for c in range(board.side)]
        print(board)

if __name__ == '__main__':
    play()