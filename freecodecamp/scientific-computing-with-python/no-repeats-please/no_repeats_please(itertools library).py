# https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/no-repeats-please
from itertools import permutations as permute

def permAlone(word):
    
    if not word.isalpha(): return "Error: must contain only letters."
    word = list(word.lower())
    
    lenght = range(len(word) - 1)
    
    if len(set(word)) == 1: return 0
 
    ls = list(permute(word))
    
    counter = 0
    
    for sublist in ls:
        for i in lenght:
            if sublist[i] == sublist[i+1]: 
                counter += 1
                break

    return len(ls) - counter
    
        
print('FreeCodeCamp testing...')
if permAlone("aaabb") == 12: print('OK 0')
if permAlone("aab") == 2: print('OK 1')
if permAlone("aaa") == 0: print('OK 2')
if permAlone("aabb") == 8: print('OK 3')
if permAlone("abcdefa") == 3600: print('OK 4')
if permAlone("abfdefa") == 2640: print('OK 5')
if permAlone("zzzzzzzz") == 0: print('OK 6')
if permAlone("a") == 1: print('OK 7')
if permAlone("aaab") == 0: print('OK 8')
