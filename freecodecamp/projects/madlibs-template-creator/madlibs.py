# Madlibs is a word (aka string) concatenation game where you have a predefined
# text with a lot of blank spaces which you will add words to.
# This program creates a unique template where you just have to insert a text and
# Define the percentage of blank spaces

from random import randint

# Choose the filename
while True:
    filename = 'madlibs.txt'#input('Filename: ')
    try:
        x = open(filename, 'r')
        x.close()
        break
    except:
        print(f'{filename} not found.')
        pass

# Percentage of the text you wanto to convert to '_____'
while True:
    percent = 30#input("Percentage 0-100 (exclusive) of blank spaces: ")
    try:
        percent = int(percent)
        if type(percent) == int and percent > 0 and percent < 100:
            break
    except:
        print("This value must be an integer between 0 and 100 exclusive.")
        pass

# Read the text in the specifiedfile

with open(filename, 'r') as raw:
    verify = 0
    result = ''
    
    for line in raw:
         words = line.split()
        
# Switch words randomly to '_______' 
# You can't change any word more than one time
         total_words = len(words)
         replacements = int((percent/100) * total_words)
        
         single = []
         for i in range(replacements):
             swipe = randint(0, total_words - 1)

             if not swipe in single:
                 single.append(swipe)          
                 words[swipe] = ' ________ '
             else:
                continue

# List to string
         result += ' '.join(words) + '\n'

# Write it into a new file
    if verify == 1:
        newfile = open('my-madlibs.txt', 'a')
        newfile.write(result)
    else:
        newfile = open('my-madlibs.txt', 'w')
        newfile.write(result)
        verify = 1
    
newfile.close()