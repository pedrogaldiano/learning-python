# import time
import random
import math



class Player:
    def __init__(self, letter):
        self.letter = letter
        
    def get_move(self, game):
        pass



class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_pos = False
        while not valid_pos:
            position = input('Choose a spot 0 ~ 8:  ')
            try:
                position = int(position)
                if not position in game.avaiable_moves():
                    raise ValueError
                valid_pos = True
            except ValueError:
                print("Type a number between 0 and 8 (inclusive).")
        return position
    
    
    
class RandomComputer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        position = random.choice(game.avaiable_moves())
        return position
    
    
    
class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        if game.number_empty_spots() == 9:
            spot = random.choice(game.avaiable_moves())
        else:
            spot = self.minimax(game, self.letter)['position']
        return spot
    
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'
        
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.number_empty_spots() + 1) if other_player == max_player else -1 * (state.number_empty_spots() + 1)}
        elif not state.empty_spots():
            return {'position': None, 'score': 0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}
        
        for possible_move in state.avaiable_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)
            
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
    
    

class TicTacToe:
    def __init__(self):
        self.board = [' ' for i in range(9)]
        self.current_winner = None
    
    
    def print_board(self):
        pb = '-------------\n'
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]:
            pb += '| ' + ' | '.join(row) + ' |' + '\n-------------\n'
        print(pb)
        
    @staticmethod
    def print_board_number():  
        pbn =  '-------------\n'
        board_index = [[str(i) for i in range((j*3), (j+1)*3)] for j in range(3)]        
        for row in board_index:
            pbn += '| ' + ' | '.join(row) + ' |' + '\n-------------\n'
        print(pbn)
    
    def avaiable_moves(self):
        # Return an index list of the empty spots
        return [index for index, val in enumerate(self.board) if val == ' ']
        
    def empty_spots(self):
        # Return True if there is blank in self.board
        return ' ' in self.board 
       
    def number_empty_spots(self):
        return len(self.avaiable_moves())
    
    def make_move(self, pos, letter):
        if self.board[pos] == ' ':
            self.board[pos] = letter
            if self.winner(pos, letter): # Does this move win the game?
                self.current_winner = letter
            return True
        return False
    
    def winner(self, spot, letter):
        # 3 x or o in a row
        row_index = spot // 3 # This spot is on which row?
        row = self.board[row_index * 3 : (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        col_index = spot % 3 # This spot is on which column?
        column = [self.board[col_index + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # Diagonal indices (0, 4, 6) or (2, 4, 8)
        if spot % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all ([spot == letter for spot in diagonal2]):
                return True
        return False
        
    
    
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_number()
    letter = 'X'
    
    while game.empty_spots():
        if letter == 'O':
            spot = o_player.get_move(game)
        else:
            spot = x_player.get_move(game)
        
        if game.make_move(spot, letter):
            if print_game:
                # time.sleep(1)
                print(f"{letter} makes a move to square {spot}")
                game.print_board()
                print()
            if game.current_winner:
                if print_game:
                    print(f"{letter} WINS!!\n")
                return letter
            letter = 'O' if letter == 'X' else 'X'
    if print_game:
        print('It\'s a tie!\n')
    
if __name__ == '__main__':
    print('aguarde...')
    x_win = 0
    o_win = 0
    tie = 0
    for i in range(100):
        x_player = SmartComputerPlayer('X')
        o_player = SmartComputerPlayer('O')
        t = TicTacToe()
        a = play(t, x_player, o_player, print_game=False)
        if a == 'X':
            x_win += 1
        elif a == 'O':
            o_win += 1
        else:
            tie += 1
    print(f"X  {x_win}\nO  {o_win}\ntie  {tie}")