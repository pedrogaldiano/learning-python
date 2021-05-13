# Compare a binary search algorithm and a naive search in a SORTED LIST
# Naive search: scan the entire list, and check if its equal to the target

# Look for an element in a list and return its index or None (if it doens't exist)
import time
import random

def naive_search(ls, target):
    for element in ls:
        if element == target:
            return ls.index(element)
    return None


# Binary search leverage the fact that the list is sorted
def binary_search(ls, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(ls) - 1 # len([0,1,2,3,4]) == 5
    
    if high < low: # low > high
        return None
    midpoint = (high + low) // 2

    if ls[midpoint] == target:
        return midpoint
    
    elif ls[midpoint] > target: # Left-side
        return binary_search(ls, target, low, midpoint - 1)
    
    else: # Rigth-side
        return binary_search(ls, target, midpoint + 1, high)


def main():
    
    length = 100000
    ls = set()
    
    while len(ls) < length:
        ls.add(random.randint(-3*length, 3*length))
    ls = sorted(list(ls))
    
    start = time.time()
    for elm in ls:
        naive_search(ls, elm)
    end = time.time()
    print(f"Naive search:  {(end-start)/length} seconds")
    
    start = time.time()
    for elm in ls:
        binary_search(ls, elm)
    end = time.time()
    print(f"Binary search:  {(end-start)/length} seconds")
    

    
if __name__ == "__main__":
    main()

        
    
