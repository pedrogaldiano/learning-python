class Game:
    def __init__(self):
        # self.board = [''] * 9 
        self.board = [' ' for _ in range(9)] # Create our board (3X3)
        self.current_winner = None # Keep track of winner
        
        
    def print_board(self):
        pb = '-------------' + '\n'
        for row in [self.board [i*3: (i+1)*3] for i in range(3)]:
            pb += '| ' + ' | '.join(row) + ' |' + '\n' + '-------------' +'\n'
        print(pb)
        
    @staticmethod
    def print_boad_nums():
        pb = '-------------' + '\n'
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            pb += '| ' + ' | '.join(row) + ' |' + '\n' + '-------------' +'\n'
        print(pb)
        
            

x = Game()
# x.print_board()
x.print_boad_nums()