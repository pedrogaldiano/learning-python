def arithmetic_arranger(problems, answer=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    values = [] 
    final = []
    
    for i in range(len(problems)):
        for j in problems[i]:
            
            if j.isdigit():
                values.append(j)
                    
            elif j.isalpha():
                return "Error: Numbers must only contain digits."
                
            elif j == '+' or j == '-':
                final.append(int(''.join(values)))
                values = []
                    
                final.append(j)
                    
            elif j != ' ':
                return "Error: Operator must be '+' or '-'."
                    

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
                return "Error: Numbers cannot be more than four digits."
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
    key = len(symbol) - 1
    
    space = []
    
    s = ''
    
    for i in lenght:
        space.append(max((len(str(value1[i]))), (len(str(value2[i])))))
    
    for i in lenght:
        s = s + str(str(value1[i]).rjust(space[i] + 2,' '))
        
        if i < key : s += '    '
        
    s = s + '\n'
                              
    for i in lenght:
        s = s + str(symbol[i]) + ' ' 
        s = s + str(str(value2[i]).rjust(space[i], ' '))
        
        if i < key : s += '    '
        
    s = s + '\n'
    
    for i in lenght:
        s = s + str( '-' * (space[i] + 2))
        
        if i < key : s += '    '
    
    if answer == True:
        s = s + '\n'
        for i in lenght:
            if symbol[i] == '+':
                s = s + str(str(value1[i] + value2[i]).rjust(space[i] + 2))
                
                if i < key : s += '    '
            
            elif symbol[i] == '-':
                s = s + str(str(value1[i] - value2[i]).rjust(space[i] + 2))
                
                if i < key : s += '    '
   
    arranged_problems = s
    return arranged_problems
