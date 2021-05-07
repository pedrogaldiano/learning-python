# Find the Symmetric Difference 
# https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/find-the-symmetric-difference
def sym(*args):
    
    # Check if the user typed more than one argument
    lenght = len(args)
    if lenght == 1: return list(set(args[0]))
    elif lenght < 1: return "Error: missing arguments."
    
    # Cast Set to remove duplicates, than cast list so you can work with the list
    list_A = list(set(args[0]))
    list_B = list(set(args[1]))
    
    # Concatenate both lists and sort it
    list_AB = (list_A + list_B)
    list_AB.sort()
    
    # Variables
    key = 2 # Used as a filter for the if statements below
    new = [] # The New list
    
    while True:
        # Stop the loop
        if key > lenght: 
            return new
        # There is more than 2 args
        elif key > 2:
            list_AB = new + list(set(args[key-1]))
            list_AB.sort()
            new = []
        # Put the correct element in the new list and remove it if needed
        for x in list_AB:
            if x not in new:
                new.append(x)
                continue
            elif x in new:
                new.remove(x)
        key += 1

print('\nFreeCodeCamp Testing...')       
if sym([1, 2, 3], [5, 2, 1, 4]) == [3, 4, 5]: print('OK')
if sym([1, 2, 3, 3], [5, 2, 1, 4]) == [3, 4, 5]: print('OK')
if sym([1, 2, 3], [5, 2, 1, 4, 5]) == [3, 4, 5]: print('OK')
if sym([1, 2, 5], [2, 3, 5], [3, 4, 5]) == [1, 4, 5]: print('OK')
if sym([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5]) == [1, 4, 5]: print('OK')
if sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3]) == [2, 3, 4, 6, 7]: print('OK')
if sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]) == [1, 2, 4, 5, 6, 7, 8, 9]: print('OK')
