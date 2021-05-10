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