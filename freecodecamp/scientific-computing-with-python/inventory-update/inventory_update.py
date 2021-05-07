def updateinventory(curInv, newInv):

    temp = []
    # Convert curInv in a dict
    # (It may have two items with the same quantities, so I must switch the order)
    for old in curInv:
        old.reverse()
        temp.append(old)

    curInv = dict(temp)
    temp = []
    
    # Convert newInv in a dict 
    # (It may have two items with the same quantities, so I must switch the order)
    for new in newInv:
        new.reverse()
        temp.append(new)
    newInv = dict(temp)
    del temp
    
    # Add up the the old quantities and the new quantities or insert a new product
    for key, value in newInv.items():
        if key in curInv:            
            curInv.update({key: curInv[key] + value})
        else:
            curInv.update({key: value})
    
    # Sort the keys
    keys = []
    for key in curInv.keys():
        keys.append(key)
    keys = sorted(keys)
    
    # Use the keys sorted to create a list with the [['value1, key1'], ['value2', 'key2'] ['value3', 'key3']]
    final = []
    for key in keys:
        final.append([curInv[key], key])

    return final
    
# Testing using the FreeCodeCamp references
print('FreeCodeCamp testing...')
if updateinventory([[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]], [[2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"], [7, "Toothpaste"]]) == [[88, "Bowling Ball"], [2, "Dirty Sock"], [3, "Hair Pin"], [3, "Half-Eaten Apple"], [5, "Microphone"], [7, "Toothpaste"]]: print(' => OK')

if updateinventory([[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]], []) == [[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]]: print(' => OK')

if updateinventory([], [[2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"], [7, "Toothpaste"]]) == [[67, "Bowling Ball"], [2, "Hair Pin"], [3, "Half-Eaten Apple"], [7, "Toothpaste"]]: print(' => OK')

if updateinventory([[0, "Bowling Ball"], [0, "Dirty Sock"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]) == [[1, "Bowling Ball"], [0, "Dirty Sock"], [1, "Hair Pin"], [1, "Half-Eaten Apple"], [0, "Microphone"], [1, "Toothpaste"]]: print(' => OK')
