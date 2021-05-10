# Players choose their letter
# Create a class player
# Create a move method
# Create a function to print out the board
# Check if there is a winner

# The game runs like:
    # P1 = X
    # P2 = O
    # Random P starts:
        # Create a list in 
        # [P1,P2,P1,P2,P1,P2]
        # while true:
            # 
            # 
            
import player

def main():
    
    while True:
        letter = input('Player 1, Choose [x or o]:  ')
        if letter == 'x' or letter == 'o':
            break
    
    if letter == 'x': 
        letter2 = 'o' 
    else:
        letter2 = 'x'
    
    P1 = player.Player(letter)
    P2 = player.Player(letter2)
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    main()  
