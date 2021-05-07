# This version will not pass successfully the test.py
# Because it print out the problems rather than return it

from sys import exit as STOP


def print_arithmetic_arranger(problems, answer=False):
    if len(problems) > 5:
        STOP('Error: Too many problems.')
    
    values = [] 
    final = [] 
    
    for i in range(len(problems)):
        for j in problems[i]:
            
            if j.isdigit():
                values.append(j)
                    
            elif j.isalpha():
                STOP("Error: Numbers must only contain digits.")
                
            elif j == '+' or j == '-':
                final.append(int(''.join(values)))
                values = []
                    
                final.append(j)
                    
            elif j != ' ':
                STOP("Error: Operator must be '+' or '-'.")
                    

        final.append(int(''.join(values)))
        values = []
    del problems
    del values
    
    value1 = []
    symbol = []
    value2 = []
    
    for i in range(len(final)):
        temp = final[i]
        
        try:
            if temp > 9999:
                STOP("Error: Numbers cannot be more than four digits.")
        except:
            pass
        
        if i in [0, 3, 6, 9, 12]:
            value1.append(temp)
        if i in [1, 4, 7, 10, 13]:
            symbol.append(temp)
        if i in [2, 5, 8, 11, 14]:
            value2.append(temp)
            
    del final        
    lenght = range(len(symbol))
    
    space = []
    
    for i in lenght:
        space.append(max((len(str(value1[i]))), (len(str(value2[i])))))
    
    for i in lenght:
        print(str(value1[i]).rjust(space[i] + 2,' '), end='    ')    
    print()
    
    for i in lenght:
        print(symbol[i], end=' ')
                
        print(str(value2[i]).rjust(space[i], ' '), end='    ')
    print()
    
    for i in lenght:
        print( '-' * (space[i] + 2), end='    ')
    
    if answer == True:
        print()
        for i in lenght:
            if symbol[i] == '+':
                print(str(value1[i] + value2[i]).rjust(space[i] + 2), end='    ')
            
            elif symbol[i] == '-':
                print(str(value1[i] - value2[i]).rjust(space[i] + 2), end='    ')
                
print_arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
