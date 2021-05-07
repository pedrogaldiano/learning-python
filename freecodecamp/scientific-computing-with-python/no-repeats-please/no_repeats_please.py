# https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/no-repeats-please
from random import sample

# Factorial N! => N * (N-1)! => N * (N-1) * (N-2)!...
def fact(n):
    if n == 1: return 1
    else: return n * fact(n-1)
    
# Permute the letters of a word and return the unique samples
def permAlone(word):
    
    # Convert the string word to a tuple
    word = tuple(word)
    if len(set(word)) == 1 : return 0
    
    length = len(word)
    index = list(range(length))
    possibilities = fact(length)
    permutations = []
    counter = 0
    
    # Create a random sample (test) and checks if this test
    # Have been placed in the permutations list, if not append it
    while True:
        test = sample(index, length)
        
        if not test in permutations: permutations.append(test)
        
        if len(permutations) == possibilities:
            
            # Convert the permutations in letters
            for sub in permutations:
                for key, value in enumerate(sub):
                    sub[key] = word[value]
                # Count if there is the same letter repeating
                for i in range(length - 1):
                    if sub[i] == sub[i+1]:
                        counter += 1
                        break
            return possibilities - counter
     
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
